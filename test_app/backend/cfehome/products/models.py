import random
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']

class Product(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.80)
    
    @property
    def body(self):
        return self.content

    @property
    def path(self):
        return f"products/{self.pk}/"

    def get_discount(self):
        return "2.5"
        
    def is_public(self):
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    
    