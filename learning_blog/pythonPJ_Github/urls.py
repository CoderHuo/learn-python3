#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

__author__ = 'Mr.Huo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bar/', views.bar_chart, name='bar_chart'),
    url(r'^line/', views.line_chart, name='line_chart'),
]
