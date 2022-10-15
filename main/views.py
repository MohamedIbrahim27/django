from multiprocessing import context
from django.shortcuts import render
from .models import project 
# Create your views here.

def main_page(request):
    main_page = project.objects.all()
    context ={'projects' :main_page }
    return render(request, 'main/main.html' , context)

def main_detail(request , slug):
    main_detail = project.objects.get(slug=slug)
    context ={'project' :main_detail }
    return render(request, 'main/main_detail.html' , context)
