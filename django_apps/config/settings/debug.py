from .base import *

DEBUG = True
config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

WSGI_APPLICATION = 'config.wsgi.debug.application'

print('@@@@@@@@@@@@@@@ DEBUG: ', DEBUG)
print('@@@@@@@@@@@@@@@ ALLOWED_HOSTS: ', ALLOWED_HOSTS)