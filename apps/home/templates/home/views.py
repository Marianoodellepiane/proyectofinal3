from django.shortcuts import render
from .forms import Clase1Form, Clase2Form, Clase3Form

def formulario_clase1(request):
    if request.method == 'POST':
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Clase1Form()
    return render(request, 'formulario_clase1.html', {'form': form})

def formulario_clase2(request):
    if request.method == 'POST':
        form = Clase2Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Clase2Form()
    return render(request, 'formulario_clase2.html', {'form': form})

def formulario_clase3(request):
    if request.method == 'POST':
        form = Clase3Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Clase3Form()
    return render(request, 'formulario_clase3.html', {'form': form})
