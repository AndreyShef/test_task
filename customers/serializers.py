from rest_framework import serializers
from .models import UserContacts

class UserContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContacts
        fields = ('first_name', 'last_name', 'phone')