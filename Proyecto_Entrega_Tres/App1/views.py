from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import ProductoFormu,ClienteFormu,ProveedorFormu

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def Producto(request):
    return render(request,'App1/producto.html')
def Cliente(request):
    return render(request,'App1/cliente.html')
def Proveedor(request):
    return render(request,'App1/proveedor.html')

                            # <<<<<<<<<<<< FORMULARIOS PRODUCTO >>>>>>>>>>>>>
def Producto(request):
    if request.method =='POST':
        miFormulario=ProductoFormu(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=producto(int(informacion['id']),str(informacion['nombre']),int(informacion['cantidad']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=ProductoFormu()
    return render(request, 'App1/producto.html', {"miFormulario": miFormulario})
                        
                            # <<<<<<<<<<<< FORMULARIOS CLIENTE >>>>>>>>>>>>>
def Cliente(request):
    if request.method =='POST':
        miFormulario=ClienteFormu(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),str(informacion['email']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=ClienteFormu()
    return render(request, 'App1/cliente.html', {"miFormulario": miFormulario})
   
                        # <<<<<<<<<<<< FORMULARIOS PROVEEDOR >>>>>>>>>>>>>
def Proveedor(request):
    if request.method =='POST':
        miFormulario=ProveedorFormu(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso = proveedor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),str(informacion['email']),int(informacion['cuil']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario= ProveedorFormu()
    return render(request, 'App1/cliente.html', {"miFormulario": miFormulario})
                            

                            # <<<<<<<<<<<< BUSQUEDA PRODUCTO >>>>>>>>>>>>>
def BusquedaProducto(request):
     return render(request,'App1/busquedaProducto.html')

def buscar(request):
     if request.GET ['id_cantidad']:
        cant = request.GET ['id_cantidad']
        resultado= producto.objects.filter(nombre__icontains=cant)
        return render(request, 'App1/resultadobusqueda.html', {"resultado":resultado}) # Llamo a la busqueda
     else:
          respuesta= "No se encontraron datos para mostrar"
     return HttpResponse (respuesta)     