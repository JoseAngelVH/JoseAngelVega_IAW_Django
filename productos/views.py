from django.shortcuts import render
from django.http import HttpResponse 
import datetime
from django.template import Template, Context

def productos(request):
    doc_externo = open("/home/usuario/Escritorio/IAW/Django/proyecto1/proyecto1/plantillas/plantilla.html")

    mensaje = "Esta es la plantilla de productos"  

    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"mensaje": mensaje})

    documento = planti.render(ctx)

    return HttpResponse(documento)

def altas_productos(request):
#    secciones = secciones.objects.all()
    return render(request, "subplantillas_productos/altas_productos.html")

def listado_productos(request):
#    productos = productos.objects.all()
#    secciones = secciones.objects.all()
    return render(request, "subplantillas_productos/listado_productos.html")

def altas_secciones(request):
#    secciones = secciones.objects.all()
    return render(request, "subplantillas_secciones/altas_secciones.html")

def listado_secciones(request):
#    productos = productos.objects.all()
#    secciones = secciones.objects.all()
    return render(request, "subplantillas_secciones/listado_secciones.html")