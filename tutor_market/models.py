from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Tutor(models.Model):
    """
    Represents a tutor in the tutoring marketplace.

    Attributes:
        display_name (str): The display name of the tutor.
        subjects (ManyToManyField): The subjects that the tutor teaches.
        hourly_rate (DecimalField): The hourly rate charged by the tutor.
        description (str): The description of the tutor.
        profile_image (ImageField): The profile image of the tutor.
        values (ManyToManyField): The values associated with the tutor.
        ratings (ManyToManyField): The ratings received by the tutor.
    """

    display_name = models.CharField(max_length=200)
    subjects = models.ManyToManyField('Subject', related_name='tutors')
    # -> Credit for decimal fields: https://docs.djangoproject.com/en/5.0/ref/models/fields/#decimalfield  # noqa
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    catch_phrase = models.CharField(max_length=200, default='Tutoring with a smile!')
    description = models.TextField()
    profile_image = models.ImageField(upload_to='tutor_images')
    values = models.ManyToManyField('Value', related_name='tutors')
    ratings = models.ManyToManyField('Rating', related_name='tutors', blank=True)

    def average_rating(self):
        """
        Returns the average rating of the tutor from all related Rating
        objects.
        """
        return self.ratings.aggregate(Avg('score', default=None))

    def __str__(self):
        return self.display_name


class Student(models.Model):
    """
    Represents a student in the tutor market system.

    Attributes:
        display_name (str): The display name of the student.
        profile_image (ImageField): The profile image of the student.
    """

    display_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='student_images')

    def __str__(self):
        return self.display_name


class Rating(models.Model):
    """
    Represents a rating given by a student to a tutor.

    Attributes:
        tutor (Tutor): The tutor being rated.
        student (Student): The student who gave the rating.
        score (int): The score given by the student (between 0 and 5).
        comment (str): Additional comment provided by the student.

    Methods:
        __str__(): Returns a string representation of the rating.
    """

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.score} - {self.comment}'


class Subject(models.Model):
    """
    Represents a subject in the tutor market.
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Value(models.Model):
    """
    Represents a teaching value that a tutor may have.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
