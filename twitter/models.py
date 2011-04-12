from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.ForeignKey(User, unique=True)
    nome = models.CharField(max_length=80)
    bio = models.TextField()
    local = models.CharField(max_length=50)
    seguidores = models.ManyToManyField('self', symmetrical=False, related_name='seguindo')
    
    def clean_seguidores(self):
        self.seguidores.remove(self) # nao ta funcionando
    
    def __unicode__(self):
        return self.user.username

class Mensagem(models.Model):
    autor = models.ForeignKey(Perfil)
    conteudo = models.CharField(max_length=140)
    publicacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-publicacao']
    
    def responder(self):
        return '@%s ' % self.autor
    
    def compartilhar(self):
        return 'RT @%s %s' % (self.autor, self.conteudo)
    
    def __unicode__(self):
        return self.conteudo
