# from django import template
# from django.conf import settings
# from products.models import Product

# register = template.Library()

# @register.simple_tag
# def get_selected_category(product_id):

#     the_selected_category = Product.objects.filter(product_id)

#     return category

# @register.simple_tag
# def get_category_name(category):

#     the_category_name = the_selected_category.category.friendly_name

#     return the_category_name(category)
