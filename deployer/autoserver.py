from fabric.api import cd, env, local, run


class Autoserver(object):

    def __init__(self, github_repo, ip_address, root_pw, user_id, user_pw, db_id, db_pw):
        self.GITHUB_REPO = github_repo
        self.IP_ADDRESS = ip_address
        self.ROOT_PW = root_pw
        self.USER_ID = user_id
        self.USER_PW = user_pw
        self.DB_ID = db_id
        self.DB_PW = db_pw

    def set_root_password(self):
        run('echo -e "{0}\n{1}" | passwd root'.format(self.ROOT_PW, self.ROOT_PW))

    def create_user(self):
        run('echo -e "{0}\n{1}" | adduser {2}'.format(self.USER_PW,
                                                      self.USER_PW,
                                                      self.USER_ID))
        run('usermod -aG sudo {}'.format(self.USER_ID))
        run('groups {}'.format(self.USER_ID))

    def start_firewall(self):
        run('sudo ufw app list')
        run('sudo ufw allow OpenSSH')
        run('su -c "y" | sudo ufw enable')

    def update_and_download_dependencies(self):
        run('sudo apt-get update')
        run('sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib')

    def setup_postgresql(self):
        # create database and user
        run('su -c "psql -c \"CREATE DATABASE {};\"" postgres'.format(self.DB_ID))
        run('su -c "psql -c \"CREATE USER {0} WITH PASSWORD \'{1}\';\"" postgres'.format(self.DB_ID, self.DB_PW))
        run('su -c "psql -c \"ALTER ROLE {} SET client_encoding TO \'utf8\';\"" postgres'.format(self.DB_ID))
        run('su -c "psql -c \"ALTER ROLE {} SET default_transaction_isolation TO \'read committed\';\"" postgres'.format(self.DB_ID))
        run('su -c "psql -c \"ALTER ROLE arbiter SET timezone TO 'UTC';\"" postgres')
