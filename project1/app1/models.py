from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    author = models.CharField(max_length=30)


class NewsData(models.Model):
    title = models.TextField()
    content = models.TextField()
    image_url = models.TextField()



