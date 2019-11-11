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

@register.inclusion_tag('base.html', takes_context=True)
def current_page(context):
    request = context['request']
    path = request.get_full_path
    return   path
