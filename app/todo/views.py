from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.template import defaultfilters
from django.utils import simplejson

@csrf_protect
def index(request):
    youtube_ids = [track.youtube_id for track in Track.objects.all()]
    full_tracks = Track.objects.all()
    print track_names
    artists_with_track_names = zip(artists, track_names)
    print artists_with_track_names
    json_artists_with_tracks = simplejson.dumps(full_tracks) 
    json_youtube_ids = simplejson.dumps(youtube_ids)
    return render(request, 'todo.html', 
                            {'tracks': json_youtube_ids,
                             'artists_with_tracks': json_artists_with_tracks})


        

        