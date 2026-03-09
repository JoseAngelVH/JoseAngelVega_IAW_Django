from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

# Listado
def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True)
    query = request.GET.get('cliente', '')
    if query:
        clientes = Cliente.objects.filter(
            nombre__icontains=query 
        ) | Cliente.objects.filter(
            email__icontains=query
        )
    return render(request, "clientes/clientes.html", {"clientes": clientes})

# Crear
def nuevo_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("clientes")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": "Nuevo Cliente",
        "url_lista": "/clientes/"
    })

# Actualizar
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("clientes")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": f"Editar Cliente #{cliente.id}",
        "url_lista": "/clientes/"
    })

# Anular / eliminar
def anular_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.activo = False
    cliente.save()
    return redirect("clientes")