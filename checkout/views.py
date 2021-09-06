from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from .models import Order, OrderItem

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

def view_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_details = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town': request.POST['town'],
            'address': request.POST['address'],
        }
        order_form = OrderForm(form_details)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                product = Product.objects.get(id=item_id)
                order_item = OrderItem(
                    order=order,
                    product=product,
                    quantity=item_data,
                )
                order_item.save()

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There's an error with the form! Please check if details are correct")
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty!")
            return redirect(reverse('products'))

        checkout_cart = cart_contents(request)
        total = checkout_cart['overall_cost']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'You are missing the Stripe public key.')


    context = {
             'order_form': order_form, 
             'stripe_public_key': stripe_public_key,
             'client_secret': intent.client_secret,
         }
         
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order was processed successfully! Your order number is {order_number}, an email will be sent to {order.email}')

    if 'cart' in request.session:
        del request.session['cart']
    context = {
        'order': order, 
    }

    return render(request, 'checkout/checkout_success.html', context)




