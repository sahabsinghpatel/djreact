from django.db import models

class Varify(models.Model):
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=50, blank=True)
    password=models.CharField(max_length=30, blank=True)
    otp=models.IntegerField(blank=True)
