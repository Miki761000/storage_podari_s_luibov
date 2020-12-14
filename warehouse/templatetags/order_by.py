from django import template
register = template.Library()


@register.filter
def sort_by(queryset):
    return queryset.order_by('Ascending')