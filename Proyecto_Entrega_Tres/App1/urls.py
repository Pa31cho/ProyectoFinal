from django.urls import path 
from App1 import views

urlpatterns=[
    path('', views.inicio , name="inicio"), # Incio de la paguina
    path('Producto', views.Producto, name="Producto"), # Producto
    path('Cliente', views.Cliente,name="Cliente"),# Cliente
    path('Proveedores', views.Proveedor,name="Proveedor"),# Proveedores
    path('BusquedaProducto',views.BusquedaProducto,name="BusquedaProducto"),
    path('buscar/',views.buscar),
]