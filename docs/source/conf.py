# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys


# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath("../../"))
sys.path.append(os.path.abspath("extensions"))


# -- Project information -----------------------------------------------------

project = "nhentaio"
copyright = "2020-Present, Kaylynn234"
author = "Kaylynn234"


# The full version, including alpha/beta/rc tags
with open("../../nhentaio/__init__.py") as f:
    match = re.search(r'__version__ = "([\d\.]+)"', f.read(), re.MULTILINE)
    assert match
    version = match[1]


master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "builder",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "details",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

pygments_style = "friendly"

autodoc_member_order = "bysource"

master_doc = "index"

napoleon_google_docstring = False
