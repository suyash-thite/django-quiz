__author__ = 'aniruddha'

from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers

from django_quiz.common_utils.exceptions import ObjectDoesNotExist


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


    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


    def update(self, instance, validated_data):
        if self.context.get('request').method == 'PATCH':
            try:
                profile = Profile.objects.get(user=instance)
                if 'bio' in validated_data:
                    profile.bio = validated_data['bio']
                    profile.save()
                    return profile
            except:
                raise ObjectDoesNotExist('Profile does not exist')
