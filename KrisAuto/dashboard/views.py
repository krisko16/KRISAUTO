from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from vehicle.models import Vehicle

@login_required
def index(request):
    vehicles = Vehicle.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html',{
        'vehicles': vehicles,
    })