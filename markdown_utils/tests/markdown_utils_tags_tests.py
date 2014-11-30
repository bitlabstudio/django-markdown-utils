"""Tests for the templatetags of the markdown_utils app."""
from django.test import TestCase

from ..templatetags import markdown_utils_tags as tags


class RenderMarkdownTestCase(TestCase):
    """Tests for the ``render_markdown`` assignment tag."""
    longMessage = True

    def test_tag(self):
        result = tags.render_markdown('# Foobar')
        self.assertEqual(result, '<h1>Foobar</h1>', msg=(
            'Should render the given input correctly.'))

        result = tags.render_markdown('Foobar\nBarfoo')
        self.assertEqual(result, '<p>Foobar<br />\nBarfoo</p>', msg=(
            'Should render the given input correctly.'))
