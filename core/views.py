from django.shortcuts import render
from core.models import Product,Category,Vendor,CartOrderItems,CartOrder,wishlist,Address,ProductImage,ProductReviews

def home(request):
    
    products = Product.objects.filter(product_status='published',featured=True)
    
    context = {
        "products":products
    }
    return render(request, 'index.html',context)


