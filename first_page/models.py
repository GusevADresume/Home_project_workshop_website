from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)
    img = models.ImageField()
