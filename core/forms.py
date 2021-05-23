from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    menssage = forms.CharField(label='Menssagem', widget=forms.Textarea())
