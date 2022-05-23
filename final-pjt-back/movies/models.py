from django.db import models
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster_path = models.TextField(blank=True)
    overview = models.CharField(max_length=200)
    genre = models.IntegerField()

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='votes')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rate = models.IntegerField()
    content = models.TextField(blank=True)