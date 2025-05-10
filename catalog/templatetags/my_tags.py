from django import template

register = template.Library()


@register.filter
def media_path(path):
    if path:
        return f"/media/{path}"
    return ""
