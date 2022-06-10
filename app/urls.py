from django.urls import path
from .views import *

urlpatterns = [
    path('index.html', index,name="index"),
    path('', index,name="index"),
    path('personalizados.html', personalizados, name="personalizados"),
    path('galeria.php', galeria, name="galeria"),
    path('aboutus.html', aboutus, name="aboutus"),
    path('sugerencias.html', sugerencias, name="sugerencias"),
    path('mostrar/', mostrar, name="mostrar"),
    path('registro.html', registro, name="registro"),
    path('form_enviado.html', form_enviado, name="form_enviado"),
    path('consultar_registro.html', consultar_registro, name="consultar_registro"),
    path('consultar_datos/', consultar_datos, name="consultar_datos"),
    path('form_mod_registro/<id>', form_mod_registro, name="form_mod_registro"),
    path('forms_clientes.html/', forms_clientes, name="forms_clientes"),
    path('form_del_registro/<id>', form_del_registro, name="form_del_registro"),
]
