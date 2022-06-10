from django.urls import path
from .views import index, personalizados, galeria, aboutus, sugerencias, mostrar, forms_clientes, form_mod_cliente, form_del_cliente, registro, form_enviado, consultar_registro

urlpatterns = [
    path('index.html', index,name="index"),
    path('', index,name="index"),
    path('personalizados.html', personalizados, name="personalizados"),
    path('galeria.php', galeria, name="galeria"),
    path('aboutus.html', aboutus, name="aboutus"),
    path('sugerencias.html', sugerencias, name="sugerencias"),
    path('mostrar/', mostrar, name="mostrar"),
    path('forms_clientes.html', forms_clientes, name="forms_clientes"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('registro.html', registro, name="registro"),
    path('form_enviado.html', form_enviado, name="form_enviado"),
    path('consultar_registro.html', consultar_registro, name="consultar_registro"),


]
