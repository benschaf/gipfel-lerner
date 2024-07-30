from django.db import models

# Create your models here.
class FrequentlyAskedQuestion(models.Model):
    """
    A model that represents a frequently asked question.
    """
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
