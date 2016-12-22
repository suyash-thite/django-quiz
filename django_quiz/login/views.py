from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from .serializers import UserSerializer
from qna.helpers import generateresponse
from django_quiz.exceptions import InvalidCredentials,InvalidInformation


class LoginView(APIView):
    """
    API to login user
    """
    def post(self,request):
        data = request.data
        uname = data['username']
        passwd = data['password']
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            serialized = UserSerializer(user)
            response = generateresponse('Success', 'User', serialized.data)
            return Response(response)
        else:
            raise InvalidCredentials("Username or password incorrect")



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