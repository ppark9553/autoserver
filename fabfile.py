'''
'pip install fabric3' with Python 3 and run locally
'''
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, hosts, get, put, sudo

from deployer.config import CONFIG
from deployer.webserver import deploy_webserver
from deployer.dbserver import deploy_dbserver
from deployer.test import DeployTester

env.hosts = [
    CONFIG['web']['ip-address'], # 0
    CONFIG['test']['ip-address'], # 1
    CONFIG['db']['ip-address'], # 2
]

env.user = 'root'

@hosts(env.hosts[0])
def auto_deploy_webserver():
    deploy_webserver()

@hosts(env.hosts[2])
def auto_deploy_dbserver():
    deploy_dbserver()

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
