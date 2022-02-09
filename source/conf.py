

project = 'TM ROS'
copyright = '2022, Techman Robot Inc'
author = 'Techman Robot Inc'

# The full version, including alpha/beta/rc tags
release = 'v1'


templates_path = ['_templates']

#extensions = [
#]

extensions = [
    'recommonmark',
    'sphinx_markdown_tables'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_favicon = '_static/favicon.png'
html_logo = '_static/logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
#html_context = {
#    'css_files': [
#        '_static/style_override.css.css',
#        ],
#     }
