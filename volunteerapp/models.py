from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)


    
