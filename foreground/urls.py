#!usr/bin/env python
#coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('',
     url(r'^$', 'foreground.views.index',name="fore_index"),
     url(r'^about/$', 'foreground.views.about',name="fore_about"),
     url(r'^case/$', 'foreground.views.case',name="fore_case"),
)
