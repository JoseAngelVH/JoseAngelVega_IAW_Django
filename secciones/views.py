from django.shortcuts import render
from django.http import HttpResponse 
import datetime
from django.template import Template, Context

def secciones(request):
    doc_externo = open("/home/usuario/Escritorio/IAW/Django/proyecto1/proyecto1/plantillas/plantilla.html")

    mensaje = "Esta es la plantilla de secciones"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"mensaje": mensaje})

    documento = planti.render(ctx)

    return HttpResponse(documento)   