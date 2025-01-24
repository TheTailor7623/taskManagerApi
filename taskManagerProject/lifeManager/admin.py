from django.contrib import admin
from lifeManager import models

# Register your models here.
admin.site.register(models.AreasModel)
admin.site.register(models.GoalsModel)
admin.site.register(models.ProjectsModel)
admin.site.register(models.TasksModel)
admin.site.register(models.SubtasksModel)