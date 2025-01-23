from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from taskManager import serializers

from taskManager.models import Task

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
                "List/Create Tasks": "http://127.0.0.1:8000/api/tasks",
                "Retrieve Task by ID": "http://127.0.0.1:8000/api/tasks/<id>",
                "Update Task by ID": "http://127.0.0.1:8000/api/tasks/<id>",
                "Delete Task by ID": "http://127.0.0.1:8000/api/tasks/<id>",
            },
        }

        return Response({
            "message": "Welcome to the Task Manager API",
            "api_endpoints": api_endpoints,
        })

class ApiRegisterView(APIView):
    """Allows users to register"""

    serializer_class = serializers.ApiRegisterSerializer

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

class ApiLoginView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ApiTaskView(APIView):
    """This view will handle creating and viewing tasks"""
    serializer_class = serializers.ApiTaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get(self, request, format=None):
        """Returns all current tasks for the user"""
        tasks = Task.objects.filter(user=request.user)
        serializer = serializers.ApiTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Adds a task"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            tasks = Task.objects.filter(user=request.user)
            serializer = serializers.ApiTaskSerializer(tasks, many=True)
            return Response(
                {
                    "message":"Task created successfully",
                    "All tasks":serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ApiTaskViewID(APIView):
    """This view will handle CRUD operations between the serializer and model"""
    serializer_class = serializers.ApiTaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get_object(self, task_id):
        """Helper method used to retrieve a task"""
        try:
            return Task.objects.get(id=task_id, user=self.request.user)
        except Task.DoesNotExist:
            return None

    def get(self, request, task_id, format=None):
        """GET method to find a task"""
        task = self.get_object(task_id)
        if not task:
            return Response(
                {
                    "message":"Task not found",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializers = self.serializer_class(task)
        return Response(
            {
                "task":serializers.data,
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, task_id, format=None):
        """Updates tasks"""
        try:
            task = Task.objects.get(id = task_id, user=request.user)
        except Task.DoesNotExist:
            return Response(
                {
                    "message":"Task not found or you do not have permission to update it",
                },
                status = status.HTTP_404_NOT_FOUND
            )
        serializers = self.serializer_class(task, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                {
                    "message":"Task updated successfully",
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, task_id, format=None):
        """Updates tasks"""
        try:
            task = Task.objects.get(id = task_id, user=request.user)
        except Task.DoesNotExist:
            return Response(
                {
                    "message":"Task not found or you do not have permission to update it",
                },
                status = status.HTTP_404_NOT_FOUND
            )
        serializers = self.serializer_class(task, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(
                {
                    "message":"Task updated successfully",
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, task_id, format=None):
        """Deletes a task"""
        try:
            task = Task.objects.get(id = task_id, user=request.user)
        except Task.DoesNotExist:
            return Response(
                {
                    "message":"Task not found or you do not have permission to update it",
                },
                status = status.HTTP_404_NOT_FOUND
            )
        task.delete()
        return Response(
            {
                "message":"Task deleted successfully",
            },
            status=status.HTTP_200_OK
        )