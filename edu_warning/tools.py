from datetime import date
from dateutil.relativedelta import relativedelta
from collections import Counter
import json

month = ''

with open('user_setting.json', 'r', encoding="utf8") as f:
    user_setting = json.load(f)


def get_date():
    global month
    today = date.today()

    date_range = (
        date(today.year-user_setting['warning_year']+1, today.month, 1),
        today+relativedelta(months=+1)
    )
    month = (today.month, date_range[1].month)

    return date_range, month


def summary_stats(qs1, qs2):
    res1 = []
    res2 = []
    y = user_setting['warning_year']
    m = '~'.join([str(m) for m in month])
    for q, title in zip(qs1, user_setting["warning_title"][:3]):
        tags = sum((i.list_tags() for i in q), [])
        topics = sum((i.list_edu_category() for i in q), [])
        if len(tags):
            tag_counter = Counter(tags)
            problems = ', '.join(str(v)+'起'+k for (k, v) in tag_counter.most_common(user_setting['warning_num']))
            i_problem = tag_counter.most_common(1)[0][0]
            i_topic = Counter(topics).most_common(1)[0][0]
            res1.append((title, user_setting['warning_template_1'] % (y, m, problems, i_problem, i_topic)))
        else:
            res1.append((title, user_setting['warning_template_3'] % (y, m)))

    for q, title in zip(qs2, user_setting["warning_title"][-2:]):
        if len(q):
            res2.append((title, [user_setting["warning_template_2"] % (i.date.strftime("%m-%d"), i.title) for i in q.order_by('date')]))
        else:
            res1.append((title, user_setting['warning_template_3'] % (y, m)))
    return res1, res2
