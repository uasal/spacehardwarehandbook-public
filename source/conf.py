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

# Parameters for the linking and link checking

# linkcheck_allowed_redirects = {
# # All HTTP redirections from the source URI to
# # the canonical URI will be treated as "working".
# }

# Ignore links that are private repos or require VPN
linkcheck_ignore = [
    'https://doi.org/10.1063/1.1149739',
    'https://github.com/uasal/spacecoron_design_docs',
    'https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/*',
    'https://spie.org/publications/book/*',
    'https://www.engineeringtoolbox.com/steel-bolts-sae-grades-d_1426.html',
    'https://www.photonics.com/Articles/Cleaning_Optics_Choosing_the_Best_Method/a32199',
    'https://www.worldcat.org/title/machinerys-handbook/oclc/954734887',
]

# # Sites where the anchoring doesn't work correctly (often a redirect issue)
# linkcheck_anchors_ignore_for_url = []