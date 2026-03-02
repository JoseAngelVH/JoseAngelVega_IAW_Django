from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Template, Context

def inicio(request):
    doc_externo = open("C:\\Users\\Usuario\\Desktop\\JoseAngelVega_IAW_Django\\proyecto1\\plantillas\\plantilla.html")

    mensaje = "Bienvenido a la página de inicio"

    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"mensaje": mensaje})

    documento = planti.render(ctx)

    return HttpResponse(documento)
