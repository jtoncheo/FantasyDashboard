'''Adding the URL patterns for the fantasy dashboard app'''

from django.urls import path 

from . import views

app_name = 'fantasy_dashboardapp'
urlpatterns = [
    #Landing Page - Home Page
    path('', views.index, name='index'),
    #Page that shows all of the topics 
    path('topics/', views.topics, name='topics'),
    #Adding a new page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]