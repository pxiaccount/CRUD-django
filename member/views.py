from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member

def index(request):
    member = Member.objects.all()
    return render(request, 'index.html', {
        "member": member
    })

def add(request):
    return render(request, 'add.html')

def add_to_model(request):
    name = request.POST['name']
    favorite_food = request.POST['food']
    member = Member(name=name, favorite_food=favorite_food)
    member.save()
    return redirect('index')

def update(request, id):
    member = Member.objects.get(id=id)
    return render(request, 'update.html', {
        "member": member
    })

def update_to_model(request, id):
    name = request.POST['name']
    favorite_food = request.POST['food']
    member = Member.objects.get(id=id)
    member.name = name
    member.favorite_food = favorite_food
    member.save()
    return redirect('index')

def delete_to_model(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('index')