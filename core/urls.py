from django.urls import path
from .views import fichacomponentes, index, prearmados, carrito, contacto, discoduro, discossd,fichacomponentes,fichapc,gabinetes,memoriasram,pagoaprobado,placasmadres,politicadereembolso,procesadores,quienessomos,software,tarjetasdevideo,terminoycondiciones



urlpatterns = [
    path('',index,name="index"),
    path('prearmados',prearmados,name="prearmados"),
    
    path('carrito',carrito,name="carrito"),
    path('contacto',contacto,name="contacto"),
    path('discoduro',discoduro,name="discoduro"),
    path('discossd',discossd,name="discossd"),
    path('fichacomponentes',fichacomponentes,name="fichacomponentes"),

    path('fichapc',fichapc,name="fichapc"),
    path('gabinetes',gabinetes,name="gabinetes"),
    path('memoriasram',memoriasram,name="memoriasram"),
    path('pagoaprobado',pagoaprobado,name="pagoaprobado"),
    path('placasmadres',placasmadres,name="placasmadres"),
    path('politicadereembolso',politicadereembolso,name="politicadereembolso"),
    
    path('procesadores',procesadores,name="procesadores"),
    path('quienessomos',quienessomos,name="quienessomos"),
    path('software',software,name="software"),
    path('tarjetasdevideo',tarjetasdevideo,name="tarjetasdevideo"),
    path('terminoycondiciones',terminoycondiciones,name="terminoycondiciones")
]

