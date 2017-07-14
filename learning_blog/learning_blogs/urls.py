#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

__author__ = 'Mr.Huo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
