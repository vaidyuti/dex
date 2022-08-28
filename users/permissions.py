from rest_framework import permissions


class User(permissions.IsAdminUser):
    pass
