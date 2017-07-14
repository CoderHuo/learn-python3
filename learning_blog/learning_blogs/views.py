from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Topic


def index(request):
    return render(request, 'learning_blogs/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_blogs/topics.html', context=context)


def topic(request, topic_id):
    """显示主题下内容"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_blogs/topic.html', context=context)
