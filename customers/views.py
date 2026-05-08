from django.shortcuts import render , redirect
from . models import Customer
from . forms import CustomerForm
# Create your views here.

def CustomerCreateView(request):
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Replace 'customer_list' with the actual URL name for the customer list page
    else:
        form=CustomerForm()
    return render(request, 'customers/create.html', {'form': form})