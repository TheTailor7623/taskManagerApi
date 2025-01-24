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
            status=status.HTTP_200_OK
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

    serializer_class = serializers.AreasSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get_object(self, areaID):
        """This will allow us to display the different areas"""
        try:
            return models.AreasModel.objects.get(id=areaID, user=self.request.user)
        except models.AreasModel.DoesNotExist:
            return None

    def get(self, request, specificArea, format=None):
        """GET method to find a task"""
        area = self.get_object(specificArea)
        if not area:
            return Response(
                {
                    "message":"Area not found",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializers = self.serializer_class(area)
        return Response(
            {
                "Area":serializers.data,
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, specificArea, format=None):
        """Updates area fully"""
        try:
            area = models.AreasModel.objects.get(id = specificArea, user=request.user)
        except models.AreasModel.DoesNotExist:
            return Response(
                {
                    "message":"Area not found or you do not have permission to update it",
                },
                status = status.HTTP_404_NOT_FOUND
            )
        serializers = self.serializer_class(area, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                {
                    "message":"Area updated successfully",
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, specificArea, format=None):
        """Updates area partially"""
        try:
            area = models.AreasModel.objects.get(id=specificArea, user=request.user)
        except models.AreasModel.DoesNotExist:
            return Response(
                {
                    "message":"Area not found or you do not have permission to update it",
                },
                status = status.HTTP_404_NOT_FOUND
            )
        serializers = self.serializer_class(area, data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(
                {
                    "message":"Area updated successfully",
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, specificArea, format=None):
        """This will allow us to DELETE an area completely"""
        try:
            area = models.AreasModel.objects.get(id=specificArea, user=request.user)
        except models.AreasModel.DoesNotExist:
            return Response(
                {
                    "message":"Area not found or you do not have permission to update it"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        area.delete()
        return Response(
            {
                "message":"Area deleted successfully",
            },
            status=status.HTTP_200_OK
        )

class Goals(APIView):
    """This view is for the goals API feature"""
    serializer_class = serializers.GoalsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get(self, request, format=None):
        """This will allow us to display the different goals"""
        goals = models.GoalsModel.objects.filter(user=request.user)
        serializer = self.serializer_class(goals, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        """This will allow us to create goals"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Goal created successfully"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class GoalsSpecific(APIView):
    """This will allow the user to update and delete a goal"""
    serializer_class = serializers.GoalsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    GoalsModel = models.GoalsModel

    def get(self, request, specificGoal, format=None):
        """This GET method will allow us to view the specific goal"""
        try:
            goal = self.GoalsModel.objects.get(id=specificGoal, user=request.user)
            serializer = self.serializer_class(goal)
        except self.GoalsModel.DoesNotExist:
           return Response(
                {
                    "message":"Goal not found or you do not have permission to update it"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {
                "Message":"Here is your goal",
                "Goal":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, specificGoal, format=None):
        """This PUT method will allow us to make a complete change to a specific goal"""
        try:
            goal = self.GoalsModel.get(id=specificGoal, user=request.user)
        except self.GoalsModel.DoesNotExist:
            return Response(
                {
                    "message":"Goal not found or you do not have permission to update it"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, specificGoal, format=None):
        pass

    def delete(self, request, specificGoal, format=None):
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