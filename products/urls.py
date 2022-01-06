from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # path('<product_id>', views.product_detail, name='product_detail'),
    path('<selected_category>/<slug:slug>/', views.product_detail, name='product_detail'),
]