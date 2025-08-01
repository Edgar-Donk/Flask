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
# sys.path.insert(0, os.path.abspath('./scripts/'))
# sys.path.insert(0, os.path.abspath('../../src'))

# The master toctree document.
master_doc = 'index'
# -- Project information -----------------------------------------------------

project = "Flask"
copyright = '2025, edga donk'
author = 'edga donk'

# The full version, including alpha/beta/rc tags
release = '0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc",
    'sphinx.ext.napoleon',
    "sphinx.ext.autosummary",
    "sphinx_carousel.carousel",
    "sphinx_design",
    # "numpydoc",
    #'sphinx.ext.mathjax',
    'sphinx_copybutton',
    #'matplotlib.sphinxext.plot_directive',
    #'sphinx_exec_code',
    #'sphinx.ext.duration',
    #'sphinx.ext.doctest',
]

#carousel_show_fade = True
#carousel_show_captions_below = True
#carousel_show_dark = True
#carousel_show_buttons_on_top = True
#carousel_show_indicators = True

napoleon_google_docstring = False
napoleon_numpy_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
  "show_prev_next": True,
  # search bar options are ‘navbar’ and ‘sidebar’.
  "search_bar_position": "sidebar",
  #  "use_edit_page_button": True,

}

html_sidebars = {
'''    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html'

    ]
'''
    "contributing": ["sidebar-search-bs.html", "custom-template.html"],
    "changelog": [],
}

# option for show/hide code
def setup(app):
    app.add_css_file('custom.css') # stylesheet

#html_logo = "_static/ben2.png"

html_theme_options = {
   "logo": {
      "text": "Flask",
      "image_light": 'bigbenc.png',
      "image_dark": "bigbencneon.png",
   }
}

html_favicon = '_static/ben1.ico'