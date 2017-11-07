from django.db import models
from django.contrib.auth.models import User


class ProjectCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)

class UserProfile(models.Model):
    user = models.OneToOneField(User,
                         on_delete=models.CASCADE,
                         related_name="profile",
                         related_query_name="profile",)
    karma = models.DecimalField(max_digits=10,decimal_places=2)
#    default_tags = models.ManyToManyField(Tag, related_name="+")

    def __str__(self):
        return self.user.username + "'s profile"

    def cacheKarma(self):
        pass
