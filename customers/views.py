from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserContactsSerializer
from .models import UserContacts


class UserContactsViewSet(viewsets.ModelViewSet):
    queryset = UserContacts.objects.all().order_by('first_name')
    serializer_class = UserContactsSerializer
