from django.db import models

# Create your models here.


class Steam(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    steam_link = models.CharField(max_length=44)
    discount = models.CharField(max_length=5)
    price = models.CharField(max_length=10)
    rating = models.CharField(max_length=6)


class Steam_g2a(models.Model):
    name = models.ForeignKey(Steam, on_delete=models.CASCADE)
    price = models.CharField(max_length=10, default="0")
    g2a_link = models.CharField(max_length=100, default='')


