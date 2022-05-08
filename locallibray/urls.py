"""locallibray URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('login', include('django.contrib.auth.urls')),
    path('logout', include('django.contrib.auth.urls')),
    path('password_change', include('django.contrib.auth.urls')),
    path('password_change_done', include('django.contrib.auth.urls')),
    path('password_reset', include('django.contrib.auth.urls')),
    path('password_reset_done', include('django.contrib.auth.urls')),
    path('password_reset_confirm', include('django.contrib.auth.urls')),
    path('password_reset_complete', include('django.contrib.auth.urls')),
]