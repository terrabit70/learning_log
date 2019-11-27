from django.shortcuts import render

# Create your views here.
def index(request):
    """Homepage of learning log application"""
    return render(request, 'learning_logs/index.html')