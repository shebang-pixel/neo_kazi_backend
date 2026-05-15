from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'phone_number', 'role', 'profile_pic', 'address', 
            'city', 'state', 'country', 'postal_code'
        ]
        read_only_fields = ['id']