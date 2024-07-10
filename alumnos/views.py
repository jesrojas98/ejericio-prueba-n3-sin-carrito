from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import productos
 # Create your views here.

def listar(request):
    producto= productos.objects.all()
    context={'producto': producto}
    return render(request, 'alumnos/alumnos_list.html', context)
    

def login(request):
    producto= productos.objects.all()
    context={'producto': producto}
    return render(request,'instituto/login.html', context)

def index(request):
    producto= productos.objects.all()
    context={'producto': producto}
    return render(request, 'alumnos/index.html', context)
@login_required(login_url="/accounts/login/")
def alumnosAdd(request):
    if request.method == 'POST':
        _id = request.POST["id"]
        _nombre = request.POST["nombre"]
        _descripcion = request.POST['descripcion']
        _precio = request.POST['precio']

        producto = productos.objects.create(
            id=_id,
            nombre=_nombre,
            descripcion=_descripcion,
            precio=_precio          
        )
        producto.save()
        return render(request, 'alumnos/alumnos_add.html')
    else:
        return render(request, 'alumnos/alumnos_add.html')
@login_required(login_url="/accounts/login/")    
def alumnos_del(request,pk):
    context={}
    try:
        producto=productos.objects.get(id=pk)

        producto.delete()
        mensaje="Bien, datos elimindados..."
        producto= productos.objects.all()
        context={'produto': producto, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        producto = productos.objects.all()
        context={'producto': producto, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
@login_required(login_url="/accounts/login/")   
def alumnos_findEdit(request,pk):

    if pk != "":
        producto=productos.objects.get(id=pk)
        context={'producto': producto}
        if producto:
            return render(request, 'alumnos/alumnos_edit.html', context)

        else:  
            context={'mensaje: '"Error rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html', context)


@login_required(login_url="/accounts/login/")
def alumnosUpdate(request):
    if request.method == "post":
            _id=request.POST["id"]
            _nombre = request.POST['nombre']
            _descripcion = request.POST['descripcion']
            _precio = request.POST['precio']

            producto = productos()
            producto.nombre=_nombre
            producto.id=_id
            producto.descripcion=_descripcion
            producto.precio=_precio
            producto.save()
            context={"mensaje": "Ok, datos actualizados", 'producto': producto}
            return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        producto=productos.objects.all()
        context={'producto': producto}
        return render(request, 'alumnos/alumnos_edit.html', context)
    
    
        
