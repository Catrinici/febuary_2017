from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def create_product(self, postData):
        self.create(name=postData['name'], description=postData['description'],price=postData['price'])

    def update_product(self, postData, id):
        product = self.get(id=id)
        if postData['name']:
            product.name = postData['name']
        if postData['description']:
            product.description = postData['description']
        if postData['price']:
            product.price = postData['price']
        product.save()

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ProductManager()
