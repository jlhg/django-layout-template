import os
import sys

# Please replace project_name with your project_name
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# Please mofiy /path/to/project_root to your project path
path = '/path/to/project_root'
if path not in sys.path:
    sys.path.append(path)
