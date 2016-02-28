# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage

import logging
logger = logging.getLogger('decoration')

def index(request):
    return render_to_response('foreground/index.html',RequestContext(request))

def about(request):
    return render_to_response('foreground/about.html',RequestContext(request))

def case(request):
    return render_to_response('foreground/case.html',RequestContext(request))
