from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class User(models.Model):
    pass
