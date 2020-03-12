from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            send_email(order)
            send_email_to_crew(order)

            return render(request,'orders/order/created.html', {'order':order})
    else:
        form = OrderForm()
    return render(request, 'orders/order/create.html', {'form':form, 'cart':cart})

def send_email(order):
    subject = "Dziękujemy za zakupy na rewolucja.com.pl!"
    message = "Numer twojego zamówienia to: {} ".format(order.id) 
    email_from = "studio.rewo@gmail.com"
    send_mail(subject, message, email_from, [order.email])

def send_email_to_crew(order):
    subject = "Nowe Zamówienie, id: {}".format(order.id)
    message = "Zamówienie: www.rewolucja.com.pl/admin/orders/order/{}/change".format(order.id)
    email_from = "studio.rewo@gmail.com"

    send_mail(subject, message, email_from, ["studio.rewo@gmail.com"]) 
