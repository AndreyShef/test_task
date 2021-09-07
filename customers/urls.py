from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views


router = routers.DefaultRouter()
router.register(r'contacts', views.UserContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts', views.UserContactsViewSet),
    path('addcontact', views.add_contact),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

]