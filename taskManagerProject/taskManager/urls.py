from django.urls import path, include

from taskManager import views

urlpatterns = [
    path("", views.ApiDashboard.as_view(), name = "ApiDashboard_name"),
    path("register", views.ApiRegisterView.as_view(), name = "ApiRegisterView_name"),
    # path("login", views.apiDashboard.as_view(), name = "apiDashboard_name"),
    # path("tasks", views.apiDashboard.as_view(), name = "apiDashboard_name"),
    # path("tasks/<id>", views.apiDashboard.as_view(), name = "apiDashboard_name"),
]
