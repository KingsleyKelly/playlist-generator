from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.template import defaultfilters
from django.utils import simplejson

@csrf_protect
def index(request):
    if not request.is_ajax():
      playlist = Playlist.objects.get(pk=1)
      tracks = playlist.track_set.all()
      youtube_ids = [track.youtube_id for track in tracks]
      tracks = simplejson.dumps(tracks)
      json_youtube_ids = simplejson.dumps(youtube_ids)
      return render(request, 'todo.html', 
                              {'tracks': json_youtube_ids,
                               'artists_with_tracks': tracks})
    else:
      playlist = Playlist.objects.get(name=request.POST['name'])
      tracks = playlist.track_set.all()
      youtube_ids = [track.youtube_id for track in tracks]
      json_youtube_ids = simplejson.dumps(youtube_ids)
      return HttpResponse(request, {'tracks': json_youtube_ids,
                              'artists_with_tracks': tracks})      


        

        