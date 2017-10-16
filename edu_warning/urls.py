from django.conf.urls import url

from .views import history_warning, questionnaire_warning

urlpatterns = [
    url(r'^$', history_warning, name='history'),
    url(r'^questionnaire/$', questionnaire_warning, name='questionnaire_list'),

]