from django.db import models
from django.urls import reverse


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
    category = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    specification = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cloth_sizes = models.BooleanField(default=False, null=True, blank=True)
    shoe_size_man = models.BooleanField(default=False, null=True, blank=True)
    shoe_size_woman = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})