'''Adding the URL patterns for the fantasy dashboard app'''

from django.urls import path 

from . import views

app_name = 'fantasy_dashboardapp'
urlpatterns = [
    #Landing Page - Home Page
    path('', views.index, name='index'),
    #Page that shows all of the topics 
    path('topics/', views.topics, name='topics'),
]