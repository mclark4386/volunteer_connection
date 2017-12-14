from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "volunteerapp"

urlpatterns = [

    url(r'^$', views.Index, name="index"),
    url(r'^leaderboard[s]*$', views.Leaderboard, name="leaderboard"),
    url(r'^projects/$', views.Index, name="project-add"),
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.ProjectDetail, name="project_detail"),
    url(r'^signup/$', views.UserFormView.as_view(), name="signup"),
    url(r'^login$', auth_views.LoginView.as_view(
        template_name='volunteerapp/login.html'), name="login"),
    url(r'^logout$', auth_views.LogoutView.as_view(
        next_page='volunteerapp:index'), name="logout"),
    url(r'^password_reset$',
        auth_views.PasswordResetView.as_view(
            email_template_name="volunteerapp/password_reset_email.html"
        ), name="password_reset"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),
]
