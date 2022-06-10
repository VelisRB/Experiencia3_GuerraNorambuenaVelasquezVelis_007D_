from django.contrib import admin
from .models import Cliente, DatosCliente
# Register your models here.
admin.site.register(Cliente)
admin.site.register(DatosCliente)