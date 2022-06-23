from unicodedata import name
from django.db import models

class Electrician(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='media/%m/',blank=True)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)


    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    electrician_id = models.IntegerField(blank=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return f'Order {self.id}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    electrician = models.ForeignKey(Electrician,related_name='order_items',on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.rate