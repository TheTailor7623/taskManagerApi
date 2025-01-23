from rest_framework import serializers

from taskManager import models

class ApiRegisterSerializer(serializers.ModelSerializer):
    """Serializes registration fields for users to be able to register"""
    class Meta:
        model = models.User
        fields = ("id", "email", "name", "surname", "password")
        extra_kwargs = {
            "password" : {
                "write_only" : "True",
                "style" : {
                    "input_type" : "password",
                },
            },
        }
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.User.objects.create_user(
            email = validated_data["email"],
            name = validated_data["name"],
            surname = validated_data["surname"],
            password = validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ApiTaskSerializer(serializers.ModelSerializer):
    """Serializes the task fields so user can input tasks"""
    class Meta:
        model = models.Task
        fields = ('id', 'user', 'title', 'description', 'completed', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')