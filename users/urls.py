'''Creating the URL patterns for the users application'''

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #Include the default auth urls
    path('', include('django.contrib.auth.urls')),
    #Adding the registration page
    path('register/', views.register, name='register'),
]