from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offers = models.BooleanField(default=False)


class Movies(models.Model):

    movie_name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='pics')
    movie_id = models.IntegerField()
    genres = models.CharField(max_length=100)
    description = models.TextField()

class Ratings(models.Model):

    movie_id = models.CharField(max_length=100)
    user_id = models.ImageField()
    ratings = models.ImageField()


class Trending(models.Model):

    movie_name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='pics')
    movie_id = models.IntegerField()
    genres = models.CharField(max_length=100)
    description = models.TextField()

class Top(models.Model):

    movie_name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='pics')
    movie_id = models.IntegerField()
    genres = models.CharField(max_length=100)
    description = models.TextField()