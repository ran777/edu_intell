from django.conf.urls import url

from .views import history_warning, questionnaire_warning, questionnaire_detail

urlpatterns = [
    url(r'^$', history_warning, name='history'),
    url(r'^questionnaire_list/$', questionnaire_warning, name='questionnaire_list'),
    url(r'^questionnaire/(?P<q_id>[0-9]+)/$', questionnaire_detail, name='questionnaire_detail'),

]