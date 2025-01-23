from django.shortcuts import render

from rest_framework.views import APIView, Response

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
    pass

class AreasSpecific(APIView):
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