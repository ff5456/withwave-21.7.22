# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import AddProductForm
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.http import JsonResponse
import json

# def get_subcategory(request):
#     id = request.GET.get('id', '')
#     result = list(SubCategory.objects.filter(category_id=int(id)).values('id', 'name'))
#     return JsonResponse({'foo': 'bar'})


def product_in_category_detail(request, id, category_slug=None):
    category = get_object_or_404(Category, id=id, slug=category_slug)
    current_category = None
    #전체 카테고리
    categories = Category.objects.all()
    #전체 제품군
    products = Product.objects.filter(available_display=True)
    #category_slug 가 있으면(absolute_url 에 들어있기 때문에, absolute_url 로 들어가면 if 문 반복)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    #현재 카테고리, 전체 카테고리, 현재 카테고리 내 제품군
    return render(request, 'shop/category.html', {
        'current_category': current_category,
        'categories': categories,
        'products': products,
    })


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    return render(request, 'shop/home.html', {
            'current_category': current_category,
            'categories': categories,
            'products': products,
        })

def product_in_category2(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    return render(request, 'shop/list.html', {
            'current_category': current_category,
            'categories': categories,
            'products': products,
        })

#카테고리, 제품 전체
def product_in_category3(request, category_slug=None):
    categories = Category.objects.all()
    category_count = len(categories)
    return render(request, 'base.html', {
            'categories': categories,
            'category_count':category_count,
        })

def product_in_category4(request, category_slug=None):
    categories = Category.objects.all()
    category_count = categories.count()
    test = 'test'
    return render(request, 'base.html', {
            'test':test,
        })


def product_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_product=Product.objects.filter(name__contains=searched)
        return render(request,
                      'shop/search.html',
                      {'searched':searched,
                       'searched_product':searched_product})
    else:
        return render(request,
                      'shop/search.html')


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})


@receiver(user_signed_up)
def user_signed_up_(**kwargs):
    user = kwargs['user']
    extra_data = user.socialaccount_set.filter(provider='naver')[0].extra_data
    user.last_name = extra_data['name'][0:4]
    user.first_name = extra_data['name'][4:]
    user.save()