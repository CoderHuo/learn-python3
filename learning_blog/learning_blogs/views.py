from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Topic, Entry
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'learning_blogs/index.html')


def mystyle(request):
    return render(request, 'learning_blogs/mystyle.css')


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


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_blogs:topics'))
    context = {'form': form}
    return render(request, 'learning_blogs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中增加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_blogs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_blogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """在特定的主题中增加新条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_blogs:topic', args=[topic.id]))
    cotext = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_blogs/edit_entry.html', cotext)
