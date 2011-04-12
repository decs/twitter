from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AcessoForm(forms.Form):
    usuario = forms.CharField(max_length=20)
    senha = forms.CharField(max_length=20, widget=forms.PasswordInput(render_value=False))
    
    def clean_usuario(self):
        try:
            usuario = User.objects.get(username=self.cleaned_data['usuario'])
            return self.cleaned_data['usuario']
        except User.DoesNotExist:
            raise forms.ValidationError('Nao existe um usuario com este nome')
    
    def clean(self):
        usuario = authenticate(username=self.cleaned_data['usuario'], password=self.cleaned_data['senha'])
        if usuario is None:
            raise forms.ValidationError('Senha incorreta')
        elif not usuario.is_active:
            raise forms.ValidationError('Conta inativa')
        return self.cleaned_data
    
    def save(self, commit=True):
        usuario = authenticate(username=self.cleaned_data['usuario'], password=self.cleaned_data['senha'])
        return usuario
