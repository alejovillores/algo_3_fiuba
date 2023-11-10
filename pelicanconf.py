
# Author and Site information

AUTHOR = 'Alejo Villores'
SITENAME = 'Algoritmos y Programacion III - Catedra Suarez'
SITEURL = 'https://alejovillores.github.io/algo_3_fiuba'
GITHUB_URL = 'https://github.com/alejovillores/algo_3_fiuba'
LINKEDIN = 'https://www.linkedin.com/in/alejo-villores-0050331b9/'
PATH = 'content'

# Time and Date
TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Campus Fiuba', 'https://campusgrado.fi.uba.ar/'),)

# Social widget
# SOCIAL = (('Github', '#'),
#          ('Linkedin', '#'),)

# Pagination and Order
DEFAULT_PAGINATION = 10
PAGE_ORDER_BY = 'position'
DISPLAY_PAGES_ON_MENU = True

DELETE_OUTPUT_DIRECTORY = True

PAGE_URL = '/pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images']

THEME = 'pelican-theme'
