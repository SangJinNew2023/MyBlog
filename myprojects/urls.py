"""myprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include, re_path
from myboard.views import base_views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", base_views.index),
    path("myboard/", include('myboard.urls')),
    path("myboard_users/", include('myboard_users.urls')),
    path("myblog/", include('myblog.urls')),
    path("myblog_users/", include('myblog_users.urls')),
    path('myinventory/', include('myinventory.urls')),
    path('myinventory_users/', include('myinventory_users.urls')),
]

handler404 = 'myboard_users.views.page_not_found'

urlpatterns += re_path(r'^media/(?P<path>.\*)$', serve, {'document_root': settings.MEDIA_ROOT,})

# You should not do this in production, so the if settings.DEBUG check is added.
# In production, you should configure your server (e.g. Nginx or Apache)
# to serve the media and static files, or serve them from a CDN.