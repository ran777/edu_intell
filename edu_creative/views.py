from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Posts
from uploadfiles.models import UploadFile


from edu_warning.tools import user_setting
# Create your views here.

def __page_it(q, page):
    paginator = Paginator(q, user_setting['creative']['page_num'])
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)
    return q


def index(request):
    context = {"page_now": "创意设计"}
    return render(request, 'creative/base.html', context)

def design(request):
    q = Posts.objects.filter(post_category__name="筹划设计").order_by('click_num')
    q = list(zip(q, (i.uploadfile_set.all()[0].file for i in q)))

    context = {'q': __page_it(q, request.GET.get('page'))}
    return render(request, 'creative/design.html', context)


def templates(request):
    q = Posts.objects.filter(post_category__name="模版创意").order_by('click_num')
    q = list(zip(q, (i.uploadfile_set.all()[0].file for i in q)))

    context = {'q': __page_it(q, request.GET.get('page'))}

    return render(request, 'creative/template_creative.html', context)


def method(request):
    q = Posts.objects.filter(post_category__name="方法形式").order_by('click_num')
    # q = list(zip(q, (i.uploadfile_set.all()[0].file for i in q)))
    attachment = [i.uploadfile_set.all() for i in q]
    img = (i.filter(type='i') for i in attachment)
    files = (i.filter(type='f') for i in attachment)
    videos = (i.filter(type='v') for i in attachment)
    q = list(zip(q, img, files, videos))
    context = {'q': __page_it(q, request.GET.get('page'))}

    return render(request, 'creative/method_form.html', context)


def post_detail(request):
    q_type = request.GET.get('type')
    if q_type is None:
        return
    context = {"q_type": q_type}
    # q_m, q_y, summary_category = basic_history_info()
    # q_category = Q(post_category__name=summary_category[int(request.GET.get('category'))])
    # keyword = request.GET.get('keyword')
    # if q_type == 'p':   # 问题详情
    #     context['query'] = HistoryWarning.objects.filter(q_m & q_y & q_category & Q(tag__name=keyword)).order_by("date")
    if q_type == 'm':   # 方法形式详情
        post = Posts.objects.get(pk=int(request.GET.get('pid')))
        post.click_num += 1
        post.save()
        context['post'] = post
        file = UploadFile.objects.get(pk=int(request.GET.get('fid')))
        context['file'] = file

    if q_type == 't':   # 表格详情
        post = Posts.objects.get(pk=int(request.GET.get('pid')))
        post.click_num += 1
        post.save()
        context['post'] = post

    return render(request, 'creative/post_detail.html', context)


# def questionnaire_warning(request):
#     q = Questionnaire.objects.filter(status=True).order_by('start_date')
#     # q = Questionnaire.objects.all().order_by('start_date')
#     paginator = Paginator(q, user_setting['warning']['page_num'])

#     page = request.GET.get('page')
#     try:
#         q = paginator.page(page)
#     except PageNotAnInteger:
#         q = paginator.page(1)
#     except EmptyPage:
#         q = paginator.page(paginator.num_pages)

#     context = {"q": q}

#     return render(request, 'warning/questionnaire-list.html', context)


# def questionnaire_detail(request, q_id):
#     if request.method == 'POST':
#         option_id = filter(lambda x: True if x[0].startswith('answer-') else False, request.POST.items())
#         option_id = list(map(lambda x: int(x[1]), option_id))
#         q = Option.objects.filter(pk__in=option_id)
#         q.update(num=F('num')+1)
#         q = Questionnaire.objects.get(pk=q_id)
#         q.population += 1
#         q.save()

#     title = Questionnaire.objects.get(pk=q_id)
#     option_id = Question.objects.filter(questionnaire=q_id)
#     q = [Option.objects.filter(question=i.id).order_by('id') for i in option_id]
#     context = {
#         "is_post": bool(request.method == 'POST'),
#         "page_now": "调查问卷",
#         'questionnaire': title,
#         "q_id": q_id,
#         "qs": zip(option_id, q)
#     }

#     return render(request, 'warning/questionnaire-detail.html', context)


# def questionnaire_result(request, q_id):

#     title = Questionnaire.objects.get(pk=q_id)
#     question = Question.objects.filter(questionnaire=q_id)
#     population = title.population
#     q = [Option.objects.filter(question=i.id).order_by('id') for i in question]
#     result = map(questionnaire_pie, q)
#     options = map(option_warning, [population]*len(q), q)
#     context = {
#         "page_now": "问卷结果",
#         'questionnaire': title,
#         "stats": result,
#         "options": zip(question, options),
#     }

#     return render(request, 'warning/questionnaire-result.html', context)
