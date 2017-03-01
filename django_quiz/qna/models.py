from __future__ import unicode_literals
import random

from django.db.models import Count
from django.db import models


class QuestionManager(models.Manager):

    def random(self,category_id):
        random_ids = []
        id_list = self.filter(question_category__id=category_id).values_list('id',flat=True)
        random_list = random.sample(range(0, len(id_list)), 2)
        random.shuffle(random_list)
        for i in random_list:
            random_ids.append(id_list[i])
        return self.filter(id__in=random_ids)

class Question(models.Model):
    question_identifier = models.CharField(max_length=255)
    question_text = models.TextField(blank=False)
    question_category = models.ManyToManyField('Category')
    question_tags = models.CharField(max_length=255, blank=True)

    objects = QuestionManager()

    def __str__(self):
        return "%s:%s" % (self.pk, self.question_identifier)


class Options(models.Model):
    question = models.OneToOneField('Question', blank=False, null=False)
    number_of_options = models.IntegerField(blank=False)
    option1 = models.CharField(max_length=255,blank=False,null=True)
    option2 = models.CharField(max_length=255,blank=False,null=True)
    option3 = models.CharField(max_length=255,blank=True,null=True)
    option4 = models.CharField(max_length=255,blank=True,null=True)
    option5 = models.CharField(max_length=255,blank=True,null=True)
    option6 = models.CharField(max_length=255,blank=True,null=True)
    option7 = models.CharField(max_length=255,blank=True,null=True)
    option8 = models.CharField(max_length=255,blank=True,null=True)
    option9 = models.CharField(max_length=255,blank=True,null=True)
    option10 = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return "%s:%s" % (self.pk, self.question.question_identifier)


class Answers(models.Model):
    question = models.OneToOneField('Question', blank=False, null=False)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' %(self.pk,self.answer)


class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=False, null=False)
    category_tags = models.TextField(blank=True)

    def __str__(self):
        return "%s:%s" % (self.pk, self.category_name)
