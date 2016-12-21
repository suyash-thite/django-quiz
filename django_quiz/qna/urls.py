from django.conf.urls import url, include
from django.contrib import admin
from views import QuestionList, QuestionDetail
urlpatterns = [
    url(r'^$', QuestionList.as_view()),
    url(r'^(?P<question_id>[0-9]+)/', QuestionDetail.as_view())
]
