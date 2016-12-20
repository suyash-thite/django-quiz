from models import Question, Answers, Category, Options
from rest_framework import serializers

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
            excluded = set(exclude)
            for field_name in excluded:
                try:
                    self.fields.pop(field_name)
                except KeyError:
                    pass


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for Taskdate object from login.models
    """
    class Meta:
        model = Question
        fields = '__all__'
        depth = 1




class AnswerSerializer(BaseSerializer):
    """
    Serializer for Taskdate object from login.models
    """
    class Meta:
        model = Answers
        fields = '__all__'