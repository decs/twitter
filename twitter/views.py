from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User
from settings import LOGIN_REDIRECT_URL
from twitter.models import *
from twitter.forms import *

@login_required(redirect_field_name='destino')
def principal(request):
    try:
        perfil = request.user.get_profile()
        paginas = Paginator(Mensagem.objects.filter(Q(autor=perfil) | Q(autor__in=perfil.seguindo.all)), 20)
        pagina = paginas.page(request.GET.get('pag', 1))
        mensagens = pagina.object_list
        if request.method == 'POST':
            form = MensagemForm(request.POST, instance=Mensagem(autor=perfil))
            if form.is_valid():
                mensagem = form.save()
                return HttpResponseRedirect('/')
        else:
            form = MensagemForm()
            for key in request.GET:
                try:
                    form.fields[key].initial = request.GET[key]
                except KeyError:
                    pass
        busca = BuscaForm()
        return render_to_response('twitter/principal.html', locals(), context_instance=RequestContext(request))
    except (PageNotAnInteger, EmptyPage):
        return HttpResponseRedirect('/')

@login_required(redirect_field_name='destino')
def seguir(request, usuario):
    perfil = get_object_or_404(Perfil, user__username=usuario)
    if perfil != request.user.get_profile():
		perfil.seguidores.add(request.user.get_profile())
    return HttpResponseRedirect('/%s/' % usuario)

@login_required(redirect_field_name='destino')
def parar(request, usuario):
    perfil = get_object_or_404(Perfil, user__username=usuario)
    perfil.seguidores.remove(request.user.get_profile())
    return HttpResponseRedirect('/%s/' % usuario)

@login_required(redirect_field_name='destino')
def editar(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.get_profile())
        if form.is_valid():
            perfil = form.save()
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
    else:
        form = PerfilForm(instance=request.user.get_profile())
    return render_to_response('twitter/editar.html', locals(), context_instance=RequestContext(request))

def buscar(request):
    try:
        termo = request.GET['termo']
        paginas = Paginator(Mensagem.objects.filter(conteudo__icontains=termo), 20)
        pagina = paginas.page(request.GET.get('pag', 1))
        mensagens = pagina.object_list
        return render_to_response('twitter/buscar.html', locals())
    except (PageNotAnInteger, EmptyPage):
        return HttpResponseRedirect('/')
    except KeyError:
        return HttpResponseRedirect('/')

def perfil(request, usuario):
    try:
        perfil = get_object_or_404(Perfil, user__username=usuario)
        paginas = Paginator(Mensagem.objects.filter(autor=perfil), 20)
        pagina = paginas.page(request.GET.get('pag', 1))
        mensagens = pagina.object_list
        return render_to_response('twitter/perfil.html', locals())
    except (PageNotAnInteger, EmptyPage):
        return HttpResponseRedirect('/%s/' % usuario)

def registrar(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = authenticate(username=form.cleaned_data['usuario'], password=form.cleaned_data['senha'])
            login(request, usuario)
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
    else:
        form = CadastroForm()
    return render_to_response('twitter/registrar.html', locals(), context_instance=RequestContext(request))
