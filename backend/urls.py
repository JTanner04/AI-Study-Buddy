from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, FlashcardViewSet, StudySuggestionViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'flashcards', FlashcardViewSet)
router.register(r'study_suggestions', StudySuggestionViewSet)
router.register(r'user_profiles', UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
