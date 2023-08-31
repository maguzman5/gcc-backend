"""
URL configuration for gcc_historic_data project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from gcc_historic_data_db import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('q1/', views.query_q1, name='q1'),
    path('get_q1/', views.get_q1, name='get_q1'),
    path('q2/', views.query_q2, name='q2'),
    path('get_q2/', views.get_q2, name='get_q2')
]
