from django.conf.urls import url

from .views import plan_design, post_detail

urlpatterns = [
    url(r'^$', plan_design, name='design'),
    url(r'^detail/$', post_detail, name='detail'),
    # url(r'^questionnaire_list/$', questionnaire_warning, name='questionnaire_list'),
    # url(r'^questionnaire/(?P<q_id>[0-9]+)/$', questionnaire_detail, name='questionnaire_detail'),
    # url(r'^questionnaire/(?P<q_id>[0-9]+)/result/$', questionnaire_result, name='questionnaire_result'),

]