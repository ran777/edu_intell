from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()


@register.simple_tag(name='svg_icon')
def svg_icon(icon_name, extra_class=''):
    svg_tag = format_html('<svg viewBox="0 0 24 24" class="icon-{name} {extra}">'
                          '<use xlink:href="#{name}" class="sym-{name}"></use>'
                          '</svg>', name=icon_name, extra=extra_class)

    return mark_safe(svg_tag)
