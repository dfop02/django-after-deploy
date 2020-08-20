__version__ = '0.0.2'
default_app_config = 'after_deploy.apps.AfterDeployConfig'
from after_deploy import *

def get_version():
    return __version__
