from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, DatosCliente


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nommascota', 'nomtutor', 'correo', 'telefono', 'descripcion']
        labels ={
            'rut': 'Rut', 
            'nommascota': 'Nombre de la mascota', 
            'nomtutor': 'Nombre del tutor', 
            'correo': 'Correo',
            'telefono': 'Telefono del tutor',
            'descripcion': 'Descripcion del pedido',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut sin puntos y con guion', 
                    'id': 'rut'
                }
            ), 
            'nommascota': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre de la mascota', 
                    'id': 'nommascota'
                }
            ), 
            'nomtutor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del tutor', 
                    'id': 'nomtutor'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ), 
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripcion del pedido',
                    'id': 'descripcion',
                }
            )

        }

class DatosClienteForm(forms.ModelForm):

    class Meta: 
        model= DatosCliente
        fields = ['rutreg', 'nombre', 'apellidos', 'correo', 'telefono']
        labels ={
            'rutreg': 'Rut', 
            'nombre': 'Nombre', 
            'apellidos': 'Apellidos',
            'correo': 'Correo',
            'telefono': 'Telefono del tutor',
        }
        widgets={
            'rutreg': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut sin puntos y con guion', 
                    'id': 'rutreg'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre' , 
                    'id': 'nombre'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese sus apellidos', 
                    'id': 'apellidos'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ), 

        }