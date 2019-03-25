from rest_framework import serializers

from .models import Choice,Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    choices = ChoiceSerializer(many=True, read_only=True, required=False)



