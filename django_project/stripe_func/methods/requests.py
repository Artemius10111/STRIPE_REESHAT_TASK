from dataclasses import dataclass
import stripe
from typing import (
  Mapping
)
import os

@dataclass
class SessionId:
    value: str

def setup_secret_key_stripe_to_work() -> None:
    stripe.api_key = os.environ['STRIPE_API_SK']

def create_checkout_session(item_dict: Mapping) -> None:
    """
    Создаем сессию для объекта модели.
    Возвращаем итоговый id из API STRIPE
    """
    id = item_dict['id']
    setup_secret_key_stripe_to_work()
    session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': item_dict['name'],
        },
        'unit_amount': int(item_dict['price']),
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url=f'http://127.0.0.1:8000/buy/{id}',
    cancel_url=f'http://127.0.0.1:8000/buy{id}',
    )
    return session.stripe_id

def buy_checkout_session(session_id: SessionId) -> None:
    """
    Реализация метода buy.
    Делает редирект на форму покупки
    """
    setup_secret_key_stripe_to_work()
    stripe.redirectToCheckout(sessionId=session_id)
    return None