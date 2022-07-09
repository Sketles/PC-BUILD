from django.shortcuts import render

from core.forms import DespachoForm
from .models import Despacho

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def prearmados(request):
    return render(request,'core/pre-armados.html')

def carrito(request):
    return render(request,'core/carrito.html')

def contacto(request):
    return render(request,'core/contacto.html')

def discoduro(request):
    return render(request,'core/discoduro.html')

def discossd(request):
    return render(request,'core/discossd.html')

def fichacomponentes(request):
    return render(request,'core/fichacomponentes.html')

def fichapc(request):
    return render(request,'core/fichapc.html')

def gabinetes(request):
    return render(request,'core/gabinetes.html')

def memoriasram(request):
    return render(request,'core/memorias-ram.html')

def pagoaprobado(request):
    return render(request,'core/pagoaprobado.html')

def placasmadres(request):
    return render(request,'core/placas-madres.html')

def politicadereembolso(request):
    return render(request,'core/politica-de-reembolso.html')

def procesadores(request):
    return render(request,'core/procesadores.html')

def quienessomos(request):
    return render(request,'core/quienes-somos.html')

def software(request):
    return render(request,'core/software.html')

def tarjetasdevideo(request):
    return render(request,'core/tarjetasdevideo.html')

def terminoycondiciones(request):
    return render(request,'core/termino-y-condiciones.html')




#-------------------------------------------------------#
#--MOSTRAR ELEMENTOS -----------------------------------#
def formulario(request):
    despachos = Despacho.objects.all()
    datos = {
        'despachos': despachos,
        'form': DespachoForm(),
    }
    if(request.method=='POST'):
        formulario = DespachoForm(request.POST)
        if(formulario.is_valid):
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"
    return render(request,'core/formulario.html',datos)
#-------------------------------------------------------#
#--FIN DEL MOSTRAR ELEMENTOS ---------------------------#




#-------------------------------------------------------#
#--MODIFICAR ELEMENTOS -----------------------------------#
def crud(request,id):
    despacho = Despacho.objects.get(nroorden=id)
    datos = {
        'form': DespachoForm(instance = despacho)
    }
    return render(request,'core/crud.html',datos)
#-------------------------------------------------------#
#--FIN DEL MODIFICAR ELEMENTOS ---------------------------#






















#-------------------------------------------------------#
#--MOSTRAR ELEMENTOS -----------------------------------#
#def formulario(request):
#    despachos = Despacho.objects.all()
#    datos = {
#        'despachos': despachos,
#    }
#    return render(request,'core/formulario.html',datos)
#-------------------------------------------------------#
#--FIN DEL MOSTRAR ELEMENTOS ---------------------------#

#----------------------------------------------------------------#
#--AGREGAR ELEMENTOS --------------------------------------------#
#def crud(request):
#    datosformulario = {
#        'form': DespachoForm()
#    }
#    if(request.method=='POST'):
#        formulario = DespachoForm(request.POST)
#        if(formulario.is_valid):
#            formulario.save()
#            datosformulario['mensaje'] = "Guardados Correctamente"
#    return render(request,'core/crud.html', datosformulario)
#----------------------------------------------------------------#
#--FIN DEL AGREGAR ELEMENTOS ------------------------------------#


