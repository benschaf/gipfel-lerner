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

class About(models.Model):
    """
    A model that represents the about page.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other entries
            About.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)
