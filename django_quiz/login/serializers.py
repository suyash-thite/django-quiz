__author__ = 'aniruddha'

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User object from django.contrib.auth.models
    """

    class Meta:
        model = User
        fields = '__all__'
        depth = 1