from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, settings
from fabric.operations import open_shell

from .autoserver import Autoserver
from .config import CONFIG

conf = CONFIG['arbiter-web']

def deploy_webserver():
    # deploys webserver using Autoserver instance with 'arbiter-web' data
    autoserver = Autoserver(conf['project-name'],
                            conf['github-repo'],
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
    autoserver.setup_postgresql()
    autoserver.setup_python_virtualenv()
    # create virtualenv directly
    run('echo "Python virtualenv cannot be created with fabric, please type in (mkvirtualenv [project name])"')
    open_shell() # mkvirtualenv {project name}
    autoserver.setup_nginx_uwsgi()
