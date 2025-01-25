from django.contrib import admin
from taskManager import models as taskModels
from lifeManager import models as lifeModels

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "task"]
    list_filter = ("user",)

admin.site.register(taskModels.User)
admin.site.register(taskModels.Task)

admin.site.register(lifeModels.AreasModel)
admin.site.register(lifeModels.GoalsModel)
admin.site.register(lifeModels.ProjectsModel)
admin.site.register(lifeModels.TasksModel, TaskModelAdmin)
admin.site.register(lifeModels.SubtasksModel)