from django import template

register = template.Library()

@register.filter
def starsz(value):
    return range(value)
