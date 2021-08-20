from django import template

register = template.Library()


censor_list = ['фбк', 'мбх']
replacement_word = '(данные удалены)'


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, replacement_word)
    return value


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()
