from django.shortcuts import render

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



