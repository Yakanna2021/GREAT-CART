from .views import store, product_detail
from django.urls import path

urlpatterns = [
    path('',store,name='store'),
    path('<slug:category_slug>/',store,name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',product_detail,name='product_detail'),
    
]