from django.shortcuts import render
from django.http import JsonResponse
from django_project.stripe_func.methods.requests import create_checkout_session
from .models import Item, Order

def buy_order(request, pk):
    order = Order.objects.get(id=pk)
    item_dict = {
        'id': order.id,
        'name': ", ".join(i.name for i in order.items.all())
    }
    for i in order.items.all():
        item_dict[i.id] = i.name
    item_dict['price'] = sum([i.price for i in order.items.all()])
    session_id = create_checkout_session(item_dict=item_dict)
    return JsonResponse(
        {"id": session_id}
    )

def get_order(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        "order": order
    }
    return render(request, "payments/get_order.html", context=context)

def buy_item(request, pk):
    item = Item.objects.get(id=pk)
    item_dict = {
        'name': item.name,
        'price': item.price,
        'id': item.id
    }
    session_id = create_checkout_session(item_dict=item_dict)
    return JsonResponse(
        {"id": session_id}
    )

def get_item(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        "item": item,
    }
    return render(request, "payments/get_item.html", context=context)

def home_view(request):
    items = Item.objects.all()
    orders = Order.objects.all()
    context = {
        "items": items,
        "orders": orders
    }
    return render(request, "payments/home.html", context=context)