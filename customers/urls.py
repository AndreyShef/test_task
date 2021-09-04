from rest_framework import permissions, routers
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nava2007@yandex.ru"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

router = routers.DefaultRouter()
router.register('contacts', views.UserContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts', views.UserContactsViewSet),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger(.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]