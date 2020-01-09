from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """Homepage of learning log application"""
    return render(request, 'learning_logs/index.html')

def about(request):
    """Page with information about project and author"""
    return render(request, 'learning_logs/about.html')

@login_required
def topics(request):
    """Shows list of topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Shows the theme and its topics"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Creates a new topic"""
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request=request, template_name='learning_logs/new_topic.html', context=context)

@login_required
def new_entry(request, topic_id):
    """Adds a new entry for the topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = TopicForm
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request=request, template_name='learning_logs/new_entry.html', context=context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(viewname='learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request=request, template_name='learning_logs/edit_entry.html', context=context)


































