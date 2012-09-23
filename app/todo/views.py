from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.template import defaultfilters
from django.utils import simplejson
from django.views.generic.detail import BaseDetailView, \
    SingleObjectTemplateResponseMixins

@csrf_protect
def index(request):
    if not request.POST:
      playlist = Playlist.objects.get(pk=1)
      tracks = playlist.track_set.all().order_by('-rank').reverse()
      youtube_ids = [track.youtube_id for track in tracks]
      json_youtube_ids = simplejson.dumps(youtube_ids)
      return render(request, 'todo.html', 
                              {'tracks': json_youtube_ids,
                               'artists_with_tracks': tracks})
    else:
      
      playlist = Playlist.objects.get(name=request.POST['name'])
      tracks = playlist.track_set.all()
      youtube_ids = [track.youtube_id for track in tracks]
      json_youtube_ids = simplejson.dumps(youtube_ids)
      return HttpResponse({'tracks': json_youtube_ids,
                           'artists_with_tracks': tracks}, 
                            mimetype="application/javascript")  

# class JSONResponseMixin(object):
#   def render_to_response(self, context):
#     return self.get_json_response(self.convert_contect_to_json(context))
#   def get_json_response(self, contennt, **httprespone_kwargs):
#     return HttpResonse(content, content_type='application/json', **httpresponse)
#   def convert_context_to_json(self, context):
#     return simplejson.dumps(context)

# class HybridDetailView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView)
#   def render_to_response(self, context):
#     if self.request.is_ajax():
#       obj = context['object'].as_dict()
#       return JSONResponseMixin.render_to_response(self,obj)
#     else:
#       return SingleObjectTemplateResponseMixin.render_to_response(self, context)



        

#         