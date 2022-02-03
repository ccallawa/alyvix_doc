# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
import time
current_year = time.strftime('%Y')
sys.path.append(os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------

project = 'Alyvix User Guide'
copyright = '&copy;2020-%s, Wuerth Phoenix S.r.l.' %(current_year)
author = 'Charles Callaway'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'3.2.3'
# The full version, including alpha/beta/rc tags.
release = u'3.2.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_copybutton',       # pip install sphinx-copybutton
    #'sphinx_rtd_theme',        # pip install sphinx-rtd-theme
    'sphinx_panels',           # The panels/tabs/dropdown/link-button theme
    'iconlink'                 # Our custom theme for links with embedded icons at _ext/iconlink.py
]
#    'sphinx.ext.mathjax'
#    'rinoh.frontend.sphinx'  # pip install rinohtype

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_themes/neteye/templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '_ext', 'pictures']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
todo_link_only = False

# If true, the `numfig` option will produce numbered labels
# Also:  `numfig_format`, `numfig_secnum_depth`
numfig = True
numfig_secnum_depth = 0


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'neteye'
html_theme_path = ["_themes"]

# Options for the Read the Docs (rtd) theme.
html_theme_options = { }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_additional_pages = {'index': 'index.html'}

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css'
    #'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
]

# html_js_files = [
#     'js/custom.js',
# ]

html_title = "%s" %(project)
html_logo = 'pictures/alyvix_icon_white_100x100.png'
html_favicon = 'pictures/alyvix_icon_100x107.png'

html_output_encoding = 'utf-8'

# Output file base name for HTML help builder.
htmlhelp_basename = 'AlyvixUserGuidedoc'
