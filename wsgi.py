#!/usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'api'))
virtenv = os.environ['OPENSHIFT_HOMEDIR'] + 'python/virtualenv/venv'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(
    virtenv, 'lib/python3.3/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
