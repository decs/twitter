from django import forms
from twitter.models import *
 
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ('user', 'seguidores')
    usuario = forms.CharField(max_length=20)
    senha = forms.CharField(max_length=20, widget=forms.PasswordInput(render_value=False))
    
    def clean_usuario(self):
        try:
            usuario = User.objects.get(username=self.cleaned_data['usuario'])
            raise forms.ValidationError('Ja existe um usuario com este nome')
        except User.DoesNotExist:
            return self.cleaned_data['usuario']
    
    def save(self, commit=True):
        usuario = User(username=self.cleaned_data['usuario'])
        usuario.set_password(self.cleaned_data['senha'])
        usuario.save()
        perfil = Perfil(user=usuario, nome=self.cleaned_data['nome'], bio=self.cleaned_data['bio'], local=self.cleaned_data['local'])
        perfil.save()
        return usuario

class BuscaForm(forms.Form):
    termo = forms.CharField(max_length=50)

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ('user', 'seguidores')

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        exclude = ('autor')
        widgets = {
            'conteudo': forms.Textarea(attrs={'cols': 40, 'rows': 3})
        }
