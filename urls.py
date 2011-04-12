from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'twitter.views.principal', name='principal'),
    url(r'^registrar/$', 'twitter.views.registrar', name='registrar'),
    url(r'^editar/$', 'twitter.views.editar', name='editar'),
    (r'^', include('usuarios.urls')),
    url(r'^buscar/$', 'twitter.views.buscar', name='buscar'),
    url(r'^@?(?P<usuario>\w+)/$', 'twitter.views.perfil', name='perfil'),
    url(r'^@?(?P<usuario>\w+)/seguir/$', 'twitter.views.seguir', name='seguir'),
    url(r'^@?(?P<usuario>\w+)/parar/$', 'twitter.views.parar', name='parar'),
)
