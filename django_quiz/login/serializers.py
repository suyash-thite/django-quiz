__author__ = 'aniruddha'

from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User object from django.contrib.auth.models
    """

    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile object from login.models
    """

    user = UserSerializer(read_only=True)

    user_id = serializers.SerializerMethodField()

    def get_user_id(self, User):
         return User.id

    class Meta:
        model = Profile
        fields = ('user', 'user_id', 'bio', 'total_score', 'profile_image')
        depth = 1

    def create(self, validated_data):
        pass

