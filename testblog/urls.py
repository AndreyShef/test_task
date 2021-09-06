"""testblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from customers import views
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('', include('customers.urls')),
    path('first_page/', views.first_page, name='index'),
    path('registration/', views.reg_page, name='registry'),
    path('contacts_list/', views.reg, name='contacts'),
    path('error/', views.reg, name='error'),

    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls
