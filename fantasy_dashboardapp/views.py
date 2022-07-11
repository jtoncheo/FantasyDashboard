from django.shortcuts import render

# Create your views here.
def index(request):
    '''Creating the home page for fantasy dashboard.'''
    return render(request, 'fantasy_dashboardapp/index.html')