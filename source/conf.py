# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'spacehardwarehandbook-public'
copyright = '2025, UASAL'
author = 'UASAL'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True
numfig_format = {
    'code-block': 'Listing %s',
    'figure': 'Fig. %s',
    'section': 'Section',
    'table': 'Table %s',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# --- SETTINGS FOR REPO LINK ---

# GitHub username or organization name
github_user = "uasal"
# Repository name
github_repo = "spacehardwarehandbook-public"
# Default branch name (CHECK THIS on GitHub: usually 'main' or 'master')
github_version = "main"
# Path in the repository root where your documentation lives
# (Relative path from repo root to the directory containing conf.py)
# CHECK THIS: Use '/docs/' if conf.py is in a 'docs' folder at the root
# Use '/' if conf.py is directly in the repository root.
conf_py_path = "/source/"

html_context = {
    # Enable "Edit on GitHub" link:
    'display_github': True,
    # Provide GitHub details:
    'github_user': github_user,
    'github_repo': github_repo,
    'github_version': github_version,
    'conf_py_path': conf_py_path,
    # Set the source file suffix (for edit links)
    # 'source_suffix': _source_suffix,
}