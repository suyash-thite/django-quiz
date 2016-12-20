from django.contrib import admin
from models import Question, Options, Answers, Category
# Register your models here.
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(Answers)
admin.site.register(Category)
