#!/usr/bin/env python
from __future__ import print_function
import os
import sys

if __name__ == "__main__":
    print('******************************************************')
    print('** If you see this message, something is wrong!     **')
    print('** This copy of manage.py should have been replaced **')
    print('** by Salt during deployment.  Did you _use_ Salt?? **')
    print('******************************************************')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
