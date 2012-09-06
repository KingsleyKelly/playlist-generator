from django.db import models

class Track(models.Model):
    youtube_id = models.CharField(max_length=200)
    