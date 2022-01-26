from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ManyToManyField('Category', blank=True,
                                      related_name='categories')
    sku = models.CharField(max_length=5, null=False, unique=False)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=50, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cloth_size = models.BooleanField(default=False, null=True, blank=True)
    shoe_size_man = models.BooleanField(default=False, null=True, blank=True)
    shoe_size_woman = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                default=True)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
