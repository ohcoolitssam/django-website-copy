from django.contrib import admin
from .models import Project, webLog

#my admin models
admin.site.site_header = "samuel phillips' portfolio admin"

admin.site.register(Project)
admin.site.register(webLog)