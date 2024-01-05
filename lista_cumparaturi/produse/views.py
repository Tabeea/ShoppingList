from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm


def home(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            products = Products.objects.all()
            context = {'form':form, 'products':products}
            return render(request, 'produse/home.html', context)
    else:
        form = ProductsForm()
        products = Products.objects.all()
        context = {'form': form, 'products': products} # contine atat formularul cat si produsele
        return render(request, 'produse/home.html', context)

def delete(request, id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

def change_status(request, id):
    product = Products.objects.get(pk=id)
    if product.cumparat:
        product.cumparat = False
        product.save()
    else:
        product.cumparat = True
        product.save()
    return redirect('home')


def about(request):
    return render(request,'produse/about.html')