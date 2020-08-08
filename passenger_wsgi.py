import os, sys
sys.path.insert(0, '/var/www/u1108756/data/www/avagro.fun/avagro')
sys.path.insert(1, '/var/www/u1108756/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'avagro.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
