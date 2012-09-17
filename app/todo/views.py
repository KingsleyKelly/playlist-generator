from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.template import defaultfilters
from django.utils import simplejson

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
      try:
        playlist = Playlist.objects.get(name=request.POST['data'])
      tracks = playlist.track_set.all()
      youtube_ids = [track.youtube_id for track in tracks]
      json_youtube_ids = simplejson.dumps(youtube_ids)
      return HttpResponse({'tracks': json_youtube_ids,
                           'artists_with_tracks': tracks}, 
                            mimetype="application/javascript")      


        

        