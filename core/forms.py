from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    menssage = forms.CharField(label='Menssagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        menssage = self.cleaned_data['menssage']

        conteudo = f'Nome: {nome} \
                    Email: {email} \
                    Assunto: {assunto} \
                    Menssagem: {menssage}'

        mail = EmailMessage(
            subject='E-mail enviado via formulario',
            body=conteudo,
            from_email='contato@teudominio.com',
            to=['contato@teudominio.com', ],
            headers={'Replay-To': email}
        )
        mail.send()
