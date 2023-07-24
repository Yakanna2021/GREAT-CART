from django.shortcuts import render
from store.models import Products

# Create your views here.
def home(request):
    
    products = Products.objects.all().filter(is_available=True).order_by('id')

    context = {
        'products':products,
    }
    return render(request,'home.html',context)