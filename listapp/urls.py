from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views

urlpatterns= [
    url('^$', views.other_index, name='other_index'),
    url('login/$', login, {'template_name': 'listapp/login.html'}),
    url('home/$', views.home_index, name='home_index'),
    url('logout/$', views.logout_index, name="logout_index"),
    url('steamsales/$', views.steamsales_index, name='steamsales_index'),
    url('humblesales/$', views.humblesales_index, name='humblesales_index'),
    url('feedback/$', views.feedback_index, name='feedback_index'),
    url('thanks/$', views.thanks_index, name='thanks_index'),
    ]
