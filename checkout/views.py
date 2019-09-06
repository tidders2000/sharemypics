from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from cuspic.models import CusPic
from django.contrib.auth.models import User
import stripe


# Create your views here.
""" a view that allows users to checkout"""
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(CusPic, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity,
                    buyer = request.user
                    )
                olid=order_line_item.id
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                order_line_item.objects.filter(id=olid).delete()
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('download_images'))
            else:
                order_line_item.objects.filter(id=olid).delete()
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            order_line_item.objects.filter(id=olid).delete()
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})

""" a view that allows users to view downloaded images """

@login_required()   
def download_images(request):
    user=request.user.username
    purchases=  OrderLineItem.objects.all()
    
 
    return render(request, 'download_images.html', {'purchases':purchases}, {'user':user})

""" a view that allows users to view sales to date"""
@login_required()
def sales(request):
    sales = OrderLineItem.objects.all()
    total=0
    for sale in sales:
        if sale.product.user == request.user:
           total=total+sale.product.price
   
        
        
    
    return render(request,'sales.html',{'sales':sales, 'total':total})