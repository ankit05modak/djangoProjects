from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    #searchcode
    searched_item = request.GET.get('item_name')
    print(searched_item)
    if searched_item != " " and searched_item is not None:
        product_objects = product_objects.filter(title__icontains = searched_item)

    #paginatorcode
    paginator = Paginator(object_list=product_objects, per_page=3)
    product_objects = paginator.get_page(request.GET.get('page'))
    context = {
        "product_objects": product_objects
    }
    return render(request, 'shop/index.html', context)


def detail(request, id):
    print(id)
    product_object = Product.objects.get(id=id)
    context = {
        "product_object" : product_object
    }
    return render(request, 'shop/detail.html', context)
