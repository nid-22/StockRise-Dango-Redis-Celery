from django import template

register = template.Library()


def get(dicti, key):
    return dicti.get(key,'')

register.filter('get',get)