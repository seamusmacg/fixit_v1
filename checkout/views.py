from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm



def view_checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
             'order_form': order_form, 
             'stripe_public_key': 'pk_test_51JWU5BJRbaONEYoNYWYlHfzBbILSbNiRLvwdw8sxEnqzskSlcp7j8WzXceQKsTUbz8e9rfRw6Ar7wAcJjhZLyjUG00C4Jcy9wx',
             'client_secret': 'test client secret',
         }
         
    return render(request, 'checkout/checkout.html', context)




