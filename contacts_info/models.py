from django.db import models


class Contacts_info(models.Model):
    title = models.CharField(max_length=50)
    addres = models.TextField(max_length=200)
    img = models.ImageField(null=True, blank=True)
    tg_token = models.CharField(max_length=50)


class Phone(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    info = models.ForeignKey(Contacts_info, on_delete=models.CASCADE, related_name='phone')
    tg_id = models.CharField(max_length=10, null=True)
