#coding:utf-8
from django import template

register = template.Library()

@register.filter()
def isdig(value):
    """проверка на соответствие числу"""
    return  value.replace('.','').replace('-','').isdigit()
