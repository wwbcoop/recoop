# django
from django.contrib import admin
# project
from .models import TextBlock

admin.site.register(TextBlock, admin.ModelAdmin)
