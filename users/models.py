from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
