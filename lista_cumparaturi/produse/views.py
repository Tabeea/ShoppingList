from django.shortcuts import render, redirect
from .models import Products, Category, Photo
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

def clothes(request):
    return render(request,'produse/clothes.html')

# Upload photos cattegory


def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    #photos=Photo.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'produse/gallery.html', context)


def viewPhoto(request,id):
    photo = Photo.objects.get(id=id)
    return render(request, 'produse/photo.html', {'photo': photo})

def deletePhoto(request, id):
    photo = Photo.objects.get(pk=id)
    photo.delete()
    return redirect('gallery')
def addPhotos(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'produse/addphoto.html', context)