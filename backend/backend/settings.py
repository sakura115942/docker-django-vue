import os


environment = os.environ.get('environment', 'develop')

if environment == 'production':
    from .settings_prod import *
else:
    from .settings_dev import *
