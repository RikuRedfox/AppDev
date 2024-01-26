from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("python/", views.python_cource, name="pythonCourse"),
    path("javascript/", views.javascript_course, name="javascriptCourse"),
    path("cplusplus/", views.cplusplus_course, name="cplusplusCourse"),
    path("lua/", views.lua_course, name="luaCourse"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    # path("todos/", views.todos, name="todos")
]
