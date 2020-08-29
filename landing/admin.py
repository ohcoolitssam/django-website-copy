from django.contrib import admin
from .models import Project

#my admin models
admin.site.site_header = "samuel phillips' portfolio admin"

admin.site.register(Project)