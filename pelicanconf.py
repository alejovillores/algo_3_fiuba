
# Author and Site information

AUTHOR = 'Alejo Villores'
SITENAME = 'Algoritmos y Programacion III - Catedra Suarez'
SITEURL = ''
GITHUB_URL = 'https://github.com/alejovillores'
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
# LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

# Pagination and Order
DEFAULT_PAGINATION = 10
PAGE_ORDER_BY = 'position'
DISPLAY_PAGES_ON_MENU = True

DELETE_OUTPUT_DIRECTORY = True

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# STATIC_PATHS = [
#    'images',
#    'extra/robots.txt',
#    ]

THEME = 'Peli-Kiera'
