"""
WSGI config for sandd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandd.settings")

from django.core.wsgi import get_wsgi_application
=======
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandd.settings")

>>>>>>> 8052b7ec016c37e91a9217b06d5337059ac7581f
application = get_wsgi_application()
