# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
        @Author yuxiankai
        @Date 2022/10/13 16:38
        @Describe 
        @Version 1.0
    """

from .base import * # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}