from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import UserContacts
from .serializers import UserContactsSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserContactsViewSet(ModelViewSet):
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['first_name', 'phone']


def reg(request):
    return render(request, './registration.html')


