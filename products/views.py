from django.shortcuts import get_object_or_404, redirect, render
from . models import Product
from products.forms import ProductForm
from django.db.models import F
# Create your views here.

def ProductCreateView(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Replace 'product_list' with the actual URL name for your product list view
    else:
        form=ProductForm()
    return render(request, 'createproduct.html', {'form': form})

def ProductListView(request):
    query = request.GET.get('q')
    products=Product.objects.all()
    if query:

        products = products.filter(
            name__icontains=query
        )
    context = {
        'products': products
    }        
    return render(request , 'listproduct.html' , context)

def ProductDetailView(request , pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request , 'productsdetail.html' , {'product':product})    
def ProductUpdateView(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request, 'productupdate.html', {'form': form})

def ProductDeleteView(request , pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'productdelete.html', {'product': product})



def low_stock_products(request):

    products = Product.objects.filter(
        current_stock__lte=F('minimum_stock_alert')
    )

    context = {
        'products': products
    }

    return render(
        request,
        'low_stock.html',
        context
    )