from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("python/", views.python_cource, name="pythoncourse"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    # path("todos/", views.todos, name="todos")
]
