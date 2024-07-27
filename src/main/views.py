from django.shortcuts import render
from .models import Projects


def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'main/index.html', context)
