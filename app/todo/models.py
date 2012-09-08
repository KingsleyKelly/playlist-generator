from django.db import models


class Playlist(models.Model):
  name = models.CharField(max_length=200)

class Track(models.Model):
  rank = models.IntegerField()
  youtube_id = models.CharField(max_length=200)
  artist_name = models.CharField(max_length=200)
  track_name = models.CharField(max_length=200)

