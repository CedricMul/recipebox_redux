from django.contrib import admin
from recipe_app import models

# Register your models here.
admin.site.register(models.Recipe)
admin.site.register(models.Author)