from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
SENTRY_DSN = 'http://3e6ecca5bf88469faf23bb3a56f336f1:ef01914c847547ecb6c9fcd176be6128@sentry.otree.org/332'
SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'my_first_app',
        'display_name': "my_first_app",
        'num_demo_participants': 1,
        'app_sequence': ['my_first_app'],
    },
    {
        'name': 'guessgame',
        'display_name': "guessgame",
        'num_demo_participants': 1,
        'app_sequence': ['guessgame'],
    },
    {'name': 'dg_baseline',
     'display_name': "dictator game - baseline",
     'num_demo_participants': 2,
     'app_sequence': ['dictator_game'],
     'treatment_gender': False,
     },
    {'name': 'dg_gender',
     'display_name': "dictator game - gender info treatment",
     'num_demo_participants': 2,
     'app_sequence': ['dictator_game'],
     'treatment_gender': True,
     },
    {'name': 'ultimatum_game',
     'display_name': "ultimatum_game",
     'num_demo_participants': 2,
     'app_sequence': ['ultimatum_game'],
     },
    {'name': 'political_views',
     'display_name': "political_views",
     'num_demo_participants': 1,
     'app_sequence': ['political_views'],
     },
    {'name': 'charities',
     'display_name': "charities",
     'num_demo_participants': 1,
     'app_sequence': ['charities'],
     },
    {'name': 'public_goods',
     'display_name': "public goods game",
     'num_demo_participants': 4,
     'app_sequence': ['public_goods'],
     },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CHF'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'ECUs'
ROOMS = []

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '^(3+4^6s^(c-a%wwjg*i^=b+h3a8dzyua+f@_pqq&r#4a)!xo^'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
