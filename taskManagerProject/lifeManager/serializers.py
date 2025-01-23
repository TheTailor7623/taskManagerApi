from rest_framework import serializers

from lifeManager import models

class AreasSerializer(serializers.ModelSerializer):
    """This area serializer will be allowing us to take in the json from input, translate it to python object to handle in backend and vice versa for POST methods"""
    class Meta:
        model = models.AreasModel
        fields = ("title", "description", "milestones")
        read_only_fields = ("id", "user")