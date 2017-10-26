from django.conf.urls import url

from .views import index, design, post_detail, templates, method

urlpatterns = [
    url(r'^$', index),
    url(r'^design/$', design, name='design'),
    url(r'^templates/$', templates, name='templates'),
    url(r'^method/$', method, name='method'),

    url(r'^detail/$', post_detail, name='detail'),
    # url(r'^questionnaire_list/$', questionnaire_warning, name='questionnaire_list'),
    # url(r'^questionnaire/(?P<q_id>[0-9]+)/$', questionnaire_detail, name='questionnaire_detail'),
    # url(r'^questionnaire/(?P<q_id>[0-9]+)/result/$', questionnaire_result, name='questionnaire_result'),

]