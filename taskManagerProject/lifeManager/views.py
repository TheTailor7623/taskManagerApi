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
                "Sub-tasks:":"http://127.0.0.1:8000/lifeManager/Subtasks",
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
            goal = self.GoalsModel.objects.get(id=specificGoal, user=request.user)
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
        """This PATCH method will allows us to make partial changes to a goal"""
        try:
            goal = self.GoalsModel.objects.get(id=specificGoal, user=request.user)
        except self.GoalsModel.DoesNotExist:
            return Response(
                {
                    "Message":"Goals was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(goal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message":"Goal updated successfully",
                    "Data":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


    def delete(self, request, specificGoal, format=None):
        """This DELETE method will allow us to delete a goal"""
        try:
            goal = self.GoalsModel.objects.get(id=specificGoal, user=request.user)
        except self.GoalsModel.DoesNotExist:
            return Response(
                {
                    "Message":"Goals was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        goal.delete()
        return Response(
            {
                "Message":"Goal deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )

class Projects(APIView):
    """This Projects class will allow us to make GET and POST requests for the projects API feature"""
    serializer_class = serializers.ProjectsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    ProjectsModel = models.ProjectsModel

    def get(self, request, format=None):
        """This GET method will allows us to display all projects"""
        projects = self.ProjectsModel.objects.filter(user=request.user)
        serializer = self.serializer_class(projects, many=True)
        return Response({
            "Message":"Here is all the projects found",
            "Projects:":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        """This POST method will allow us to create projects"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"The project was created successfully",
                    "Project details:":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProjectsSpecific(APIView):
    """This will allow us to use update or delete methods on specific projects"""
    serializer_class = serializers.ProjectsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    ProjectsModel = models.ProjectsModel

    def get(self, request, specificProject, format=None):
        """This GET method allows us to display the specific project"""
        try:
            project = self.ProjectsModel.objects.get(id=specificProject, user=request.user)
        except self.ProjectsModel.DoesNotExist:
            return Response(
                {
                    "Message":"Project was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(project)
        return Response(
            {
                "Here is the project":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, specificProject, format=None):
        """This PUT method allows us to make changes to a specific project"""
        try:
            project = self.ProjectsModel.objects.get(id=specificProject, user=request.user)
        except self.ProjectsModel.DoesNotExist:
            return Response(
                {
                    "Message":"Project was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Project updated",
                    "Updated project":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, specificProject, format=None):
        """This PATCH method allows us to make partial changes to a specific project"""
        try:
            project = self.ProjectsModel.objects.get(id=specificProject, user=request.user)
        except self.ProjectsModel.DoesNotExist:
            return Response(
                {
                    "Message":"Project was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Project updated successfully",
                    "Updated project:":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, specificProject, format=None):
        """This DELETE method allows us to delete a specific project"""
        try:
            project = self.ProjectsModel.objects.get(id=specificProject, user=request.user)
        except self.ProjectsModel.DoesNotExist:
            return Response(
                {
                    "Message":"Project was not found or you do not have the permission to delete such a project",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        project.delete()
        return Response(
            {
                "Message":"Project deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )

class Tasks(APIView):
    """This view will handle the tasks for this feature in the API"""
    serializer_class = serializers.TasksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    TasksModel = models.TasksModel

    def get(self, request, format=None):
        """This GET mothod allows us to visualise tasks"""
        task = self.TasksModel.objects.filter(user = request.user)
        serializer = self.serializer_class(task, many=True)
        return Response(
            {
                "Message:":"Here are the tasks we found...",
                "Tasks:":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        """This POST method allows us to create tasks"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Task has been added successfully",
                    "Task:":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class TasksSpecific(APIView):
    """This will allow us to use update or delete methods on specific tasks"""
    serializer_class = serializers.TasksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    TasksModel = models.TasksModel

    def get(self, request, specificTask, format=None):
        """This GET method allows us to display the specific project"""
        try:
            task = self.TasksModel.objects.get(id=specificTask, user=request.user)
        except self.TasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Task was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(task)
        return Response(
            {
                "Here is the project":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, specificTask, format=None):
        """This PUT method allows us to make changes to a specific project"""
        try:
            task = self.TasksModel.objects.get(id=specificTask, user=request.user)
        except self.TasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Task was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Task updated",
                    "Updated task":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, specificTask, format=None):
        """This PATCH method allows us to make partial changes to a specific task"""
        try:
            task = self.TasksModel.objects.get(id=specificTask, user=request.user)
        except self.TasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Task was not found or you do not have permission to edit such a task",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Task updated successfully",
                    "Updated task:":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, specificTask, format=None):
        """This DELETE method allows us to delete a specific task"""
        try:
            project = self.TasksModel.objects.get(id=specificTask, user=request.user)
        except self.TasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Task was not found or you do not have the permission to delete such a task",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        project.delete()
        return Response(
            {
                "Message":"Task deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )

class Subtasks(APIView):
    """This view will handle the subtasks for this feature in the API"""
    serializer_class = serializers.SubtasksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    SubtasksModel = models.SubtasksModel

    def get(self, request, format=None):
        """This GET mothod allows us to visualise tasks"""
        subTask = self.SubtasksModel.objects.filter(user = request.user)
        serializer = self.serializer_class(subTask, many=True)
        return Response(
            {
                "Message:":"Here are the subtasks we found...",
                "Subtask:":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        """This POST method allows us to create tasks"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Task has been added successfully",
                    "Task:":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class SubtasksSpecific(APIView):
    """This will allow us to use update or delete methods on specific tasks"""
    serializer_class = serializers.SubtasksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    SubtasksModel = models.SubtasksModel

    def get(self, request, specificSubTask, format=None):
        """This GET method allows us to display the specific subtask"""
        try:
            subTask = self.SubtasksModel.objects.get(id=specificSubTask, user=request.user)
        except self.SubtasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Subtask was not found or you do not have permission to edit such a subtask",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(subTask)
        return Response(
            {
                "Here is the subtask":serializer.data,
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, specificSubTask, format=None):
        """This PUT method allows us to make changes to a specific subtask"""
        try:
            task = self.SubtasksModel.objects.get(id=specificSubTask, user=request.user)
        except self.SubtasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Subtask was not found or you do not have permission to edit such a goal",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Subtask updated",
                    "Updated subtask":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, specificSubTask, format=None):
        """This PATCH method allows us to make partial changes to a specific subtask"""
        try:
            task = self.SubtasksModel.objects.get(id=specificSubTask, user=request.user)
        except self.SubtasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Subtask was not found or you do not have permission to edit such a subtask",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "Message":"Subtask updated successfully",
                    "Updated subtask:":serializer.data,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, specificSubTask, format=None):
        """This DELETE method allows us to delete a specific subtask"""
        try:
            project = self.SubtasksModel.objects.get(id=specificSubTask, user=request.user)
        except self.SubtasksModel.DoesNotExist:
            return Response(
                {
                    "Message":"Subtask was not found or you do not have the permission to delete such a subtask",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        project.delete()
        return Response(
            {
                "Message":"Subtask deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )