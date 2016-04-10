from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def number(n):
	if n[0] == '-':
		return n[1:].isdigit()
	return n.isdigit()