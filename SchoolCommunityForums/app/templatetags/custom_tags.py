

#自定义模板
#1)templatetags folder
#2) @register.filter(name='split')
#3) html add {% load custom_tags %}
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
@register.filter(name='split')
def split(value, arg):
    split_result = []
    try:
        [split_result.append(item) for item in value.split(arg) if item != '']
    except Exception as e :
        pass
    return split_result


@register.filter(name='splitone')
def split(value, arg):
    split_result = value.split(arg)
    if len(split_result) > 0:
        lists = []
        lists.append(split_result[0])
        split_result = lists
    else:
        pass
    return split_result

@register.filter(name='splitlastthree')
def split(value, arg):
    split_result = value.split(arg)
    if len(split_result) > 0:
        lists = []
        lists.append(split_result[1])
        lists.append(split_result[2])
        lists.append(split_result[3])        
        split_result = lists
    else:
        pass
    return split_result