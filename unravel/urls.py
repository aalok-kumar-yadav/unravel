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
from index.views import home, search_video, watch_video
from project.views import project
from playlist.views import playlist

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^watch', watch_video, name ='watch_video'),
    url(r'^search$', search_video, name='search_video'),
    url(r'^playlist$', playlist, name='playlist'),
    url(r'^project$', project, name='project'),
    url(r'^admin/', admin.site.urls),
]
