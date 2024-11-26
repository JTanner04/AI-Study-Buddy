from rest_framework import serializers
from .models import Quiz, Flashcard, StudySuggestion, UserProfile

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

class StudySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySuggestion
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
