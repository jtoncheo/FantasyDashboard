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

def topic(request, topic_id):
    '''Show just a single topic'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'fantasy_dashboardapp/topic.html', context)
    