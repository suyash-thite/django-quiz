from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate,login

from .serializers import UserSerializer
from qna.helpers import generateresponse
from django_quiz.exceptions import InvalidCredentials


class LoginView(APIView):
    """
    API to login user
    """
    def post(self,request):
        data = request.data
        uname = data['username']
        passwd = data['password']
        user = authenticate(username=uname,password=passwd)
        if user is not None:
            login(request,user)
            serialized = UserSerializer(user)
            response = generateresponse('Success', 'User', serialized.data)
            return Response(response)
        else:
            raise InvalidCredentials("Username or password incorrect")




