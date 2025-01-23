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
    milestones=models.TextField()

    def set_data(self, milestones):
        """This is a method born for us to be able to store a list in the milestones field, we turn the input into json and store it into json format"""
        self.milestones = json.dumps(milestones)

    def get_data(self):
        """This is a method born for us to be able to turn the json back into plain text"""
        return json.loads(self.milestones)

    def __str__(self):
        """This shows what gets displayed in the admin panel"""
        return f"{self.title}"