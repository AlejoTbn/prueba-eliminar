from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conductor
from .forms import ConductorForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def motox(request):
    return render(request, 'paginas/motox.html')

def conductores(request):
    conductores = Conductor.objects.all()
    print(conductores)
    return render(request, 'conductores/index.html', {'conductores': conductores})

def crear(request):
    formulario = ConductorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('conductores')
    return render(request, 'conductores/crear.html', {'formulario': formulario})

def editar(request, id):
    conductor = Conductor.objects.get(id=id)
    formulario = ConductorForm(request.POST or None, request.FILES or None, instance=conductor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('conductores')
    return render(request, 'conductores/editar.html', {'formulario': formulario})

def eliminar(request, id):
    conductor = Conductor.objects.get(id=id)
    conductor.delete()
    return redirect('conductores')