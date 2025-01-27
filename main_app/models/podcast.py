from django.db import models


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    audio_url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, blank=True)
    duration = models.IntegerField(null=True)
    episode_number = models.IntegerField()
    episode_type = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title