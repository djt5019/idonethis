#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sphinx_rtd_theme

from idonethis import __version__

project = 'idonethis'
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
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = []
exclude_patterns = []

intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'tornado': ('http://tornadoweb.org/en/latest/', None),
}
