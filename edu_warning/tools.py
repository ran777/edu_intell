from datetime import date
from dateutil.relativedelta import relativedelta
from collections import Counter
import json
from django.db.models import Q

month = ''
date_range = []

with open('user_setting.json', 'r', encoding="utf8") as f:
    user_setting = json.load(f)


def __common_tag_topic(q):
    tag_counter = Counter(sum((i.list_tags() for i in q), []))
    topic_counter = Counter(sum((i.list_edu_category() for i in q), []))
    if len(tag_counter):
        problems = list(tag_counter.most_common(user_setting['warning']['num']))
        return problems, tag_counter, topic_counter

    return None


def __template1(x):
    if x[0] is None:
        return x[1], user_setting['warning']['template_3'] % (
            user_setting['warning']['year'],
            '~'.join([str(i) for i in month])
        ), False
    return (
        x[1],
        user_setting['warning']['template_1'] % (user_setting['warning']['year'], '~'.join([str(i) for i in month])),
        True,
        x[0][0],
        x[0][1].most_common(1)[0][0], x[0][2].most_common(1)[0][0]
    )
    

def __template2(x):
    if len(x[0]):
        return x[1], [user_setting['warning']['template_2'] %
                      (i.date.strftime("%m-%d"), i.title) for i in x[0].order_by('date')]
    return x[1], user_setting['warning']['template_3'] % (
        user_setting['warning']['year'],
        '~'.join([str(i) for i in month])
    )


def __bar_data(data):
    if data is not None:
        m = '~'.join([str(i) for i in month])
        years = [i.year for i in date_range]
        fig = user_setting['warning']['bar']
        fig['title']['text'] = user_setting['warning']['bar_title'] % (
            m, years[0], years[1]
        )
        fig["xAxis"]["data"] = [i for i in data[1].keys()]
        fig["series"][0]["data"] = [i for i in data[1].values()]
        return fig


def __pie_data(data, title):
    if data is not None:
        fig = user_setting['warning']['pie']
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


def __get_date():
    global month, date_range
    today = date.today()

    date_range = (
        date(today.year - user_setting['warning']['year'] + 1, today.month, 1),
        today + relativedelta(months=+1)
    )
    month = (today.month, date_range[1].month)
    return date_range, month


def basic_history_info():
    __get_date()
    q_m = (Q(date__month=month[0]) | Q(date__month=month[1]))
    q_y = Q(date__range=date_range)
    summary_category = (
        '教育计划预警',
        '倾向性问题预警',
        '一人一事思想工作预警',
        '重大节日庆典预警',
        '敏感时节预警',
    )

    return q_m, q_y, summary_category


def summary_stats(qs1, qs2):
    prams = list(map(__common_tag_topic, qs1))
    res1 = map(__template1, zip(prams, user_setting['warning']['title'][:3]))
    res2 = map(__template2, zip(qs2, user_setting['warning']['title'][-2:]))
    chart2_title = user_setting['warning']['pie_title'] % (
        '~'.join([str(i) for i in month]),
        date_range[0].year,
        date_range[1].year
    )
    topics = map(lambda x: x[-1].items() if x is not None else None, prams)

    chart1 = map(lambda x: [x[1], json.dumps(__bar_data(x[0]))], zip(prams, user_setting['warning']['title'][:3]))
    chart2 = map(lambda x: [x[1], json.dumps(__pie_data(x[0], chart2_title))],
                 zip(topics, user_setting['warning']['title'][:3]))

    return res1, res2, list(zip(chart1, chart2))


def questionnaire_pie(qs):
    option_set = map(lambda x: (x.title, x.num), qs)
    pie = __pie_data(option_set, '')
    return json.dumps(pie)


def option_warning(population, qs):
    title = [['%s (%.2f%%)' % (i.title, i.num/population * 100), 0] for i in qs]
    for i, q in enumerate(qs):
        if q.value is not None and q.num/population > q.value:

            title[i][0] += " 超出预警值%.2f%%!" % (q.value*100)
            title[i][1] = 1
    return title
