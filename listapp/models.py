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
    g2a_link = models.CharField(max_length=200, default='')

class Humble(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    humble_link = models.CharField(max_length=200)
    discount = models.CharField(max_length=5)
    price = models.CharField(max_length=15)

class HumbleG2a(models.Model):
    name = models.ForeignKey(Humble, on_delete=models.CASCADE)
    price = models.CharField(max_length=20, default="0")
    g2a_link = models.CharField(max_length=200, default='')
    margin_num = models.DecimalField(max_digits=20, decimal_places=2, default="-100.00")
    margin_percent = models.DecimalField(max_digits=5, decimal_places=2, default="-100.00")

class Feedback(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    feedback = models.CharField(max_length=500, default="n/a")