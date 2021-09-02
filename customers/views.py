from rest_framework import viewsets
from .serializers import UserContactsSerializer
from .models import UserContacts
from django_filters.rest_framework import DjangoFilterBackend
from .service import UserContactsFilter

class UserContactsViewSet(viewsets.ModelViewSet):
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserContactsFilter
