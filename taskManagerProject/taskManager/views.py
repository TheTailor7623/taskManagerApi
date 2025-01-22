from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from taskManager import serializers

# Create your views here.
class ApiDashboard(APIView):
    """Shows all API endpoints"""

    def get(self, request, format=None):
        """Returns a list of API endpoints"""

        api_endpoints = {
            "User Authentication": {
                "Register": "http://127.0.0.1:8000/api/register",
                "Login": "http://127.0.0.1:8000/api/login",
            },
            "Task Management": {
                "List/Create Tasks": "http://http://127.0.0.1:8000/api/tasks",
                "Retrieve Task by ID": "http://http://127.0.0.1:8000/api/tasks/<id>",
                "Update Task by ID": "http://http://127.0.0.1:8000/api/tasks/<id>",
                "Delete Task by ID": "http://http://127.0.0.1:8000/api/tasks/<id>",
            },
        }

        return Response({
            "message": "Welcome to the Task Manager API",
            "api_endpoints": api_endpoints,
        })

class ApiRegisterView(APIView):
    """Allows users to register"""

    serializer_class = serializers.ApiRegisterViewSerializer

    def post(self, request, format=None):
        """Handles the registration of users"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )