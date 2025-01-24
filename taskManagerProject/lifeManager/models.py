import json
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class AreasModel(models.Model):
    """This is a model for areas"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    milestones=models.JSONField()

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"

class GoalsModel(models.Model):
    """This is a model for goals"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    milestones=models.JSONField()

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"

class ProjectsModel(models.Model):
    """This is a model for projects"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    milestones=models.JSONField()

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"

class TasksModel(models.Model):
    """This is a model for projects"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    milestones=models.JSONField()

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"

class SubtasksModel(models.Model):
    """This is a model for projects"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subtask=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

    def __str__(self):
        """This shows what gets displayed in the shell"""
        return f"{self.title}"