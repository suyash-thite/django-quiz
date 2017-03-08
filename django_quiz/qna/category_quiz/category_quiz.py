__author__ = 'aniruddha'
from rest_framework.views import APIView
from rest_framework.response import Response

from qna.models import Question, Category, Options, Answers
from qna.helpers import generateresponse,deleteEmptyOptions
from qna.serializers import QuestionSerializer,CategorySerializer,OptionSerializer
from django_quiz.common_utils.exceptions import InvalidInformation,ObjectDoesNotExist
from django_quiz.common_utils.security import login_required

class CategoryQuiz(APIView):

    """
    Get a quiz given a category
    """

    def get(self,request,category_id):
        response_data = []
        try:
            questions = Question.objects.random(category_id)
        except Exception as e:
            raise ObjectDoesNotExist(e)
        serializer = QuestionSerializer(questions,many=True)
        for data in serializer.data:
            no_of_options = data['options']['number_of_options']
            key_list = data['options'].keys()
            for i in range(no_of_options+1,len(key_list)):
                del data['options'][key_list[i]]
        response = generateresponse('Success','Quiz',serializer.data)
        return Response(response)

class CheckAnswer(APIView):

    """
    Check answer of a specific question
    """

    def get(self, request, question_id):
        is_correct = False
        try:
            q_obj = Question.objects.get(id=question_id)
            correct_answer = Answers.objects.get(question=q_obj).answer
        except:
            raise InvalidInformation('Question does not exist')
        user_answer = request.query_params.dict()['answer']
        if user_answer == correct_answer:
                is_correct = True
        response = {
                    "question_id": question_id,
                    "is_correct": is_correct
                   }
        return Response(response)


