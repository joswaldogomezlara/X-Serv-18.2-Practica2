from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from models import URLs


# Create your views here.

def main(request):

    template = get_template('main.html')
    context = ({})

    return HttpResponse(template.render(context))

@csrf_exempt
def acortar(request):

    if request.method == 'GET':

        template = get_template('formulario.html')
        context = ({})

        return HttpResponse(template.render(context))

    else:

        URL_larga = request.POST['URL_larga']
        URL_larga = URL_larga.replace('%3A',':')
        URL_larga = URL_larga.replace('%2F','/')

        if URL_larga.find('http://') == -1 and URL_larga.find('https://') == -1:
            URL_larga = 'http://' + URL_larga

        try:

            URL = URLs.objects.get(larga=URL_larga)

            template = get_template('error.html')
            context = ({'URL_larga':URL.larga, 'URL_corta':URL.corta})

            respuesta = template.render(context)

        except URLs.DoesNotExist:
     
            lista_URLs = URLs.objects.all()
            URL = URLs(larga=URL_larga, corta=len(lista_URLs)+1)
            URL.save()

            template = get_template('acierto.html')
            context = ({'URL_larga':URL.larga, 'URL_corta':URL.corta})

            respuesta = template.render(context)

        return HttpResponse(respuesta)

def lista(request):

    lista_URLs = URLs.objects.all()
    respuesta = '<ul>'

    for URL in lista_URLs:

        respuesta += '<li><a href=' + URL.larga + '>' + URL.larga + '</a> >>> ' + '<a href=' + URL.larga + '>' + str(URL.corta) + '</a></li>'

    respuesta += '</ul>'

    return HttpResponse(respuesta)

def disp(request, direccion):

    try:

        URL = URLs.objects.get(larga=direccion)
        respuesta = URL.larga

        return HttpResponseRedirect(respuesta)

    except URLs.DoesNotExist:


        try:

            URL = URLs.objects.get(corta=direccion)
            respuesta = URL.larga

            return HttpResponseRedirect(respuesta)

        except URLs.DoesNotExist:

            respuesta = 'La direccion que has solicitado no se encuentra en la base de datos'

            return HttpResponse(respuesta)






















