from datetime import date
from dateutil.relativedelta import relativedelta
from collections import Counter
import json

month = ''
date_range = []

with open('user_setting.json', 'r', encoding="utf8") as f:
    user_setting = json.load(f)


def __common_tag_topic(q):
    tag_counter = Counter(sum((i.list_tags() for i in q), []))
    topic_counter = Counter(sum((i.list_edu_category() for i in q), []))
    if len(tag_counter):
        problems = ', '.join(str(v) + '起' + k for (k, v) in tag_counter.most_common(user_setting['warning_num']))
        return problems, tag_counter, topic_counter

    return None


def __template1(x):
    if x[0] is None:
        return x[1], user_setting['warning_template_3'] % (
            user_setting['warning_year'],
            '~'.join([str(i) for i in month])
        )
    return x[1], user_setting['warning_template_1'] % (
        user_setting['warning_year'], '~'.join([str(i) for i in month]),
        x[0][0],
        x[0][1].most_common(1)[0][0],
        x[0][2].most_common(1)[0][0]
    )


def __template2(x):
    if len(x[0]):
        return x[1], [user_setting["warning_template_2"] %
                      (i.date.strftime("%m-%d"), i.title) for i in x[0].order_by('date')]
    return x[1], user_setting['warning_template_3'] % (
        user_setting['warning_year'],
        '~'.join([str(i) for i in month])
    )


def __bar_data(data):
    if data is not None:
        m = '~'.join([str(i) for i in month])
        years = [i.year for i in date_range]
        fig = user_setting['warning_bar']
        fig['title']['text'] = user_setting['warning_bar_title'] % (
            m, years[0], years[1]
        )
        fig["xAxis"]["data"] = [i for i in data[1].keys()]
        fig["series"][0]["data"] = [i for i in data[1].values()]
        return fig


def __pie_data(data, title):
    if data is not None:
        fig = user_setting['warning_pie']
        fig['title']['text'] = title
        fig["series"][0]["data"] = [{'name': i, 'value': j} for i, j in data]
        return fig


def __add_legend(fig):
    fig['legend'] = {
        'orient': 'vertical',
        'x': 'right',
        'data': [i['name'] for i in fig["series"][0]["data"]]
    }
    return fig


def __warning_this(fig, title):
    new_name = [
        {
            "textStyle": {"color": "red"},
            "name": i,
        } for i in title]
    [
        fig['legend']['data'].insert(0, i) for i in new_name
    ]
    return fig


def get_date():
    global month, date_range
    today = date.today()

    date_range = (
        date(today.year - user_setting['warning_year'] + 1, today.month, 1),
        today + relativedelta(months=+1)
    )
    month = (today.month, date_range[1].month)
    return date_range, month


def summary_stats(qs1, qs2):
    prams = list(map(__common_tag_topic, qs1))
    res1 = map(__template1, zip(prams, user_setting["warning_title"][:3]))
    res2 = map(__template2, zip(qs2, user_setting['warning_title'][-2:]))
    chart2_title = user_setting['warning_pie_title'] % (
        '~'.join([str(i) for i in month]),
        date_range[0].year,
        date_range[1].year
    )
    topics = map(lambda x: x[-1].items() if x is not None else None, prams)

    chart1 = map(lambda x: [x[1], json.dumps(__bar_data(x[0]))], zip(prams, user_setting["warning_title"][:3]))
    chart2 = map(lambda x: [x[1], json.dumps(__pie_data(x[0], chart2_title))],
                 zip(topics, user_setting["warning_title"][:3]))

    return res1, res2, list(zip(chart1, chart2))


def questionnaire_pie(population, qs, n):
    option_set = map(lambda x: (x.title, x.num), qs)
    question = qs[0].question.title
    pie = __add_legend(__pie_data(option_set, 'Q%d: %s' % (n + 1, question)))
    prefix = []
    warning_state = list(filter(lambda x: x.num / population > x.value, qs.exclude(value__isnull=True)))
    if len(warning_state):
        prefix = '(超出预警值！%.1f%%/%.1f%%)'
        pie = __warning_this(pie, (i.title for i in warning_state))
        prefix = map(lambda x: prefix % (x.num / population * 100, x.value * 100), warning_state)
    return json.dumps(pie), prefix
