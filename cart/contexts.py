from django.shortcuts import get_object_or_404
from cuspic.models import CusPic


def cart_contents(request):
    """
    ensure that cart contents are available to all templates
    
    """
    
    cart =request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    
    for id,quantity in cart.items():
        product = get_object_or_404(CusPic,pk=id)
        total += quantity*product.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'product':product})
    return{'cart_items':cart_items, 'total':total, 'product_count':product_count}