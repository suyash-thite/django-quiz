from django.conf.urls import url, include
from django.contrib import admin

from views import QuestionList, QuestionDetail,CategoryList, OptionList,CheckAnswer
from django.conf import settings




urlpatterns = [
    url(r'question/(?P<question_id>[0-9]+)/', QuestionDetail.as_view()),
    url(r'question/options/', OptionList.as_view()),
    url(r'^questions/', QuestionList.as_view()),
    url(r'^categories', CategoryList.as_view()),
    url(r'^checkanswer/(?P<question_id>[0-9]+)/$', CheckAnswer.as_view()),

]
