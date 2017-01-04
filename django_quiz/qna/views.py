from django.shortcuts import render

from models import Question, Answers, Category, Options
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpers import generateresponse
from serializers import QuestionSerializer,CategorySerializer,OptionSerializer
from django_quiz.exceptions import InvalidData,ObjectDoesNotExist


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
            raise InvalidData(serializer.errors)





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

        # def put(self, request, emp_id, task_id):
        #     validate_login(request)
        #     try:
        #         Employee.employee.get(pk=emp_id)
        #     except ObjectDoesNotExist:
        #         raise EmployeeDoesNotExist("This Employee Does Not Exist")
        #     task = self.get_object(task_id)
        #     serializer = TaskSerializer(
        #         task, data=request.data, context={
        #             'request': request})
        #     validate_task = validatetask(
        #         serializer.initial_data,
        #         post=False,
        #         task_id=task_id)
        #     if validate_task:
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # def patch(self, request, emp_id, task_id):
        #     validate_login(request)
        #     is_rejected = False
        #     try:
        #         Employee.employee.get(pk=emp_id)
        #     except ObjectDoesNotExist:
        #         raise EmployeeDoesNotExist("This Employee Does Not Exist")
        #     if "task_name" in request.data:
        #         if request.data.get("task_name") == '':
        #             raise InvalidData("Task name cannot be empty")
        #     task = self.get_object(task_id)
        #     month = task.tasks.first().task_date.month
        #     year = task.tasks.first().task_date.year
        #     is_submitted = SubmittedTimesheet.objects.filter(
        #         emp_id=task.emp_id, month=month, year=year)
        #     if is_submitted.exists():
        #         for timesheet in is_submitted:
        #             if timesheet.approved == 'Rejected':
        #                 is_rejected = True
        #         if is_rejected is not True:
        #             raise TimesheetAlreadySubmitted
        #     serializer = TaskSerializer(
        #         task, data=request.data, partial=True, context={
        #             'request': request})
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # def delete(self, request, emp_id, task_id):
        #     validate_login(request)
        #     try:
        #         Employee.employee.get(pk=emp_id)
        #     except ObjectDoesNotExist:
        #         raise EmployeeDoesNotExist("Employee Does Not Exist")
        #     task = self.get_object(task_id)
        #     task.delete()
        #     response = generateresponse('Success', 'task', 'null')
        #     return Response(response)

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
            raise InvalidData(serializer.errors)

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










