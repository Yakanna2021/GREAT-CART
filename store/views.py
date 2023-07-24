from django.shortcuts import render, get_object_or_404
from .models import Products
from category.models import Category
from cart.models import CartItem,Cart
from cart.views import _cart_id
# Create your views here.
from django.db.models import Q
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def store(request, category_slug=None):
    categories = None
    products = None
    paged_counter=0
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=categories, is_available=True)
        cnt_prodt = products.count()
    else:
        products = Products.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_counter = paginator.get_page(page)
        cnt_prodt = products.count()

    context={
        'products' : paged_counter,
        'cnt_prodt' :  cnt_prodt
    }

    
    return render(request,'store/store.html',context)

def product_detail(request, category_slug, product_slug ):
    try:
        single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    
    context={
        'single_product' : single_product,
        'in_cart'        : in_cart
    }

 
    return render(request,'store/product_detail.html',context)

def search(request):
    if 'keyword' in request.path:
        keyword = request.GET['keyword']
        if keyword:
            products = Products.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        context = {
            'products':products,
            'product_count':product_count
        }

        return render(request,'store/store.html',context)

