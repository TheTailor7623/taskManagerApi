from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from lifeManager import models, serializers

# Create your views here.
class Dashboard(APIView):
    """This dashboard provides a gateway to all endpoints for application API"""
    def get(self, request, format=None):
        """This get method displays the list of endpoints"""
        return Response(
            {
                "Message":"list of endpoints...",
                "Areas:":"http://127.0.0.1:8000/lifeManager/Areas",
                "Goals:":"http://127.0.0.1:8000/lifeManager/Goals",
                "Projects:":"http://127.0.0.1:8000/lifeManager/Projects",
                "Tasks:":"http://127.0.0.1:8000/lifeManager/Tasks",
                "Sub-tasks:":"http://127.0.0.1:8000/lifeManager/Sub-tasks",
            }
        )

class Areas(APIView):
    """This is a view for the areas API feature"""
    serializer_class = serializers.AreasSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get(self, request, format=None):
        """This will allow us to display the different areas"""
        areas = models.AreasModel.objects.filter(user=request.user)
        serializer = serializers.AreasSerializer(areas, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_302_FOUND
        )

    def post(self, request, format=None):
        """This will allow us to create new areas"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            areas = models.AreasModel.objects.filter(user=request.user)
            serializer = serializers.AreasSerializer(areas, many=True)
            return Response(
                {
                    "message":"Task created successfully",
                    "All areas":serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AreasSpecific(APIView):
    """This is a view for specific areas allowing us to make changes or deleting"""
    def get_object(self, request, format=None):
        """This will allow us to display the different areas"""
        pass

    def patch(self, request, format=None):
        """This will allow us to change an area partially"""
        pass

    def put(self, request, format=None):
        """This will allow us to change an area completely"""
        pass

    def delete(self, request, format=None):
        """This will allow us to DELETE an area completely"""
        pass

class Goals(APIView):
    pass

class GoalsSpecific(APIView):
    pass

class Projects(APIView):
    pass

class ProjectsSpecific(APIView):
    pass

class Tasks(APIView):
    pass

class TasksSpecific(APIView):
    pass

class Subtasks(APIView):
    pass

class SubtasksSpecific(APIView):
    pass