from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    phone = PhoneNumberField (unique= False, null=False, blank=False)
    text = models.TextField(max_length=1000)
    consent = models.BooleanField(null=False)
    date = models.DateField(auto_now_add=True)


class AGREEMENT(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)

