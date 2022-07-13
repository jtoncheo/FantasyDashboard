from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

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

def new_topic(request):
    '''Adding a new topic'''
    if request.method != 'POST':
        #No data submitted, create a blank form 
        form = TopicForm()
    else:
        #POST data submmitted then process 
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('fantasy_dashboardapp:topics')
    
    # Display a blank or invalid form 
    context = {'form': form}
    return render(request, 'fantasy_dashboardapp/new_topic.html', context)



