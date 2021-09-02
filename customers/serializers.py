from rest_framework import serializers
from .models import UserContacts

class UserContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContacts
        fields = ('phone', 'first_name')