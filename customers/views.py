from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserContactsSerializer
from .models import UserContacts


class UserContactsViewSet(viewsets.ModelViewSet):
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer
