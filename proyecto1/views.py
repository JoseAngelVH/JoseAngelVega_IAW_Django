from django.http import HttpResponse
import datetime
from django.template import Template, Context

def home(request):
    return HttpResponse("Hello, World! Esta es la pagina de inicio\n")

def index(request):
    return HttpResponse("Hello, World!\n")

def calculaEdad(request, edad, agno):
    periodo = agno - 2026
    edadFutura = edad + periodo 
    documento = """
    <html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2> </body> </html> 
    """ % (agno, edadFutura)
    return HttpResponse(documento)

def saludo(request):
    doc_externo = open("/home/usuario/Escritorio/IAW/Django/proyecto1/proyecto1/plantillas/plantilla.html")

    nombre = "Jose"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": nombre})

    documento = planti.render(ctx)

    return HttpResponse(documento)   