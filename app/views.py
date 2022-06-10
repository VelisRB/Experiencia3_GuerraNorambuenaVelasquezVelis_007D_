from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Cliente, DatosCliente
from .forms import ClienteForm, DatosClienteForm
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def personalizados(request):
    return render(request, 'app/personalizados.html')

def galeria(request):
    return render(request, 'app/galeria.php')

def aboutus(request):
    return render(request, 'app/aboutus.html')

def sugerencias(request):
    return render(request, 'app/sugerencias.html')

def registro(request):
    return render(request, 'app/registro.html')

def form_enviado(request):
    return render(request, 'app/form_enviado.html')

def consultar_registro(request):
    return render(request, 'app/consultar_registro.html')

def consultar_datos(request):
    return render(request, 'app/consultar_datos.html')
    


def mostrar(request):
    datoscliente= DatosCliente.objects.all()
    datos={
        'datoscliente': datoscliente
    }
    return render(request, 'app/mostrar.html',datos)

def form_mod_registro(request, id):
    datoscliente = DatosCliente.objects.get(rutreg=id)
    datos ={
        'form': DatosClienteForm(instance=datoscliente)
    }
    if request.method=='POST':
        formulario = DatosClienteForm(data = request.POST, instance=datoscliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar')
    return render(request, 'app/form_mod_registro.html', datos)

def form_del_registro(request, id):
    datoscliente = DatosCliente.objects.get(rutreg=id)
    datoscliente.delete()
    return redirect('mostrar')


def forms_clientes(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('form_enviado')
    else:
        cliente_form= ClienteForm()
    return render(request, 'app/forms_clientes.html', {'cliente_form': cliente_form})



def registro(request):
    if request.method=='POST':
        datoscliente_form = DatosClienteForm(request.POST)
        if datoscliente_form.is_valid():
            datoscliente_form.save()
            return redirect('form_enviado')
    else:
        datoscliente_form= DatosClienteForm()
    return render(request, 'app/registro.html', {'datoscliente_form': datoscliente_form})


def consultar_datos(request):
    datos={
    }
    rutreg=request.POST['rutreg']
    clientes=DatosCliente.objects.filter(rutreg=rutreg)
    if clientes:
        datos['mensaje']= "Usuario encontrado correctamente"
        Cliente=DatosCliente.objects.get(rutreg=rutreg)
        datos['Persona']=Cliente
        return render (request, 'app/consultar_datos.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'app/consultar_datos.html',datos)










 



