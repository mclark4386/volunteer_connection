from django.db import models

# Create your models here.

Class Projects(models.Model):
    category = models.CharField(max_length = 45)
    organization = models.Foreignkey("")
