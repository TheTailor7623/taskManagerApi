import json
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class AreasModel(models.Model):
    """This is a model for the areas"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    milestones=models.JSONField()

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"

class GoalsModel(models.Model):
    """This is a model for the goals"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    milestones=models.JSONField()

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"