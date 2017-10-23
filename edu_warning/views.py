from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import HistoryWarning, Questionnaire, Question, Option
from uploadfiles.models import UploadFile


from .tools import summary_stats, user_setting, questionnaire_pie, option_warning, basic_history_info
# Create your views here.


def history_warning(request):
    q_m, q_y, summary_category = basic_history_info()
    q_list = HistoryWarning.objects.filter(q_m)
    q_data_range = q_list.filter(q_y)
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


def history_detail(request):
    q_type = request.GET.get('type')
    if q_type is None:
        return
    context = {"q_type": q_type}
    q_m, q_y, summary_category = basic_history_info()
    q_category = Q(post_category__name=summary_category[int(request.GET.get('category'))])
    keyword = request.GET.get('keyword')
    if q_type == 'p':   # 问题详情
        context['query'] = HistoryWarning.objects.filter(q_m & q_y & q_category & Q(tag__name=keyword)).order_by("date")
    if q_type == 'f':   # 节日详情
        q = HistoryWarning.objects.get(q_category & Q(title=keyword))
        context['title'] = q.title
        context['description'] = q.content
        context['query'] = UploadFile.objects.filter(festival=q.id)
    if q_type == 'ff':   # 方案详情
        context['file'] = UploadFile.objects.get(pk=int(request.GET.get('id')))

    return render(request, 'warning/warning_detail.html', context)


def questionnaire_warning(request):
    q = Questionnaire.objects.filter(status=True).order_by('start_date')
    # q = Questionnaire.objects.all().order_by('start_date')
    paginator = Paginator(q, user_setting['warning']['page_num'])

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
        option_id = list(map(lambda x: int(x[1]), option_id))
        q = Option.objects.filter(pk__in=option_id)
        q.update(num=F('num')+1)
        q = Questionnaire.objects.get(pk=q_id)
        q.population += 1
        q.save()

    title = Questionnaire.objects.get(pk=q_id)
    option_id = Question.objects.filter(questionnaire=q_id)
    q = [Option.objects.filter(question=i.id).order_by('id') for i in option_id]
    context = {
        "is_post": bool(request.method == 'POST'),
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
    q = [Option.objects.filter(question=i.id).order_by('id') for i in question]
    result = map(questionnaire_pie, q)
    options = map(option_warning, [population]*len(q), q)
    context = {
        "page_now": "问卷结果",
        'questionnaire': title,
        "stats": result,
        "options": zip(question, options),
    }

    return render(request, 'warning/questionnaire-result.html', context)
