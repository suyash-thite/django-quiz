from rest_framework.views import APIView
from rest_framework.response import Response

from models import Question, Category, Options
from helpers import generateresponse
from serializers import QuestionSerializer,CategorySerializer,OptionSerializer
from django_quiz.common_utils.exceptions import InvalidInformation,ObjectDoesNotExist


class QuestionList(APIView):
    """
    List all Questions, or create a new Questions.
    """

    def get(self, request):
        response = ''
        try:
            questions = Question.objects.all()
        except:
            raise ObjectDoesNotExist('Question does not exist')
        try:
            serializer = QuestionSerializer(questions, many=True)
            response = generateresponse('Success', 'Questions', serializer.data)
        except Exception as e:
            print e
        return Response(response)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = generateresponse('Success','Question',serializer.data)
            return Response(response)
        else:
            raise InvalidInformation(serializer.errors)


class QuestionDetail(APIView):
    """
    API to get deatils of questions
    """
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except:
            raise ObjectDoesNotExist('Question does not exist')

    def get(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionSerializer(question)
        response = generateresponse('Success', 'question', serializer.data)
        return Response(response)


class CategoryList(APIView):
    """
    List of all categories or create new category
    """

    def get(self,request):

        try:
            categories = Category.objects.all()
        except:
            raise ObjectDoesNotExist('Categories do not exist')

        serializer = CategorySerializer(categories,many=True)
        response = generateresponse('Success','Categories',serializer.data)
        return Response(response)

    def post(self,request):
        data = request.data
        serializer = CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = generateresponse('Success','Category',serializer.data)
            return Response(response)
        else:
            raise InvalidInformation(serializer.errors)

class OptionList(APIView):
    """
    Lists options for a particular question
    """

    def get(self,request):
        question_id = request.query_params['question_id']
        try:
            question = Question.objects.get(id = question_id)
        except:
            raise ObjectDoesNotExist('Question does not exist')
        try:
            options = Options.objects.get(question = question)
        except:
            raise ObjectDoesNotExist('Options does not exist')
        serializer = OptionSerializer(options)
        response = generateresponse('Success','Options',serializer.data)
        return Response(response)



