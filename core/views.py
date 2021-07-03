from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm, ColaboradorrutForm
# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def Galeria(request):
    colab = Colaborador.objects.all()
    return render(request,'Galeria.html', context={'datoscolab': colab})




def colaborador_crear(request):
    if request.method == 'POST':
        colaborador_form = ColaboradorForm(request.POST, files=request.FILES)
        if colaborador_form.is_valid():
            contraseñas = (colaborador_form.cleaned_data['rutColaborador'])[0:2] + ((colaborador_form.cleaned_data['nombre'])[0:2]).upper() + ((colaborador_form.cleaned_data['pais'])[-2:]).lower() + str(colaborador_form.cleaned_data['telefono'])[-2:]
            rut= colaborador_form.cleaned_data['rutColaborador']
            colaborador_form.save()
            nuevascontraseñas = Colaborador.objects.get(rutColaborador=rut)
            nuevascontraseñas.contraseña = contraseñas
            nuevascontraseñas.save()

            return redirect('Galeria')
    else:
        colaborador_form = ColaboradorForm()
    return render(request,'core/colaborador_crear.html', {'colaborador_form': colaborador_form})





def colaborador_modi(request, id ):
    colab = Colaborador.objects.get(rutColaborador=id)
    if request.method == 'POST':
        colaborador_form = ColaboradorrutForm(data=request.POST, files=request.FILES, instance=colab)
        if colaborador_form.is_valid():
            colaborador_form.save()
            return redirect('Galeria')
    else:
        colaborador_form = ColaboradorrutForm(instance=colab)
    return render(request,'core/colaborador_modi.html', {'colaborador_form': colaborador_form})

def colaborador_eli(request, id):
    colab = Colaborador.objects.get(rutColaborador=id)
    colab.delete()

    return redirect('Galeria')