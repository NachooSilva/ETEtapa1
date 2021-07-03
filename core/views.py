from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm, ColaboradorrutForm
# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def Galeria(request):
    colab = Colaborador.objects.all()
    return render(request,'Galeria.html', context={'datos': colab})

def colaborador_crear(request):
    if request.method == 'POST':
        colaborador_form = ColaboradorForm(request.POST, files=request.FILES)
        if colaborador_form.is_valid():
            colaborador_form.save()
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