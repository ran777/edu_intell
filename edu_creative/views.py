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
    q = Posts.objects.filter(post_category__name="筹划设计").order_by('-click_num')
    q = list(zip(q, (i.uploadfile_set.all()[0].file for i in q)))

    context = {'q': __page_it(q, request.GET.get('page'))}
    return render(request, 'creative/design.html', context)


def templates(request):
    q = Posts.objects.filter(post_category__name="模版创意").order_by('-click_num')
    q = list(zip(q, (i.uploadfile_set.all()[0].file for i in q)))

    context = {'q': __page_it(q, request.GET.get('page'))}

    return render(request, 'creative/template_creative.html', context)


def method(request):
    q = Posts.objects.filter(post_category__name="方法形式").order_by('-click_num')
    # q = list(zip(q, (i.uploadfile_set.all()[0].file for i in q)))
    attachment = [i.uploadfile_set.all() for i in q]
    img = (i.filter(type='i') for i in attachment)
    files = (i.filter(type='f') for i in attachment)
    videos = (i.filter(type='v') for i in attachment)
    q = list(zip(q, img, files, videos))
    context = {'q': __page_it(q, request.GET.get('page'))}

    return render(request, 'creative/method_form.html', context)

def course_ware(request):
    q = Posts.objects.filter(post_category__name="课件样式").order_by('-click_num')
    attachment = [i.uploadfile_set.all() for i in q]
    img = (i.filter(type='i')[0] for i in attachment)
    files = (i.filter(type='f')[0] for i in attachment)
    q = list(zip(q, img, files))
    context = {'q': __page_it(q, request.GET.get('page'))}

    return render(request, 'creative/course_ware.html', context)


def post_detail(request):
    q_type = request.GET.get('type')
    if q_type is None:
        return
    context = {"q_type": q_type}

    if q_type == 'c':   # 课件详情
        post = Posts.objects.get(pk=int(request.GET.get('pid')))
        post.click_num += 1
        post.save()
        context['post'] = post
        context['file'] = UploadFile.objects.get(pk=int(request.GET.get('fid')))
        context['img'] = UploadFile.objects.get(pk=int(request.GET.get('iid')))

    if q_type == 'm':   # 方法形式详情
        post = Posts.objects.get(pk=int(request.GET.get('pid')))
        post.click_num += 1
        post.save()
        context['post'] = post
        context['file'] = UploadFile.objects.get(pk=int(request.GET.get('fid')))

    if q_type == 't':   # 表格详情
        post = Posts.objects.get(pk=int(request.GET.get('pid')))
        post.click_num += 1
        post.save()
        context['post'] = post

    return render(request, 'creative/post_detail.html', context)
