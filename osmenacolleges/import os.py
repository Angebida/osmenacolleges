import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/osmenacolleges'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'osmenacolleges.settings'

# Activate your virtual environment
activate_this = '/home/yourusername/osmenacolleges/venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
