# django
from django.contrib import admin
# project
from .models import Initiative

admin.site.register(Initiative, admin.ModelAdmin)
