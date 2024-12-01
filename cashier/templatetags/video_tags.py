from django import template
register = template.Library()


@register.simple_tag
def suma(services):
    return sum([s.cost for s in services])






