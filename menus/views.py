# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from models import *
from pedidos.models import *
from pedidos.forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')

def index(request):
    page_title = "Perosonaliza tu menu"
    user = request.user
    template = Template.objects.all()
    if request.method == 'POST':
        form_template = pedidoForm(request.POST,request.FILES)
        if form_template.is_valid():
            template = form_empleado.save(commit = False)
            template.save()           
            return redirect(template.get_absolute_url())
    else:
        form_template = pedidoForm()
    args = {}
    args.update(csrf(request))   
    template_name ="index.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def logout(request):
    auth_logout(request)
    return redirect('/')