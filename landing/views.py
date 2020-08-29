from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from .models import Project


# Create your views here.
def landing_view(request):
	projects = Project.objects.all()
	context = {"projects": projects}
	return render(request, "landing.html", context)

def project_detail_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)

def info_view(request):
	return render(request, "info.html", {})