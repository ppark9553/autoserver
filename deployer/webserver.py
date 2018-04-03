from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, settings

from .autoserver import Autoserver
from .config import CONFIG

conf = CONFIG['arbiter-web']

def deploy_webserver():
    autoserver = Autoserver(conf['github-repo'],
                            conf['ip-address'],
                            conf['root-pw'],
                            conf['user-id'],
                            conf['user-pw'],
                            conf['db-id'],
                            conf['db-pw'])
    autoserver.set_root_password()
    with settings(warn_only=True):
        autoserver.create_user()
    autoserver.start_firewall()
    autoserver.update_and_download_dependencies()
