from rest_framework import serializers

from models import Question, Answers, Category, Options
from django_quiz.common_utils.exceptions import ObjectDoesNotExist


class BaseSerializer(serializers.ModelSerializer):
    """
    A Base Serializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        # Instantiate the superclass normally
        super(BaseSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if exclude:
            # Drop fields that are specified in the `exclude` argument.
            for field_name in exclude:
                try:
                    self.fields.pop(field_name)
                except KeyError:
                    pass


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category object from qna.models
    """
    class Meta:
        model = Category
        fields = ('id','category_name','category_tags')




class AnswerSerializer(serializers.ModelSerializer):
     """
     Answer Serializer
     """

     class Meta:
        model = Answers
        fields = '__all__'





class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for Question object from qna.models
    """
    question_category = CategorySerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_identifier','question_text','question_tags','question_category')
        depth = 1

    def create(self, validated_data):
        for quest_category in validated_data['question_category']:
            try:
                category = Category.objects.get(category_name=quest_category['category_name'])
                question = Question.objects.create(question_identifier=validated_data['question_identifier'],
                                                   question_text=validated_data['question_text'],
                                                   question_tags=validated_data['question_tags'])
                question.question_category.add(category)
                return question
            except:
                raise ObjectDoesNotExist('Category Name does not exist')



class OptionSerializer(serializers.ModelSerializer):
    """
    Serializer for options from qna.models
    """
    question = QuestionSerializer()

    class Meta:
        model = Options
        fields = '__all__'
        depth = 1




