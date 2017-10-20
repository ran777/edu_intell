from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import HistoryWarning, Questionnaire, Question, Option


from .tools import get_date, summary_stats, user_setting, questionnaire_pie, option_warning
# Create your views here.


def history_warning(request):
    date_range, m = get_date()

    q_list = HistoryWarning.objects.filter(Q(date__month=m[0]) | Q(date__month=m[1]))
    q_data_range = q_list.filter(date__range=date_range)
    summary_category = (
        '教育计划预警',
        '倾向性问题预警',
        '一人一事思想工作预警',
        '重大节日庆典预警',
        '敏感时节预警',
    )
    qs1 = map(lambda x: q_data_range.filter(post_category__name=x), summary_category[:3])
    qs2 = map(lambda x: q_list.filter(post_category__name=x), summary_category[-2:])

    summary1, summary2, charts = summary_stats(qs1, qs2)
    context = {
        "page_now": "预警研判",
        "cards_with_figure": summary1,
        "cards": summary2,
        'charts': charts,

    }

    return render(request, 'warning/warning.html', context)


def questionnaire_warning(request):
    q = Questionnaire.objects.filter(status=True).order_by('start_date')
    paginator = Paginator(q, user_setting['warning_page_num'])

    page = request.GET.get('page')
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)

    context = {"q": q}

    return render(request, 'warning/questionnaire-list.html', context)


def questionnaire_detail(request, q_id):
    if request.method == 'POST':
        option_id = filter(lambda x: True if x[0].startswith('answer-') else False, request.POST.items())
        option_id = map(lambda x: int(x[1]), option_id)
        q = Option.objects.filter(pk__in=option_id)
        q.update(num=F('num')+1)
        q = Questionnaire.objects.get(pk=q_id)
        q.population += 1
        q.save()

        return render(request, 'warning/questionnaire-submit.html', {})
    else:
        title = Questionnaire.objects.get(pk=q_id)
        option_id = Question.objects.filter(questionnaire=q_id)
        q = [Option.objects.filter(question=i.id).order_by('order') for i in option_id]
        context = {
            "page_now": "调查问卷",
            'questionnaire': title,
            "q_id": q_id,
            "qs": zip(option_id, q)
        }

        return render(request, 'warning/questionnaire-detail.html', context)


def questionnaire_result(request, q_id):

    title = Questionnaire.objects.get(pk=q_id)
    question = Question.objects.filter(questionnaire=q_id)
    population = title.population
    q = [Option.objects.filter(question=i.id) for i in question]
    result = map(questionnaire_pie, q)
    options = map(option_warning, [population]*len(q), q)
    context = {
        "page_now": "问卷结果",
        'questionnaire': title,
        "stats": result,
        "options": zip(question, options),
    }

    return render(request, 'warning/questionnaire-result.html', context)
