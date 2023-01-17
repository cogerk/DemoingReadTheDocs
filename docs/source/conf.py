# Configuration file for the Sphinx documentation builder.

# -- Project information

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'demoingreadthedocs'
copyright = 'Amyris'
author = 'Mel, Kathryn'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo', 
    'sphinx.ext.viewcode', 
    'sphinx.ext.autodoc',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
autosummary_generate=True
master_doc = 'index'
