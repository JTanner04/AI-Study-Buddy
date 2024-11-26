from django.contrib import admin
from .models import Quiz, Flashcard, StudySuggestion, UserProfile

admin.site.register(Quiz)
admin.site.register(Flashcard)
admin.site.register(StudySuggestion)
admin.site.register(UserProfile)
