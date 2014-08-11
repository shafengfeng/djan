__author__ = 'shafengfeng'
# -*- coding: utf-8 -*-
from django.conf import settings
settings.configure()

from django import template

t=template.Template("<html><body>It is now {{current_date}}.</body></html>")
