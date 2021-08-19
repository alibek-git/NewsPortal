from django import template

register = template.Library()


censor_list = ['фбк', 'мбх']
replacement_word = '(данные удалены)'


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, replacement_word)
    return value
