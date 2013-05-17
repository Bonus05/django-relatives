#!/usr/bin/env python
import sys
from os.path import abspath, dirname

from django.conf import settings


sys.path.insert(0, abspath(dirname(__file__)))


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.auth',
            'relatives',
            'relatives.tests',
            'django.contrib.admin',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        ROOT_URLCONF='relatives.tests.urls',
        STATIC_URL='/static/',
    )


def runtests():
    from django.test.simple import DjangoTestSuiteRunner
    failures = DjangoTestSuiteRunner(failfast=False).run_tests(['tests'])
    sys.exit(failures)


if __name__ == "__main__":
    runtests()
