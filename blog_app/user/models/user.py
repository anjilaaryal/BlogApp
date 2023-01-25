from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=300, unique=True, null=False)
    first_name = models.CharField(max_length=200, null=False)
    contact_number = models.CharField(max_length=200, null=False)
    otp_verified = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "contact_number"]