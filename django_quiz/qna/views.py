from django.shortcuts import render

from models import Question, Answers, Category, Options
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpers import generateresponse
from serializers import QuestionSerializer


class QuestionList(APIView):
    """
    List all Questions, or create a new Questions.
    """

    def get(self, request):
        response = ''
        try:
            questions = Question.objects.all()
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()
        try:
            serializer = QuestionSerializer(questions, many=True)
            response = generateresponse('Success', 'Questions', serializer.data)
        except Exception as e:
            print e
        return Response(response)

    # def post(self, request, emp_id):
    #     try:
    #         Employee.employee.get(pk=emp_id)
    #     except ObjectDoesNotExist:
    #         raise EmployeeDoesNotExist()
    #     serializer = TaskSerializer(data=request.data)
    #     validate_task = validatetask(serializer.initial_data, post=True)
    #     if validate_task:
    #         try:
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 response = generateresponse(
    #                     'Success', 'tasks', serializer.data)
    #         except Exception as e:
    #             response = {
    #                 "status": status.HTTP_400_BAD_REQUEST,
    #                 "data": {
    #                     "post": serializer.data}}
    #     return Response(response)

class QuestionDetail(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise ObjectDoesNotExist

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