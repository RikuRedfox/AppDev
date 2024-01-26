from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def python_cource(request):
    return render(request, "pages/python-basic-course.html")

# def todos(request):
#     items = TodoItem.objects.all()
#     return render(request, "todos.html", {"todos": items})