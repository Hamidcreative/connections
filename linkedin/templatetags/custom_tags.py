from django import template
register = template.Library()

import datetime



@register.filter
def remaining_time(value, arg=None):
    if value == None or value == '':
        return '-----'
    # today = datetime.datevalue
    # someday = datetime.date.today()
    # diff = someday - today

    return  "10 Days"


@register.filter
def active_route(request, path):
    print(request.path)
    print(path)
    if path in request.path:
        return 'elementor-item-active'
    return ''