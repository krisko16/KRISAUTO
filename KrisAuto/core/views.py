from django.shortcuts import render, redirect
from vehicle.models import Category, Vehicle
from .forms import SignUpForm

def index(request):
    vehicles = Vehicle.objects.all()
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'vehicles': vehicles,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
