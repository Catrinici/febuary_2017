from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'project_app/index.html', context)

def show(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'project_app/show.html', context)

def edit(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'project_app/edit.html', context)

def delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect('products:index')

def create(request):
    Product.objects.create_product(request.POST)
    return redirect('products:index')

def new(request):
    return render(request, 'project_app/new.html')

def update(request, id):
    Product.objects.update_product(request.POST, id)
    return redirect('products:index')
