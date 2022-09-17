from django import template
import os
register = template.Library()

@register.simple_tag
def get_pk():
    return os.environ["STRIPE_API_PK"]
    