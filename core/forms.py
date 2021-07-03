from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget

from .models import Colaborador


class ColaboradorForm(forms.ModelForm):
    
    class Meta: 
        model = Colaborador
        fields = ['rutColaborador', 'image', 'nombre', 'telefono','direccion','correo','pais','contraseña']
        
        labels = {
            'rutColaborador': 'Rut Colaborador',
            'image': 'Imagen',
            'nombre': 'Nombre completo',
            'telefono': 'Telefono',
            'direccion': 'Dirección',
            'correo': 'Correo',
            'pais': 'Pais',
            'contraseña': 'Contraseña',
        }

        widgets = {

            'rutColaborador' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut' 
                }
            ),

            'image' : forms.ClearableFileInput(
                attrs = {
                    'class': 'form-control'
                    
                    
                }
            ),

            'nombre' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre' 
                }
            ),
            'telefono' : forms.NumberInput(
                attrs = { 
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Telefono' 
                }
            ),

            'direccion' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Dirección' 
                }
            ),

            'correo' : forms.EmailInput(
                attrs = {
                    'class': 'form-control',  
                    'placeholder': 'Ingrese Correo' 
                }
            ),

            'pais': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Pais' 
                }
            ),

             'contraseña' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Contraseña' 
                }
            )
        }


class ColaboradorrutForm(forms.ModelForm):
    
    class Meta: 
        model = Colaborador
        fields = ['rutColaborador', 'image', 'nombre', 'telefono','direccion','correo','pais','contraseña']
        
        labels = {
            'rutColaborador': 'Rut Colaborador',
            'image': 'Imagen',
            'nombre': 'Nombre completo',
            'telefono': 'Telefono',
            'direccion': 'Dirección',
            'correo': 'Correo',
            'pais': 'Pais',
            'contraseña': 'Contraseña',
        }

        widgets = {

            'rutColaborador' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut',
                    'readonly': '' 
                }
            ),

            'image' : forms.ClearableFileInput(
                attrs = {
                    'class': 'form-control'
                    
                }
            ),

            'nombre' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre' 
                }
            ),
            'telefono' : forms.NumberInput(
                attrs = { 
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Telefono' 
                }
            ),

            'direccion' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Dirección' 
                }
            ),

            'correo' : forms.EmailInput(
                attrs = {
                    'class': 'form-control',  
                    'placeholder': 'Ingrese Correo' 
                }
            ),

            'pais': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Pais' 
                }
            ),

             'contraseña' : forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Contraseña' 
                }
            )
        }