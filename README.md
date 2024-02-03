Python with DJango Framework.
Link: https://www.youtube.com/watch?v=rHux0gMZ3Eg&t=588s

# 1. Create a Virtual Environment (Optional):
If you want to isolate your Django project, you can create a virtual environment. 
Replace [foldername] with your preferred name.
```
# Create a virtual environment
python -m venv .[foldername]

# Activate the virtual environment
cd .[foldername]/Scripts
./activate

# If activation fails, run this PowerShell script as an administrator:
# Set-ExecutionPolicy Unrestricted -Force
```
# 2. Install Django:
Navigate to the root directory where you want to create your Django project and install Django using pip.
```
# Install Django
pip install django
```
# 3. Create a Django Project:
Create a new Django project by replacing [projectname] with your preferred name.
```
# Create a new Django project
django-admin startproject [projectname]
```
# 4. Create a Django App:
Navigate into the project folder and create a new app by replacing [appname] with your preferred name.
```
# Navigate to the project folder
cd [projectname]

# Create a new app
python manage.py startapp [appname]
```
# 5. Configure Templates and URLs:
Inside the app folder, create a `templates` folder and a file named `urls.py`. 
This is where you'll manage your app's templates and URLs.

# 6. Update INSTALLED_APPS in Settings:
In the settings.py file located in the project's root folder, find the INSTALLED_APPS section and add the name of the app you just created.
```
# settings.py

INSTALLED_APPS = [
    # ... other apps
    '[appname]',
]
```
# 7. Run the Development Server:
Run the following commands to start the Django development server, apply migrations, and run the initial setup.
```
# Start the development server
python manage.py runserver

# Create and apply database migrations
python manage.py makemigrations
python manage.py migrate
```
# 8. Configure URLs and Views:
Inside the app folder, open the `urls.py` file. This is where you'll define the URL patterns for your app.
```
# [appname]/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add more URL patterns as needed
]
```
Now, create views for these URLs. Inside the app folder, open the views.py file and define your views.
```
# [appname]/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is your home view!")
```
# 9. Connect App URLs to Project URLs:
In the project's root folder, open the urls.py file. This is where you'll include your app's URL patterns.
```
# [projectname]/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('[appname]/', include('[appname].urls')),  # Include app-specific URLs
]
```
Replace [appname] with the name of your app.