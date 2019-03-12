from django.db import models
from django.contrib.auth.models import AbstractUser,  BaseUserManager
from my_blog.models.base import BaseModel
from datetime import timedelta



class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email),
                          **kwargs)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, BaseModel):

    objects = UserManager()

    username = None

    email = models.EmailField(unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
