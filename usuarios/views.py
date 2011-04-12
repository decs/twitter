from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import login, logout
from django.template import RequestContext
from settings import LOGIN_REDIRECT_URL
from usuarios.forms import *

def entrar(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = AcessoForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
    else:
        form = AcessoForm()
    return render_to_response('usuarios/entrar.html', locals(), context_instance=RequestContext(request))

def sair(request):
    logout(request)
    return HttpResponseRedirect('/')
