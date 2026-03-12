from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    fecha = request.GET.get('fecha')
    mostrar = request.GET.get('mostrar', '')
    if mostrar == 'inactivos':
        ventas = Venta.objects.filter(activo=False)
    else:
        ventas = Venta.objects.filter(activo=True)
    total_ventas = None

    if fecha:
        ventas = ventas.filter(fecha=fecha)
        total_ventas = ventas.count()

    fechas = Venta.objects.values_list('fecha', flat=True).distinct()

    return render(request, "ventas/ventas.html", {
        "ventas": ventas,
        "fechas": fechas,
        "total_ventas": total_ventas,
        "fecha_seleccionada": fecha,
        "mostrar": mostrar
    })

def nueva_venta(request):
    form = VentaForm(request.POST or None) 
    if form.is_valid(): 
        form.save()
        return redirect("ventas")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": "Nueva Venta",
        "url_lista": "/ventas/"
    })

def editar_venta(request, id):
    venta = get_object_or_404(Venta, id=id) 
    form = VentaForm(request.POST or None, instance=venta)
    if form.is_valid():
        form.save()
        return redirect("ventas")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": f"Editar Venta #{venta.id}",
        "url_lista": "/productos/"
    })

def anular_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    venta.activo = False 
    venta.save()
    return redirect("ventas")

def reactivar_venta(request, id):
    """Reactivar una venta anulada (activo=True)."""
    venta = get_object_or_404(Venta, id=id)
    venta.activo = True
    venta.save()
    return redirect("ventas")
