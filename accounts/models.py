from django.db import models
from django.contrib import auth

# Models
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self) -> str:
        return '@{}'.format(self.username)