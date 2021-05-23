from django import template
from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programcao Python',
        'produtos': produtos,
    }
    return render(request, 'core/index.html', context)


def contato(request):
    return render(request, 'core/contato.html')

def produto(request, pk):
    try:
        prod = Produto.objects.get(pk=pk)
        context = {
        'produto': prod
        }
    except get_object_or_404(Produto, id=pk):
        raise print('Error in get page 404')

    return render(request, 'core/produto.html', context)


def error404(request, exception):
    template = loader.get_template('error/404.html')
    return HttpResponse(content=template.render(), 
                        content_type='text/html; charset=utf8',
                        status=404)

def error500(request):
    template = loader.get_template('error/500.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500)