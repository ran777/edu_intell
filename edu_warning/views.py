from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import HistoryWarning, Questionnaire


from .tools import get_date, summary_stats, user_setting
# Create your views here.


def history_warning(request):
    date_range, m = get_date()

    q_list = HistoryWarning.objects.filter(Q(date__month=m[0]) | Q(date__month=m[1]))
    q_data_range = q_list.filter(date__range=date_range)

    qs1 = [
        q_data_range.filter(post_category__name="教育计划预警"),
        q_data_range.filter(post_category__name="倾向性问题"),
        q_data_range.filter(post_category__name="一人一事思想工作预警"),
    ]
    qs2 = [
        q_list.filter(post_category__name="重大节日庆典预警"),
        q_list.filter(post_category__name="敏感时节预警"),
    ]

    summary1, summary2 = summary_stats(qs1, qs2)

    context = {
        "page_now": "预警研判",
        "cards_with_figure": summary1,
        "cards": summary2,
    }

    return render(request, 'warning.html', context)


def questionnaire_warning(request):
    q = Questionnaire.objects.order_by('start_date')
    paginator = Paginator(q, user_setting['warning_page_num'])

    page = request.GET.get('page')
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)

    context = {"q": q}

    return render(request, 'warning_questionnaire.html', context)
