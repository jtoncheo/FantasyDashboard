from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    '''Creating the home page for fantasy dashboard.'''
    return render(request, 'fantasy_dashboardapp/index.html')

def topics(request):
    '''Show all topics.'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'fantasy_dashboardapp/topics.html', context)