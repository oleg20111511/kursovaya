import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/var/www/kursovaya_django/kursovaya')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/kursovaya_django/venv/lib/python3.5/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kursovaya.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()