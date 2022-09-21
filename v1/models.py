from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=25,unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subject")
    image = models.ImageField(upload_to="Products")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product_Inventry(models.Model):
    product = models.OneToOneField(Product, related_name='product_inventry', on_delete=models.CASCADE)
    price = models.FloatField()
    sell = models.FloatField()
    discount = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.product.sku
    def save(self, *args, **kwargs):
        self.discount = 100-((self.sell/self.price)*100)
        super(Product_Inventry, self).save(*args, **kwargs)

class Product_Stock(models.Model):
    product = models.OneToOneField(Product, related_name='product_stock', on_delete=models.CASCADE)
    stock = models.IntegerField()
    def __str__(self):
        return self.product.sku