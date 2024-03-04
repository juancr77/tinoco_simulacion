# En simulation_project/urls.py

from django.urls import path
from simulation.views import simulate

urlpatterns = [
    path('simulate/', simulate, name='simulate'),
]
