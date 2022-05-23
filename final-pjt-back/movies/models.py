from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)

class Vote(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rate = models.IntegerField()
    content = models.TextField()