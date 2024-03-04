# En simulation/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import SimulationData

def simulate(request):
    # Aquí iría la lógica de simulación
    # Por ejemplo, generación de datos simulados y almacenamiento en la base de datos
    SimulationData.objects.create(value=10)  # Ejemplo de creación de un dato simulado
    
    return JsonResponse({'message': 'Simulation completed'})
