from datetime import date
from dateutil.relativedelta import relativedelta
from collections import Counter
import json

month = ''

with open('user_setting.json', 'r', encoding="utf8") as f:
    user_setting = json.load(f)


def __common_tag_topic(q):
    tag_counter = Counter(sum((i.list_tags() for i in q), []))
    topic_counter = Counter(sum((i.list_edu_category() for i in q), []))
    if len(tag_counter):
        problems = ', '.join(str(v)+'起'+k for (k, v) in tag_counter.most_common(user_setting['warning_num']))
        return problems, tag_counter.most_common(1)[0][0], topic_counter.most_common(1)[0][0]

    return None


def __template1(x):
    if x[0] is None:
        return x[1], user_setting['warning_template_3'] % \
               (user_setting['warning_year'], '~'.join([str(i) for i in month]))
    return x[1], user_setting['warning_template_1'] % \
              (user_setting['warning_year'], '~'.join([str(i) for i in month]), x[0][0], x[0][1], x[0][2])


def __template2(x):
    if len(x[0]):
        return x[1], [user_setting["warning_template_2"] %
                      (i.date.strftime("%m-%d"), i.title) for i in x[0].order_by('date')]
    return x[1], user_setting['warning_template_3'] % \
           (user_setting['warning_year'], '~'.join([str(i) for i in month]))


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
    prams = map(__common_tag_topic, qs1)
    res1 = map(__template1, zip(prams, user_setting["warning_title"][:3]))
    res2 = map(__template2, zip(qs2, user_setting['warning_title'][-2:]))
    return res1, res2
