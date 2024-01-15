# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)  # Set write_only=True to exclude user from response

    class Meta:
        model = UserProfile
        fields = ['user', 'mobile_number', 'birthday', 'profile_picture', 'bio']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile
