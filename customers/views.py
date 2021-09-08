from django.contrib.sites import requests
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
    # permission_classes = [IsAuthenticated]
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

######### CRUD ##########

@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_contact(request):
    """Добавление контакта через API"""
    payload = json.loads(request.body)
    contact = UserContacts.objects.create(
        first_name=payload['first_name'],
        last_name=payload['last_name'],
        phone=payload['phone']
    )
    serializer = UserContactsSerializer(contact)
    return JsonResponse({'contacts': serializer.data}, safe=False, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_contact(request, usercontacts_id):
    """Изменение контакта через API по id"""
    # user = request.user.id
    payload = json.loads(request.body)
    # book_item = Book.objects.filter(added_by=user, id=contacts_id)
    contact_item = UserContacts.objects.filter(id=usercontacts_id)
    # returns 1 or 0
    contact_item.update(**payload)
    contact = UserContacts.objects.get(id=usercontacts_id)
    serializer = UserContactsSerializer(contact)
    return JsonResponse({'contacts': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_contact(request, usercontacts_id):
    """Удаление контакта"""
    user = request.user.id
    # book = UserContacts.objects.get(added_by=user, id=usercontacts_id)
    contact = UserContacts.objects.get(id=usercontacts_id)
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


