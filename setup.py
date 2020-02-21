# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from after_deploy import __version__

here   = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name                 = 'django-after-deploy',
    version              = __version__,
    description          = 'Automated tasks after-deploy for Django.',
    long_description     = README,
    license              = 'MIT',
    packages             = find_packages(),
    python_requires      = '>3.5.2',
    author               = 'Diogo Fernandes',
    author_email         = 'dfop02@hotmail.com',
    platforms            = ["any"],
    include_package_data = True,
    keywords             = ['django', 'task', 'tasks'],
    zip_safe             = False,
    url                  = 'https://github.com/dfop02/django-after-deploy',
    install_requires     = [
        'Django>=1.6',
    ]
)
