from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    name= models.CharField(max_length=20,verbose_name='Бренд')
    img = models.ImageField(upload_to="Brand_img")
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-create_data','-update_data']
        verbose_name="Бренд"
        verbose_name_plural="Бренды"


class Products(models.Model):

    GENDER = [
        ("Male","Male"),
        ("Female","Female"),
        ("for kids","for kids"),
    ]

    brand  = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    title = models.CharField(max_length=50,verbose_name="Name product", blank = False)
    description = models.TextField(verbose_name="description", blank = False)
    size = models.IntegerField(default="35",verbose_name="size",null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    image = models.ImageField(upload_to="Product_img",verbose_name="image", blank = False,null=True )
    gender = models.CharField(verbose_name="Gender", choices=GENDER, max_length=100,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)
       
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-create_data','-update_data']
        verbose_name="Продукт"
        verbose_name_plural="Продукты" 



class Cart(models.Model):
    brand  = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, verbose_name="Product", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return str(self.product)
    
    class Meta:
        ordering = ['-create_data','-update_data']
        verbose_name_plural="Корзины" 


class Order(models.Model):
    brand  = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, verbose_name="Product", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return str(self.product)
    
    class Meta:
        ordering = ['-create_data','-update_data']
        verbose_name_plural="Order" 


class Favorite(models.Model):
    brand  = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, verbose_name="Product", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return str(self.product)
    
    class Meta:
        ordering = ['-create_data','-update_data']
        verbose_name_plural="Favorites" 








