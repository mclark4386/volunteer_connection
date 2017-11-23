from django.db import models
from django.contrib.auth.models import User, Group


class ProjectCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,
                         on_delete=models.CASCADE,
                         related_name="profile",
                         related_query_name="profile",)
    karma = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
    default_tags = models.ManyToManyField('volunteerapp.Tag', related_name="+", blank=True)

    def __str__(self):
        return self.user.username + "'s profile"

    def cacheKarma(self):
        pass


class Tag(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    color = models.CharField(max_length=25)
    projects = models.ManyToManyField('volunteerapp.Project', blank=True)

    def __str__(self):
        return self.name

class ProjectEmail(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey('volunteerapp.Project')
    fromEmail = models.CharField(max_length=500)
    toEmail = models.CharField(max_length=500)
    emailBCC = models.TextField()
    emailSubject = models.CharField(max_length=250)
    emailBody = models.TextField()

    def __str__(self):
        return self.project

class GoldStar(models.Model):
    awarder = models.ForeignKey(User,
                         on_delete=models.CASCADE,
                         related_name="awarded_gold_stars",
                         related_query_name="awarded_gold_stars",)
    receiver = models.ForeignKey(User,
                         on_delete=models.CASCADE,
                         related_name="my_gold_stars",
                         related_query_name="my_gold_stars",)
    reason = models.CharField(max_length=1000)


    def __str__(self):
        return self.receiver

class Location(models.Model):
    organization = models.ForeignKey(Group)
    name = models.CharField(max_length=500)
    descrip = models.TextField()
    gpsCoord = models.CharField(max_length=2500)
    address = models.CharField(max_length=500)
    hours = models.CharField(max_length=500)


    def __str__(self):
        return self.name

class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=140)
    category = models.ForeignKey('volunteerapp.ProjectCategory')
    organization = models.ForeignKey(Group)
    volunteers = models.ManyToManyField(User, blank=True, through='Participation')
    locations = models.ManyToManyField('volunteerapp.Location',
                                        related_name = "projects",
                                        related_query_name = "projects")
    description = models.TextField()
    tags = models.ManyToManyField('volunteerapp.Tag', blank=True)
    #TODO: implement times

    def __str__(self):
        return self.title

class Participation(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey('volunteerapp.Project')
    promised_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    actual_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
