import math

from django import template

register = template.Library()


@register.simple_tag
def call_discountPrice(price, Discount):
    if Discount is None or Discount is 0:
        return price
    discountPrice = price
    discountPrice = price - (price * Discount / 100)
    return math.floor(discountPrice)


@register.simple_tag
def progress_bar(total_quantity, Availability):
    progress_bar = Availability
    progress_bar = Availability * (100/total_quantity)
    return math.floor(progress_bar)