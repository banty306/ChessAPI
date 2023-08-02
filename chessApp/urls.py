"""chessApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from chessApp.health_check_view import health_check_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck/', health_check_api, name='knockknock'),
    re_path(r'^$', health_check_api),
    re_path(r'healthcheck/^$', health_check_api),
    path('api/v1/chess/', include('chess.urls'))
]
