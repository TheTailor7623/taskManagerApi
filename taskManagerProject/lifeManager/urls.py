from django.urls import path, include
from lifeManager import views

urlpatterns = [
    path("Dashboard/", views.Dashboard.as_view()),
    path("Areas/", views.Areas.as_view()),
    path("Areas/<int:specificArea>/", views.AreasSpecific.as_view()),
    path("Goals/", views.Goals.as_view()),
    path("Goals/<int:specificGoal>/", views.GoalsSpecific.as_view()),
    path("Projects/", views.Projects.as_view()),
    path("Projects/<int:specificProject>/", views.ProjectsSpecific.as_view()),
    path("Tasks/", views.Tasks.as_view()),
    path("Tasks/<int:specificTask>/", views.TasksSpecific.as_view()),
    path("Subtasks/", views.Subtasks.as_view()),
    path("Subtasks/<int:specificSubTask>/", views.SubtasksSpecific.as_view()),
]
