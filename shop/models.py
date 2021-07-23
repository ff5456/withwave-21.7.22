# Create your models here.
from django.db import models
from django.urls import reverse
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel

class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        #스스로의 이름을 정의하기 위한 함수
        ordering = ['title']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        #admin 에서 자연스럽게 categories 로 뜬다

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_in_category_detail', args=[self.id, self.slug])


# class SubCategory(models.Model):
#     name = models.CharField(max_length=150, db_index=True)
#     slug = models.SlugField(max_length=150, unique=True, db_index=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)
#     class Meta:
#         ordering = ('-created', )
#         verbose_name = 'sub-category'
#         verbose_name_plural = 'sub-categories'
#     def __str__(self):
#         return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])