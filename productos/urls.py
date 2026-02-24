from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('/altas_productos/', views.altas_productos, name='altas_productos'),
    path('/listado_productos/', views.listado_productos, name='listado_productos'),
    path('/altas_secciones/', views.altas_secciones, name='altas_secciones'),
    path('/listado_secciones/', views.listado_secciones, name='listado_secciones'),
]
