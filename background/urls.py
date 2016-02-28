#!usr/bin/env python
#coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('',
     url(r'^index$', 'background.views.index',name="back_index"),
     url(r'^login$', 'background.views.login',name="back_login"),
)
