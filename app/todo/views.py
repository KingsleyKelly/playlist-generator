# -*- coding: utf-8 -*-

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.template import defaultfilters

@csrf_protect
def index(request):
    tracks = [unicode(track.youtube_id) for track in Track.objects.all()]

    return render(request, 'todo.html', {'tracks': tracks})
        

        