import datetime
import subprocess

AUTHOR = 'Marcin Panasiuk'
SITENAME = 'Marcin Panasiuk - blog'
SITEURL = "https://blog.marcinpanasiuk.com"

PATH = "content"

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/apple-touch-icon.png',
    'extra/site.webmanifest',
    'extra/android-chrome-192x192.png',
]

EXTRA_PATH_METADATA = {
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
}

THEME = 'theme'
OUTPUT_PATH = "docs"
COMMIT_ID = subprocess.check_output(['git', 'rev-parse', '--short=7', 'HEAD'], text=True).strip()
TIMESTAMP = datetime.datetime.now().replace(microsecond=0).astimezone().isoformat(' ')

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/{slug}.atom.xml'
# Disabled Atom feeds, don't need them
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'render_math', 'image_process']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

MARKDOWN = {
    'extensions': ['markdown.extensions.smarty'],
}

IMAGE_PROCESS = {
    "article-image": ["scale_in 480 380 True"],
}
