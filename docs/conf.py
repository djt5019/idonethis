#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import datetime

from idoneit-cli import __version__

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

project = 'idoneit-cli'
copyright = '{0.year}, Dan Tracy'.format(datetime.datetime.now())
version = release =__version__

needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = []
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
pygments_style = 'sphinx'
html_static_path = []
exclude_patterns = []

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
}
