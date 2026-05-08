from django.shortcuts import render , redirect , get_object_or_404
from . models import *
from . forms import *

# Create your views here.


def CreateSupplierView(request):
    if request.method=="POST":
        form=SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form=SupplierForm()
    return render(request, 'suppliercreate.html', {'form': form})   

def ListSupplierView(request):
    query = request.GET.get('q')
    suppliers=Supplier.objects.all()
    if query:

        # suppliers = Supplier.objects.filter(
        suppliers=suppliers.filter(
            name__icontains=query
        )
    context = {
        'suppliers': suppliers
    }         
    return render(request , 'supplierlist.html' , context)

def DetailSupplierView(request , pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request , 'supplierdetail.html' , {'supplier':supplier})    

def UpdateSupplierView(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method=='POST':
        form = SupplierForm(request.POST, instance=supplier)

        if form.is_valid():
            form.save()
            return redirect('supplier_list')

    else:
        form = SupplierForm(instance=supplier)

    return render(request, 'supplierupdate.html', {'form': form})        


def SupplierDeleteView(request , pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'supplierdelete.html', {'supplier': supplier})