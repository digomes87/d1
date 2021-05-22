from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programcao Python'
    }
    return render(request, 'core/index.html', context)


def contato(request):
    return render(request, 'core/contato.html')
