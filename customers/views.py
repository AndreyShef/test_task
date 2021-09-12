from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import UserContacts
from .serializers import UserContactsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login
from .forms import RegForm


class UserContactsViewSet(ModelViewSet):
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['first_name', 'phone']


# def first_page(request):
#     return render(request, './first_page.html')
#
#
# def reg_page(request):
#     form = RegForm()
#     return render(request, './registration.html', {'form': form})


def reg(request):
    return render(request, './contacts_list.html')


