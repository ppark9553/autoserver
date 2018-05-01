'''
'pip install fabric3' with Python 3 and run locally
'''
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, hosts, get, put, sudo

from deployer.config import CONFIG
from deployer.webserver import deploy_webserver
from deployer.test import DeployTester

env.hosts = [
    CONFIG['arbiter-web']['ip-address'], # 0
    CONFIG['test']['ip-address'], # 1
]

env.user = 'root'

REPO_URL = 'https://github.com/WeareArbiter/Arbiter-Keystone-BuzzzLightYear.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        run('pwd')

@hosts(env.hosts[0])
def auto_deploy_webserver():
    deploy_webserver()

def test(tester, func_name):
    # wrapper for testing DeployTester methods
    print('Testing: {}'.format(func_name))
    passed_count, failed_status = getattr(tester, func_name)() # a way to run python methods using its string name value
    if failed_status != True:
        print('Total test passed: {}'.format(passed_count))

### Test function for Autoserver class
@hosts(env.hosts[1])
def test_deploy():
    tester = DeployTester()
    # first get all DeployTester method names containing 'test' in the front
    test_funcs = [func_name for func_name in dir(tester) if 'test' in func_name]
    print('Testing: ' + ', '.join(test_funcs))

    for test_func in test_funcs:
        test(tester, test_func)
