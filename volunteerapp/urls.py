from django.conf.urls import url
from . import views

app_name = "volunteerapp"

urlpatterns = [
    url(r'^', views.Index, name="index"),
    url(r'^projects/$', views.Index, name="project-add"),

]
