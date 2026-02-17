from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Template, Context

def inicio(request):
    doc_externo = open("/home/usuario/Escritorio/IAW/Django/proyecto1/proyecto1/plantillas/plantilla.html")

    mensaje = "Bienvenido a la página de inicio"

    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"mensaje": mensaje})

    documento = planti.render(ctx)

    return HttpResponse(documento)
