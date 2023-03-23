from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    workers_count = User.objects.all().count()
    products_count = products.count()
    orders_count = orders.count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }

    return render(request, 'myinventory/index.html', context)






@login_required(login_url='myiventory-user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.all().count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'myinventory/staff.html', context)

def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'myinventory/staff_detail.html', context)


@login_required(login_url='myiventory-user-login')
def product(request):
    items = Product.objects.all()
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    products_count = items.all().count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name') # cleaned data is only from fields whic have passed the validation tests.
            messages.success(request, f'{product_name} has been added.')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items':items,
        'form': form,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'myinventory/product.html', context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')

    return render(request, 'myinventory/product_delete.html')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context={
        'form': form
    }

    return render(request, 'myinventory/product_update.html', context)

@login_required(login_url='myiventory-user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    products_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    context={
        'orders': orders,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'myinventory/order.html', context)