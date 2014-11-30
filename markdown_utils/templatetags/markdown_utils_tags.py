"""Templatetags for the markdown_utils app."""
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


register = template.Library()


@register.assignment_tag
@stringfilter
def render_markdown(content):
    """
    Renders a markdown string into it's HTML representation.

    :param content: String representing the Markdown representation of the
      content to be rendered to HTML.

    """
    extensions = ['nl2br', ]
    return mark_safe(markdown.markdown(force_unicode(content), extensions))
