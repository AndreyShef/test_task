from rest_framework import routers
from django.urls import path, include


from . import views


router = routers.DefaultRouter()
router.register('contacts', views.UserContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts', views.UserContactsViewSet),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

]