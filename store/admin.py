from django.contrib import admin
from .models import Products , Variation
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','Variation_category','variation_value','is_active')
    list_editable = ('is_active',)

admin.site.register(Products,ProductsAdmin)
admin.site.register(Variation,VariationAdmin)