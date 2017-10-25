import os
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings


# Create your views here.

document_root=settings.MEDIA_ROOT

def file_download(request, file_name):

	# file_name = request.GET['file_name']
	if file_name is not None:

	    the_file_name = file_name.split('/')[-1]
	    print(path.join(document_root, file_name))
	    
	    response = FileResponse(open(path.join(document_root, file_name)))
	    # response['Content-Type'] = 'application/octet-stream'
	    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

	return response
# def download(request, path):
#     path, name = os.path.split(path)
 
#     url = '/media/{0}?renameto={1}'.format(path,)
     
#     # add uid to the filename if the requesting user is authenticated
#     if request.user.is_authenticated():
#         url += '_u{0}'.format(request.user.id)
#     url += ext
 
#     response = HttpResponse()
#     response['X-Accel-Redirect'] = url
#     return response