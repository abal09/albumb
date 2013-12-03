from django.shortcuts import render

# Create your views here.

from django.conf import settings
# Create your views here.
from django.shortcuts import render_to_response, RequestContext
from django.shortcuts import get_object_or_404
from multiuploader.forms import MultiUploadForm
from multiuploader.models import MultiuploaderFile

def my_view(request):
    context = {
        'uploadForm':MultiUploadForm()
    }
    return render_to_response('images.html',
                              locals(),
                              context_instance=RequestContext(request))
