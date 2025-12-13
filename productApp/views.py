from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    firstname = 'Tife'
    roles = ['Admin', 'Finance officer', 'Customer']
    
    return render(request, template_name='index.html', context= {'name': firstname, 'roles': roles})


def getProducts(request):
    products = Product.objects.all().order_by('-created_at', '-updated_at')
    # products = Product.objects.filter(name__icontains = 'coke')
    # product = Product.objects.get(id=1)
    # print(products)
    
    return render(
        request,
        template_name='products.html',
        context={
            'products': products
        }
    )
    
    
def getProductById(request, id):
    # try:
    #     product = Product.objects.get(id = id)
    # except Product.DoesNotExist:
    #     return redirect('products') 
    
    product = get_object_or_404(Product, id = id)
    
    return render(
        request,
        template_name='single.html',
        context={
            'product': product
        }
    )
    
    
    
    
def addProduct(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
        return redirect('products')
    
    else:
        form = ProductForm()
        return render(
            request,
            template_name='product_form.html',
            context={
                'form': form,
                'type': 'Add'
            }   
        )
        


def editProduct(request, id):
    product = get_object_or_404(Product, id = id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        
        return redirect('get-product', id)
    
    else:
        form = ProductForm(instance=product)
        return render(
            request,
            template_name='product_form.html',
            context={
                'form': form,
                'type': 'Edit'
            } 
        )
        
        
def deleteProduct(request, id):
    product = get_object_or_404(Product, id = id)
    product.delete()
    return redirect('products')