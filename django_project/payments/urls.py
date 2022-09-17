from django.urls import path
from .views import (
    buy_order,
    get_item,
    buy_item,
    get_order,
    home_view
) 

app_name = "payments"

urlpatterns = [
    path("", home_view, name="home"),
    path('item/<int:pk>', get_item, name='get_item'),
    path('buy_item/<int:pk>', buy_item, name="buy_item"),
    path('order/<int:pk>', get_order, name="get_order"),
    path('buy_order/<int:pk>', buy_order, name="buy_order")
]
