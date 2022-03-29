from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'Dojos': Dojos.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojos.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
        desc=request.POST['desc']
    )
    return redirect('/')

def add_ninja(request):
    Ninjas.objects.create(
        dojo_id=request.POST['dojo_select'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    return redirect('/')

def delete_dojo(request):
    if request.POST['delete_dojo'] == 'wind':
        dojo4.delete()
        return redirect('/')
    elif request.POST['delete_dojo'] == 'lightning':
        dojo5.delete()
        return redirect('/')
    elif request.POST['delete_dojo'] == 'rain':
        dojo6.delete()
        return redirect('/')
    elif request.POST['delete_dojo'] == 'cow':
        dojo7.delete()
        return redirect('/')
