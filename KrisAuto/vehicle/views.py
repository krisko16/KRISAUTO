from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewItemForm, EditItemForm
from .models import Category, Vehicle

def vehicles(request):
    query = request.GET.get('query', '')
    model = request.GET.get('model', '')
    price = request.GET.get('price', '')
    categories = Category.objects.all()
    vehicles = Vehicle.objects.all()

    if query:
        vehicles = vehicles.filter(make__icontains=query)

    if model:
        vehicles = vehicles.filter(model__icontains=model)

    if price:
        try:
            price = float(price)
            vehicles = vehicles.filter(price=price)
        except ValueError:
            # Handle the case where the price entered is not a valid number
            pass    

    return render(request, 'vehicle/vehicles.html',{
        'vehicles': vehicles,
        'query': query,
        'model': model,
        'price':price,
        'categories':categories
    })

def detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    return render(request, 'vehicle/detail.html', {
        'vehicle': vehicle,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
           vehicle = form.save(commit=False) 
           vehicle.created_by = request.user
           vehicle.save()

           return redirect('vehicle:detail', pk=vehicle.id)
    else:    
        form= NewItemForm()

    return render(request, 'vehicle/form.html',{
        'form': form,
        'title': 'New item',
    })

@login_required
def delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, created_by=request.user)
    vehicle.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=vehicle)

        if form.is_valid():
            form.save()

            return redirect('vehicle:detail', pk=vehicle.id)
    else:    
        form= EditItemForm(instance=vehicle)

    return render(request, 'vehicle/form.html',{
        'form': form,
        'title': 'Edit item',
    })