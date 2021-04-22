from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # specify product id as integer othwerwise add will be interpeted
    # as a product id as django won't be able to tell the differnece
    # between a product number and string like add
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

]
