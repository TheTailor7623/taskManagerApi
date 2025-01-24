from rest_framework import serializers

from lifeManager import models

class AreasSerializer(serializers.ModelSerializer):
    """This area serializer will be allowing us to take in the json from input, translate it to python object to handle in backend and vice versa for POST methods"""
    class Meta:
        model = models.AreasModel
        fields = ("id","title", "description", "milestones")
        read_only_fields = ("id", "user")

class GoalsSerializer(serializers.ModelSerializer):
    """This goal serializer will be allowing us to take in the json from input, translate it to python object to handle in backend and vice versa for POST methods"""
    class Meta:
        model = models.GoalsModel
        fields = ("id","title", "description", "milestones")
        read_only_fields = ("id", "user")

class ProjectsSerializer(serializers.ModelSerializer):
    """This project serializer will be allowing us to take in the json from input, translate it to python object to handle in backend and vice versa for POST methods"""
    class Meta:
        model = models.ProjectsModel
        fields = ("id","title", "description", "milestones")
        read_only_fields = ("id", "user")

class TasksSerializer(serializers.ModelSerializer):
    """This project serializer will be allowing us to take in the json from input, translate it to python object to handle in backend and vice versa for POST methods"""
    class Meta:
        model = models.TasksModel
        fields = ("id","task", "description", "milestones")
        read_only_fields = ("id", "user")

class SubtasksSerializer(serializers.ModelSerializer):
    """This project serializer will be allowing us to take in the json from input, translate it to python object to handle in backend and vice versa for POST methods"""
    class Meta:
        model = models.SubtasksModel
        fields = ("id","subtask", "description")
        read_only_fields = ("id", "user")