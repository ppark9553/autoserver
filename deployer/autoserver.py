from fabric.api import cd, env, local, run, sudo, settings, put


class Autoserver(object):
    '''
    Autoserver wraps up basic commands needed for deploying and managing Ubuntu (Debian based) servers.
    '''

    def __init__(self, project_name, github_repo, ip_address, root_pw, user_id, user_pw, db_id, db_pw):
        # initialize Autoserver instance with github_repo, ip_address, root_pw, user_id, user_pw, db_id, and db_pw data
        # you are most likely to get these data from config.py file
        self.PROJECT_NAME = project_name
        self.GITHUB_REPO = github_repo
        self.IP_ADDRESS = ip_address
        self.ROOT_PW = root_pw
        self.USER_ID = user_id
        self.USER_PW = user_pw
        self.DB_ID = db_id
        self.DB_PW = db_pw

    ### TEST PASSED ###
    def set_root_password(self):
        run('echo -e "{0}\n{1}" | passwd root'.format(self.ROOT_PW, self.ROOT_PW))
        return True # returns True after running so DeployTester knows that the function ran

    ### TEST PASSED ###
    def create_user(self):
        run('echo -e "{0}\n{1}" | adduser {2}'.format(self.USER_PW,
                                                      self.USER_PW,
                                                      self.USER_ID))
        run('usermod -aG sudo {}'.format(self.USER_ID))
        run('groups {}'.format(self.USER_ID))
        return True

    ### TEST PASSED ###
    def start_firewall(self):
        run('sudo ufw app list')
        run('sudo ufw allow OpenSSH')
        run('echo -e "y" | sudo ufw enable')
        return True

    ### TEST PASSED ###
    def update_and_download_dependencies(self):
        run('sudo apt-get update')
        run('sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib')
        return True

    ### TEST PASSED ###
    def setup_postgresql(self):
        # open port 5432 to remote computers/servers
        run('sudo ufw allow 5432')
        # moving postgresql configuration files to server
        # this is needed to allow access from remote computers to server
        put('.\\config\\postgresql\\postgresql.conf', '/etc/postgresql/9.5/main/postgresql.conf')
        put('.\\config\\postgresql\\pg_hba.conf', '/etc/postgresql/9.5/main/pg_hba.conf')
        # start, enable and restart postgresql service
        run('sudo systemctl start postgresql.service')
        run('sudo systemctl enable postgresql.service')
        run('sudo systemctl restart postgresql.service')

        # create database table and user if they do not exist already
        with settings(warn_only=True):
            run('sudo -i -u postgres psql -c "CREATE DATABASE {};"'.format(self.DB_ID))
        with settings(warn_only=True):
            run("sudo -i -u postgres psql -c \"CREATE USER {0} WITH PASSWORD '{1}';\"".format(self.DB_ID, self.DB_PW))
        run("sudo -i -u postgres psql -c \"ALTER ROLE {} SET client_encoding TO 'utf8';\"".format(self.DB_ID))
        run("sudo -i -u postgres psql -c \"ALTER ROLE {} SET default_transaction_isolation TO 'read committed';\"".format(self.DB_ID))
        run("sudo -i -u postgres psql -c \"ALTER ROLE {} SET timezone TO 'UTC';\"".format(self.DB_ID))
        run("sudo -i -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE {0} TO {1};\"".format(self.DB_ID, self.DB_ID))
        return True

    ### TEST PASSED ###
    def setup_python_virtualenv(self):
        # download dependencies
        run('sudo -H pip3 install --upgrade pip')
        run('sudo pip3 install setuptools')
        run('sudo -H pip3 install virtualenv virtualenvwrapper')
        # configure virtualenvwrapper to load on terminal open
        run('echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc')
        run('echo "export WORKON_HOME=/home/arbiter/venv" >> ~/.bashrc')
        run('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc')
        # final step of this is to reboot server
        run('source ~/.bashrc')
        return True

    def setup_nginx_uwsgi(self):
        run('sudo apt-get install build-essential nginx')
        run('sudo -H pip3 install uwsgi')
