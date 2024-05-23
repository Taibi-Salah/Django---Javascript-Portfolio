from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here.

def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")  # Corrected from "contact.hmtl" to "contact.html"

def project(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "project.html", {"project": project})

def error404(request, exception):
    return render(request, '404.html', status=404)


