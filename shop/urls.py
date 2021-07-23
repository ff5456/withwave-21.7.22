from django.urls import path
from .views import *
from . import views

app_name = 'shop'

urlpatterns = [
    path('<int:id>/<slug:category_slug>/', product_in_category_detail, name='product_in_category_detail'),
    path('left', product_in_category2, name='product_all_left'),
    path('list', product_in_category2, name='product_list'),
    path('', product_in_category, name='product_all'),
    path('pro/<int:id>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('search', product_search, name='product_search'),
    # path('getSubcategory/', views.get_subcategory)
]
