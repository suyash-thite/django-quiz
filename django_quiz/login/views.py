from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

import requests
import json

from .serializers import UserSerializer
from qna.helpers import generateresponse
from django_quiz.exceptions import InvalidCredentials,InvalidInformation


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
            raise InvalidInformation('Post data sent is not valid. Please Check!')
        my_data = json.dumps(data)
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post('http://localhost:8000/api-token-auth/', my_data, headers=headers)
            token = json.loads(response.content)['token']
            token_obj = Token.objects.get(key=token)
            user_obj = token_obj.user
        except:
            raise InvalidCredentials('Incorrect Username or password')
        serializer = UserSerializer(user_obj)
        resp_data = serializer.data
        resp_data['token'] = token
        response = generateresponse('Success','User',resp_data)
        return Response(response)


class RegisterView(APIView):
    """
    API to register new Users
    """
    def post(self,request):
        data = request.data
        uname = data['username']
        passwd = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        try:
            user = User.objects.create_user(username=uname, password=passwd,email=email,
                                            first_name=first_name, last_name=last_name)
            serialized = UserSerializer(user)
            response = generateresponse('Success','User',serialized.data)
            return Response(response)
        except:
            raise InvalidInformation("The information entered is invalid or incorrect")