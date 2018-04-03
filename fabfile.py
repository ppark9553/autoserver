'''
'pip install fabric3' with Python 3
and run locally
'''
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, hosts, get

from deployer.config import CONFIG
# from deployer.webserver import deploy_webserver

# env.hosts = [
#     CONFIG['arbiter-web']['ip-address'], # 0
# ]

env.hosts = ['45.32.59.138']

env.user = 'root'
# env.host = CONFIG['arbiter-web']['ip-address']

REPO_URL = 'https://github.com/WeareArbiter/Arbiter-Keystone-BuzzzLightYear.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        run('pwd')

# @hosts(env.hosts[0])
# def auto_deploy_webserver():
#     deploy_webserver()

def say_fuck_you():
    run('mkdir /home/fuckyou')

def backup_secret_file():
    get(remote_path="/home/fuckyou/secret.txt", local_path="C:\\Users\\hori9\\Desktop\\secret.txt")
    local('cd C:\\Users\\hori9\\Desktop')
    local('more C:\\Users\\hori9\\Desktop\\secret.txt')
