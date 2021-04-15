from django.db import models

# Create your models here.

class MyDemo(models.Model):
    name = models.TextField(default = "")
