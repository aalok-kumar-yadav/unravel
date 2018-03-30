"""unravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from index.views import home, search_video, watch_video, about_us
from project.views import project
from playlist.views import playlist
from login.views import sin_up, log_in

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^watch', watch_video, name ='watch_video'),
    url(r'^search$', search_video, name='search_video'),
    url(r'^playlist$', playlist, name='playlist'),
    url(r'^project$', project, name='project'),
    url(r'^sinup$', sin_up, name='sin_up'),
    url(r'^login$', log_in, name='log_in'),
    url(r'^aboutus$' ,about_us, name="about_us"),
    url(r'^admin/', admin.site.urls),
]
