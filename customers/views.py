from django.contrib.sites import requests
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import json
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
        # if request.user.token:
        #     token = user.token
        #     response = requests.get('contacts', headers={"Authorization": "Token {}"})
        #     return response
        # if user.status_code == 200:
        # response = user.json()
        # token = response['token']
        # print(token)
        # if user is None:
        if request.user.is_authenticated:
            login(request, user)
            return render(request, './contacts_list.html')
        # else:
        #     return render(request, './error.html')
        return render(request, './contacts_list.html')

    # if request.user.is_authenticated:
    #     return render(request, './contacts_list.html')
    # else:
    #     return render(request, './registration.html')


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_contact(request):
    payload = json.loads(request.body)
    contact = UserContacts.objects.create(
        first_name=payload['first_name'],
        last_name=payload['last_name'],
        phone=payload['phone']
    )
    serializer = UserContactsSerializer(contact)
    return JsonResponse({'contacts': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
