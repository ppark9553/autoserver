'''
Configuration .py file for Autoserver.
Following the dictionary convention of setting configuration files.
CONFIG dict will take server names as its key values,
each key value will take on its own key values, which are:

(project-name,
github-repo,
ip-address,
root-pw,
user-id,
user-pw,
db-id,
db-pw,
uwsgi-ini,
uwsgi-service,
nginx-conf,
supervisor-celery,
supervisor-celerybeat)

you can also add other key values to use in the program
'''

CONFIG = {
    # ar_web_server
    'web': {
        'project-name': 'buzzz',
        'github-repo': 'https://github.com/ppark9553/our-web-server.git',
        'ip-address': '207.148.103.151',
        'root-pw': 'makeitpopwear!1',
        'user-id': 'arbiter',
        'user-pw': 'projectargogo!',
        'db-id': 'arbiter',
        'db-pw': 'projectAR!gogo',
        'uwsgi-ini': 'buzzz.ini',
        'uwsgi-service': 'uwsgi.service',
        'nginx-conf': 'buzzz.conf',
        'supervisor-celery': 'celery.conf',
        'supervisor-celerybeat': 'celerybeat.conf'
    },

    'db': {
        'project-name': 'buzzz',
        'github-repo': 'https://github.com/ppark9553/our-web-server.git',
        'ip-address': '45.77.134.175',
        'root-pw': 'makeitpopwear!1',
        'user-id': 'arbiter',
        'user-pw': 'projectargogo!',
        'db-id': 'arbiter',
        'db-pw': 'projectAR!gogo',
        'uwsgi-ini': 'buzzz.ini',
        'uwsgi-service': 'uwsgi.service',
        'nginx-conf': 'buzzz.conf',
        'supervisor-celery': 'celery.conf',
        'supervisor-celerybeat': 'celerybeat.conf'
    },

    'gobble': {
    },

    # ar_test_server
    'test': {
        'project-name': 'buzzz',
        'github-repo': 'https://github.com/WeareArbiter/Arbiter-Keystone-BuzzzLightYear.git',
        'ip-address': '207.148.103.151',
        'root-pw': 'makeitpopwear!1',
        'user-id': 'arbiter',
        'user-pw': 'projectargogo!',
        'db-id': 'arbiter',
        'db-pw': 'projectAR!gogo',
        'uwsgi-ini': 'buzzz.ini',
        'uwsgi-service': 'uwsgi.service',
        'nginx-conf': 'buzzz.conf',
        'supervisor-celery': 'celery.conf',
        'supervisor-celerybeat': 'celerybeat.conf'
    }
}
