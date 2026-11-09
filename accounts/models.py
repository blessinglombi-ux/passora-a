
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        PARTICIPANT = "participant", "Participant"
        ORGANIZER = "organizer", "Organizer"

    class Language(models.TextChoices):
        ENGLISH = "en", "English"
        FRENCH = "fr", "French"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PARTICIPANT,
    )

    preferred_language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.ENGLISH,
    )

    email_verified = models.BooleanField(default=False)

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
