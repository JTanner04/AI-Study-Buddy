from rest_framework import viewsets
from .models import Quiz, Flashcard, StudySuggestion, UserProfile
from .serializers import QuizSerializer, FlashcardSerializer, StudySuggestionSerializer, UserProfileSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

class StudySuggestionViewSet(viewsets.ModelViewSet):
    queryset = StudySuggestion.objects.all()
    serializer_class = StudySuggestionSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
