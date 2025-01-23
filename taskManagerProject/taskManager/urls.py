from django.urls import path, include
from taskManager import views

urlpatterns = [
    path("", views.ApiDashboard.as_view(), name = "ApiDashboard_name"),
    path("register/", views.ApiRegisterView.as_view(), name = "ApiRegisterView_name"),
    path("login/", views.ApiLoginView.as_view(), name = "ApiLoginView_name"),
    path("tasks/", views.ApiTaskView.as_view(), name = "ApiTaskView_name"),
    path("tasks/<int:task_id>", views.ApiTaskViewID.as_view(), name = "ApiTaskViewID_name"),
]
