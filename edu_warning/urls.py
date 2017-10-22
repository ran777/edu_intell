from django.conf.urls import url

from .views import history_warning, history_detail, questionnaire_warning, questionnaire_detail, questionnaire_result

urlpatterns = [
    url(r'^$', history_warning, name='history'),
    url(r'^detail/$', history_detail, name='detail'),
    url(r'^questionnaire_list/$', questionnaire_warning, name='questionnaire_list'),
    url(r'^questionnaire/(?P<q_id>[0-9]+)/$', questionnaire_detail, name='questionnaire_detail'),
    url(r'^questionnaire/(?P<q_id>[0-9]+)/result/$', questionnaire_result, name='questionnaire_result'),

]