# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from after_deploy import get_version

here   = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name                 = 'django-after-deploy',
    version              = get_version(),
    description          = 'Automated tasks after-deploy for Django.',
    long_description     = README,
    license              = 'MIT',
    packages             = find_packages(),
    python_requires      = '>=3.6',
    author               = 'Diogo Fernandes',
    author_email         = 'dfop02@hotmail.com',
    platforms            = ['any'],
    include_package_data = True,
    keywords             = ['django', 'deploy', 'task', 'tasks'],
    zip_safe             = False,
    url                  = 'https://github.com/dfop02/django-after-deploy',
    download_url         = f'https://github.com/dfop02/django-after-deploy/archive/v{get_version()}.tar.gz',
    classifiers          = [
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires     = [
        'Django>=1.6',
    ]
)
