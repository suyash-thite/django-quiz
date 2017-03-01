__author__ = 'aniruddha'
from rest_framework.views import APIView
from rest_framework.response import Response

from qna.models import Question, Category, Options, Answers
from qna.helpers import generateresponse
from qna.serializers import QuestionSerializer,CategorySerializer,OptionSerializer
from django_quiz.common_utils.exceptions import InvalidInformation,ObjectDoesNotExist
from django_quiz.common_utils.security import login_required

class CategoryQuiz(APIView):

    def get(self,request,category_id):
        try:
            questions = Question.objects.random(category_id)
            options = Options.objects.filter(question__in=questions)
        except Exception as e:
            raise ObjectDoesNotExist(e)
        serializer = OptionSerializer(options,many=True)
        response = generateresponse('Success','Quiz',serializer.data)
        return Response(response)

