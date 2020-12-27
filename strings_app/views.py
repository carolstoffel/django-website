from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def manip_strings(request):
    context = {'string_text': 'Seu texto convertido ficará aqui.'}
    print(request.method)
    if request.method == 'POST':
        texto = request.POST.get('task')
        if request.POST.get('btnradio1') is not None:
            texto = texto.upper()
        elif request.POST.get('btnradio2') is not None:
            texto = texto.lower()
        elif request.POST.get('btnradio3') is not None:
            novo_texto = ''
            for index in range(0, len(texto)-1):
                if index % 2 == 0:
                    novo_texto += texto[index].upper()
                else:
                    novo_texto += texto[index].lower()
            texto = novo_texto
        elif request.POST.get('btnradio4') is not None:
            novo_texto = ''
            for i in range(len(texto)-1, -1, -1):
                novo_texto += texto[i]
            texto = novo_texto
        context = {
            'string_text': texto
        }
    return render(request, 'manip_strings.html', context)
    # return HttpResponse("Welcome to task page")


def index(request):
    context = {
        'index_text': "BEM VINDO.",
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Welcome to task page")


def contact(request):
    context = {
        'contato_text': "BEM VINDO.",
    }
    return render(request, 'contact.html', context)
    # return HttpResponse("Welcome to task page")


def projects(request):
    context = {
        'project_text': "BEM VINDO.",
    }
    return render(request, 'projects.html', context)
    # return HttpResponse("Welcome to task page")


def chatbot(request):
    context = {
        'chatbot_text': "BEM VINDO.",
    }
    return render(request, 'chatbot.html', context)


def image_converter(request):
    context = {
        'imageconverter_text': "BEM VINDO.",
    }
    return render(request, 'image_converter.html', context)
