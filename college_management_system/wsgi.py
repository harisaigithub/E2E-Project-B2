"""
WSGI config for college_management_system project.

It exposes the WSGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Check if the settings module is properly named and matches your directory structure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_management_system.settings')

# If you need to import anything related to NexuSmart, make sure it's correctly set up.
# Double-check if NexuSmart is necessary, and if not, remove any references.
# If you need NexuSmart, install it or add it to your project directory.

application = get_wsgi_application()
