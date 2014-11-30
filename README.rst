Django Markdown Utils
=====================

A reusable Django app with some useful markdown utilities.

This should mainly serve as an alternative to the `django.contrib.markup`
module which has been removed in Django 1.5.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-markdown-utils

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-markdown-utils.git#egg=markdown_utils

TODO: Describe further installation steps (edit / remove the examples below):

Add ``markdown_utils`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'markdown_utils',
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load markdown_utils_tags %}

Templatetags
------------

render_markdown
+++++++++++++++

Usage:

.. code-block:: html

    {% render_markdown some_text as markdown_text %}
    {% render_markdown some_text is_safe=True as markdown_text %}
    {{ markdown_text }}

Renders some given Markdown text to it's HTML representation.

Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-markdown-utils
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
