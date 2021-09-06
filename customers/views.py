from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import UserContacts
from .serializers import UserContactsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegForm


class UserContactsViewSet(ModelViewSet):
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['first_name', 'phone']


def first_page(request):

    return render(request, './first_page.html')


def reg_page(request):
    form = RegForm()
    return render(request, './registration.html', {'form': form})


def reg(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # if user is None:
        if request.user.is_authenticated:
            login(request, user)
            return render(request, './contacts_list.html')
        else:
            return render(request, './error.html')
    return render(request, './contacts_list.html')

    # if request.user.is_authenticated:
    #     return render(request, './contacts_list.html')
    # else:
    #     return render(request, './registration.html')


