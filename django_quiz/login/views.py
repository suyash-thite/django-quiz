import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

import requests
from datetime import datetime

from .serializers import UserSerializer,ProfileSerializer
from qna.helpers import generateresponse
from .models import Profile

from django_quiz.common_utils.exceptions import AuthenticationFailure,InvalidInformation,ObjectDoesNotExist
from django_quiz.common_utils.security import login_required


class LoginView(APIView):
    """
    API to login user
    """
    def post(self,request):
        data = request.data
        try:
            uname = data['username']
            passwd = data['password']
        except:
            raise InvalidInformation('Username or Password not present')
        my_data = json.dumps(data)
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post('http://localhost:8000/api-token-auth/', my_data, headers=headers)
            token = json.loads(response.content)['token']
            token_obj = Token.objects.get(key=token)
            token_obj.created = datetime.utcnow()
            token_obj.save()
            user_obj = token_obj.user
        except:
            raise AuthenticationFailure('Incorrect Username or password')
        serializer = UserSerializer(user_obj)
        resp_data = serializer.data
        resp_data['token'] = token
        response = generateresponse('Success','User',resp_data)
        return Response(response)

class LogoutView(APIView):
    """
    API to logout user
    """
    @login_required
    def get(self,request):
        token = request.auth
        token.delete()
        response = generateresponse('Success','token','null')
        return Response(response)

class UserInfo(APIView):
    """
    Get User Information from token
    """

    @login_required
    def get(self,request):
        user_obj = request.auth.user
        serializer = UserSerializer(user_obj)
        response = generateresponse('Success','User',serializer.data)
        return Response(response)

class RegisterView(APIView):
    """
    API to register new Users
    """
    def post(self,request):
        data = request.data
        try:
            uname = data['username']
            passwd = data['password']
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            new_user = User.objects.create_user(username=uname, password=passwd,email=email,
                                            first_name=first_name, last_name=last_name)
        except:
            raise InvalidInformation("The information entered is invalid or incorrect")
        serializer = UserSerializer(new_user)
        try:
            token = Token.objects.get(user=new_user)
            resp_data = serializer.data
            resp_data['token'] = token.key
        except:
            raise ObjectDoesNotExist('Token for the user not created.')
        response = generateresponse('Success','User',resp_data)
        return Response(response)

class Authenticate(APIView):

    """
    Authenticate the user
    """

    def get(self,request):
        token = request.auth
        if token is None:
            raise AuthenticationFailure('Unauthorised Access')
        else:
            response = {'token':token.key}
            return Response(response)


class ProfileDetails(APIView):
    """
    Get details about user profile
    """
    def get_object(self,user_id):
        try:
            user = User.objects.get(id=user_id)
            return Profile.objects.get(user=user)
        except:
            raise ObjectDoesNotExist('User/Profile does not exist')

    @login_required
    def get(self,request,profile_id):
        profile = self.get_object(profile_id)
        serializer = ProfileSerializer(profile)
        response = generateresponse('Success','profile',serializer.data)
        return Response(response)

class UpdateProfileDetails(APIView):
    """
    Update Profile
    """

    @login_required
    def patch(self,request):
        data = request.data
        try:
            user = request.user
        except:
            raise InvalidInformation('User is not present')
        serializer = ProfileSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
        else:
            raise InvalidInformation(serializer.errors)
        response = generateresponse('Success','profile',serializer.data)
        return Response(response)

