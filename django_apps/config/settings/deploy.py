from .base import *

DEBUG = False
config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

WSGI_APPLICATION = 'config.wsgi.deploy.application'


print('@@@@@@@@@@@@@@@ DEBUG: ', DEBUG)
print('@@@@@@@@@@@@@@@ ALLOWED_HOSTS: ', ALLOWED_HOSTS)