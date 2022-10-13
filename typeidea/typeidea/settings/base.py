# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
        @Author yuxiankai
        @Date 2022/10/13 16:37
        @Describe 
        @Version 1.0
    """

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True