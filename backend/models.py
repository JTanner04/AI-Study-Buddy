from django.db import models

class Quiz(models.Model):
    question = models.TextField()
    answer = models.TextField()
    options = models.JSONField()  # Store options as JSON
    category = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=20)

    def __str__(self):
        return self.question

class Flashcard(models.Model):
    front = models.TextField()
    back = models.TextField()
    category = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=20)

    def __str__(self):
        return self.front

class StudySuggestion(models.Model):
    topic = models.CharField(max_length=100)
    suggestion_text = models.TextField()

    def __str__(self):
        return self.topic

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Link to Django's User model
    completed_quizzes = models.JSONField()
    study_history = models.JSONField()
    personalized_suggestions = models.JSONField()

    def __str__(self):
        return self.user.username
