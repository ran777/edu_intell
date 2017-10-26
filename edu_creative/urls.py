from django.conf.urls import url

from .views import index, design, post_detail, templates, method, course_ware

urlpatterns = [
    url(r'^$', index),
    url(r'^design/$', design, name='design'),
    url(r'^templates/$', templates, name='templates'),
    url(r'^method/$', method, name='method'),
    url(r'^courseware/$', course_ware, name='courseware'),
    url(r'^detail/$', post_detail, name='detail'),

]