from django.conf.urls import url

from .views import file_download

urlpatterns = [
    url(r'^file_download\/(?P<path>.*)$', file_download),

]