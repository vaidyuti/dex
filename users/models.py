from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.create(username=username)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create(username=username, is_superuser=True, is_staff=True)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model used for authenticating users
    """

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    date_joined = models.DateTimeField(
        default=now,
        verbose_name="Joined on",
        help_text="Date and time when the user was created",
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        help_text="User's email address (optional)",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this user should be treated as active",
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Staff",
        help_text="Whether this user has access to the admin site",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="User's full name",
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Username",
        help_text="Username (must be unique)",
    )

    objects = UserManager()

    def __str__(self):
        return str(self.name)
