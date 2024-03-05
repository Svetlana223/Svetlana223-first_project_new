from django.core.files.storage import FileSystemStorage
from django.utils.timezone import now
from datetime import timedelta
from django.shortcuts import render, HttpResponse
from .models import User, Order
from .forms import ProductForm


def index(request):
    return HttpResponse('Добро пожаловать!')


def get_user_orders_by_period(user_id):
    user = User.objects.get(id=user_id)
    end_date = now()
    periods = {
        'week': end_date - timedelta(days=7),
        'month': end_date - timedelta(days=30),
        'year': end_date - timedelta(days=365),
    }
    products_in_periods = {}

    for period, start_date in periods.items():
        orders = Order.objects.filter(user=user, order_date__range=[start_date, end_date])
        products = set()
        for order in orders:
            for product in order.products.all():
                products.add(product)
        products_in_periods[period] = products

    return products_in_periods


def user_orders_view(request, user_id):
    products_in_periods = get_user_orders_by_period(user_id)
    return render(request, 'hw_2_app/user_orders.html',
                  {'products_in_periods': products_in_periods, 'user_id': user_id})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            return render(request, "hw_2_app/product_saved.html", {'product': product})
        else:
            return render(request, "hw_2_app/product_create.html", {'form': form})
    return render(request, "hw_2_app/product_create.html", {'form': ProductForm})
