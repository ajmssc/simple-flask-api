#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/admin/project/flaskwww/")

from app import app as application
application.secret_key = 'fefwoafkawj03jt023jaaj@!Rrok2po'