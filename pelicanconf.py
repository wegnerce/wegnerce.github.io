#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### Basic info ####
AUTHOR = u'Carl-Eric Wegner'
SITENAME = u'Exploring Microbes'
HIDE_SITENAME = True
SITEURL = ''

###############################################################

### Paths / Plugins ###
STATIC_PATHS = ['images', 'extra', 'extra/custom.css', 'pages']
#STATIC_PATHS = ['pages/images', 'extra']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/css/custom.css'}
}

PATH = 'content'
PLUGIN_PATHS = ["/home/cewegner/Dropbox/exploring_microbes/pelican-plugins"]
PLUGINS = ['i18n_subsites']

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
I18N_TEMPLATES_LANG = 'en'

###############################################################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

###############################################################

### Custom theming ###
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = "sandstone"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_FLUID = False

SITELOGO = "images/logo.png"
SITELOGO_SIZE = "125"
FAVICON = "images/favicon.png"

###############################################################

### Navbar ###

#CUSTOM_CSS = 'theme/css/custom.css'
CUSTOM_CSS = 'extra/custom.css'
#CUSTOM_CSS = 'static/custom.css'
BOOTSTRAP_NAVBAR_INVERSE = False

### Sidebar ###

ABOUT_ME = "I'm a <strong>microbiologist</strong> with a <strong> diverse background </strong>. My passion is learning more about <strong> unknown microbial physiology </strong> and my main research interest is <strong> lanthanide utilization in bacteria </strong>."
AVATAR = "images/avatar_2020.jpg"
HIDE_SIDEBAR = True

# Twitterfeed
TWITTER_USERNAME = "wegnerce"
TWITTER_WIDGET_ID = ""

# Links
LINKS = (('Friedrich Schiller University Jena', 'https://www.uni-jena.de'),
         ('The Küsel Lab', 'https://www.bio.uni-jena.de/en/kuesellab'),
         ('CRC AquaDiva', 'https://www.aquadiva.uni-jena.de/'),
         ('CRC ChemBioSys', 'https://chembiosys.de/en/'),
         ('Balance of the Microverse', 'https://www.microverse-cluster.de/en/'))

# Social widget
SOCIAL = (('Mail', 'mailto:carl-eric.wegner@uni-jena.de', 'envelope'),('github', 'https://github.com/wegnerce', 'github'))

################################################################

### Save pages, articles ###

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

DEFAULT_PAGINATION = 10

#################################################################

### Analytics, Comments ###

DISQUS_SITENAME = "exploring-microbes"
DISQUSURL = "http://www.exploringmicrobes.de/blog/"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True 
