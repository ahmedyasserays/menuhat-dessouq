from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from uuid import uuid4

from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = UserManager()

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_superuser = models.BooleanField(
        "Superuser status",
        default=False,
        help_text="Designates that this user has all permissions without explicitly assigning them.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return self.email
        return self.first_name + " " + self.last_name

    get_full_name.short_description = "Full Name"
