from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='shop', null=True, blank=True)
    precio = models.FloatField()
    availibility = models.BooleanField(default=True)
    categories = models.ForeignKey('ProductCategory', related_name='products', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name