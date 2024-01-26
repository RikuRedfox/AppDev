from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def python_cource(request):
    return render(request, "pages/python-basic-course.html")

def javascript_course(request):
    return render(request, "pages/javascript-basic-course.html")

def cplusplus_course(request):
    return render(request, "pages/c-cpp-basic-course.html")

def lua_course(request):
    return render(request, "pages/lua-basic-course.html")
