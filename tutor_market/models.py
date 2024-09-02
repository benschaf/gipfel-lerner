from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Tutor(models.Model):
    """
    Represents a tutor in the tutoring marketplace.

    Attributes:
        user (OneToOneField): The user associated with the tutor.
        display_name (str): The display name of the tutor.
        subjects (ManyToManyField): The subjects that the tutor teaches.
        hourly_rate (DecimalField): The hourly rate charged by the tutor.
        catch_phrase (str): The catch phrase of the tutor.
        description (str): The description of the tutor.
        profile_image (ImageField): The profile image of the tutor.
        values (ManyToManyField): The values associated with the tutor.
        iban (str): The IBAN of the tutor.
        calendly_event_url (URLField): The Calendly event URL of the tutor.
        calendly_personal_token (str): The Calendly personal token of the tutor.
        calendly_access_token (str): The Calendly access token of the tutor.
        calendly_refresh_token (str): The Calendly refresh token of the tutor.
        calendly_token_expires_at (DateTimeField): The expiration date and time of the Calendly token.
        profile_status (bool): The profile status of the tutor.

    Methods:
        average_rating(): Returns the average rating of the tutor from all related Rating objects.
    """

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='tutor')
    display_name = models.CharField(max_length=200)
    subjects = models.ManyToManyField('Subject', related_name='tutors')
    # -> Credit for decimal fields: https://docs.djangoproject.com/en/5.0/ref/models/fields/#decimalfield  # noqa
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    catch_phrase = models.CharField(max_length=200, default='Tutoring with a smile!')
    description = models.TextField()
    profile_image = models.ImageField(upload_to='tutor_images', null=True, blank=True)
    values = models.ManyToManyField('Value', related_name='tutors')
    iban = models.CharField(max_length=34, null=True, blank=True)
    calendly_event_url = models.URLField(null=True, blank=True)
    calendly_personal_token = models.CharField(max_length=600, null=True, blank=True)
    calendly_access_token = models.CharField(max_length=600, null=True, blank=True)
    calendly_refresh_token = models.CharField(max_length=600, null=True, blank=True)
    calendly_token_expires_at = models.DateTimeField(null=True, blank=True)
    profile_status = models.BooleanField(default=False)
    testing_profile = models.BooleanField(default=False)

    def average_rating(self):
        """
        Returns the average rating of the tutor from all related Rating objects.

        Returns:
            float: The average rating of the tutor.
        """
        return Rating.objects.filter(tutor=self).aggregate(Avg('score'))

    def __str__(self):
        """Returns the display name of the tutor."""
        return self.display_name

    class Meta:
        """Defines the ordering of the tutors."""

        ordering = ['display_name']



class Student(models.Model):
    """
    Represents a student in the tutor market system.

    Attributes:
        display_name (str): The display name of the student.
        profile_image (ImageField): The profile image of the student.
    """

    display_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='student_images', null=True, blank=True)

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
    """

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='ratings', default=None)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.score} - {self.comment}'


class Subject(models.Model):
    """
    Represents a subject in the tutor market.
    """

    name = models.CharField(max_length=200, default='Other')

    def __str__(self):
        return f"{self.name} - {self.id}"


class Value(models.Model):
    """
    Represents a teaching value that a tutor may have.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
