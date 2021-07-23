from django.contrib import admin
from .models import *

#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}
#
#
# admin.site.register(Category, CategoryAdmin)


# from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product


# class CategoryAdmin2(DraggableMPTTAdmin):
#     mptt_indent_field = "title"
#     list_display = ('tree_actions', 'indented_title',
#                     'related_products_count', 'related_products_cumulative_count')
#     list_display_links = ('indented_title',)
#     prepopulated_fields = {'slug': ('title',)}
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#
#         # Add cumulative product count
#         qs = Category.objects.add_related_count(
#                 qs,
#                 Product,
#                 'category',
#                 'products_cumulative_count',
#                 cumulative=True)
#
#         # Add non cumulative product count
#         qs = Category.objects.add_related_count(
#                 qs,
#                  Product,
#                  'category',
#                  'products_count',
#                  cumulative=False)
#         return qs
#
#     def related_products_count(self, instance):
#         return instance.products_count
#     related_products_count.short_description = 'Related products (for this specific category)'
#
#     def related_products_cumulative_count(self, instance):
#         return instance.products_cumulative_count
#     related_products_cumulative_count.short_description = 'Related products (in tree)'
#
# admin.site.register(Category, CategoryAdmin2)

# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'category', 'created', 'updated']
#     prepopulated_fields = {'slug': ('name',)}
#
#
# admin.site.register(SubCategory, SubCategoryAdmin)
# admin, models, urls, views, change_form 변경

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']


admin.site.register(Product, ProductAdmin)