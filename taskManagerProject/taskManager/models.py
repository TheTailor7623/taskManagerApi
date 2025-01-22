from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    """This manages the user accounts"""
    def create_user(self, email, name, surname, password=None):
        """Create and return a user"""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, password):
        """Create and return a superuser"""
        user = self.create_user(email, name, surname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """This is my custom user model"""
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # Connect to the custom manager

    USERNAME_FIELD = 'email'  # Login field
    REQUIRED_FIELDS = ['name', 'surname']  # Required fields when creating a user

    def __str__(self):
        return self.email