import os
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from django.db.models import F
from .models import UploadFile
from posts.models import Posts

# Create your views here.

document_root = settings.MEDIA_ROOT


def file_download(request, path):
    file_name = path
    pid = request.GET['pid']
    if file_name is not None:
        the_file_name = file_name.split('/')[-1]


        response = FileResponse(open(os.path.join(document_root, file_name), 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
        # try:
        q = Posts.objects.get(pk=int(pid))
        q.download_num += 1
        q.save()
        # except:
        #     pass
        return response
