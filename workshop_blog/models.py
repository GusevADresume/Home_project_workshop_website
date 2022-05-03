from django.db import models



class Article(models.Model):
    text = models.TextField(max_length=1000)
    datetime = models.DateField(auto_now_add=True)

    @classmethod
    def create(cls, text):
        art = cls(text=text)
        return art



class ArticlePhoto(models.Model):
    img = models.ImageField(null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='photos')

    @classmethod
    def create(cls, img,article):
        photos = cls( img=img,article=article)
        return photos

class Vk_data(models.Model):
    writer_work = models.BooleanField()
    vk_group_id = models.IntegerField(null=True)
    vk_app_token = models.CharField(max_length=100,null=True)
    vk_group_token = models.CharField(max_length=100, null=True)
