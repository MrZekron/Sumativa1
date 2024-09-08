from django.shortcuts import render, redirect

# Create your views here.
from .models import Vehiculo
from .forms import VehiculoForm

def agregarVehiculo(request):
    form = VehiculoForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = VehiculoForm()
            
    vehiculos = Vehiculo.objects.all()
    data = {'form': form, 'vehiculos': vehiculos}
    return render(request, 'templatesApp/admVehiculo.html', data)


def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(idVehiculo = id)
    vehiculo.delete()
    return redirect('/')

def actualizarVehiculo(request,id):
    vehiculo = Vehiculo.objects.get(idVehiculo = id)
    form = VehiculoForm(instance=vehiculo)
    if (request.method == 'POST'):
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            form = VehiculoForm()
    
    vehiculos = Vehiculo.objects.all()
    data = {'form': form, 'vehiculo':vehiculos}
    return render(request, 'templatesApp/admVehiculo.html', data)