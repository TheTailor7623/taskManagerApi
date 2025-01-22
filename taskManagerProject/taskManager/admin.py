from django.contrib import admin
from taskManager import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Task)