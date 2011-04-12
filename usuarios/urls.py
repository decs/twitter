from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^entrar/$', 'usuarios.views.entrar', name='entrar'),
    url(r'^sair/$', 'usuarios.views.sair', name='sair'),
)
