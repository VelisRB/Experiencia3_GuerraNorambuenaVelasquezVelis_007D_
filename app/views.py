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


def mostrar(request):
    clientes= Cliente.objects.all()
    datos={
        'clientes': clientes
    }
    return render(request, 'app/mostrar.html',datos)

def forms_clientes(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('form_enviado')
    else:
        cliente_form= ClienteForm()
    return render(request, 'app/forms_clientes.html', {'cliente_form': cliente_form})


def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar')
    return render(request, 'app/form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar')



def mostrar(request):
    clientes= DatosCliente.objects.all()
    datos={
        'datos del cliente': clientes
    }
    return render(request, 'app/mostrar.html',datos)

def registro(request):
    if request.method=='POST':
        datoscliente_form = DatosClienteForm(request.POST)
        if datoscliente_form.is_valid():
            datoscliente_form.save()
            return redirect('form_enviado')
    else:
        datoscliente_form= DatosClienteForm()
    return render(request, 'app/registro.html', {'datoscliente_form': datoscliente_form})




def form_mod_registro(request,id):
    clientes= DatosCliente.objects.get(rut=id)

    datos= {
        'form': DatosClienteForm(instance=clientes),
        'Persona':clientes
        
    }
    return render(request, 'core/form_mod_registro.html',datos)


def form_del_cliente(request, id):
    cliente = DatosCliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar')



 



