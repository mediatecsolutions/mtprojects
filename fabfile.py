import getpass
from fabric.api import sudo, cd, env, task, prompt
from fabric.context_managers import shell_env
import subprocess


class Site(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def run(self, cmd, directory=None):
        directory = directory or self.dir
        with cd(directory):
            with shell_env(HOME=self.HOME):
                sudo(cmd, user=self.user_id)

    def sudo(self, cmd, directory=None):
        directory = directory or self.dir
        with cd(directory):
            with shell_env(HOME=self.HOME):
                sudo(cmd)

    def deploy(self):
        self.git_pull()
        self.update_packages()
        self.run('venv/bin/python manage.py syncdb')
        self.run('venv/bin/python manage.py collectstatic --noinput --clear')
        self.restart()

    def git_pull(self):
        self.run("git reset --hard && git checkout master && git pull")

    def update_packages(self):
        self.run("./venv/bin/pip install -r requirements.txt")

    def restart(self):
        self.run("touch reload")

SITES = {
    'prod': Site(
        dir='/home/mt-web/mtprojects/',
        user_id='mt-web',
        HOME='/home/mt-web/',
        host='prosjekt.mtserver.no',
    ),

}


@task
def prod():
    env.hosts = ['prosjekt.mtserver.no']
    env.site = SITES['prod']


@task
def deploy():
    """
    Deploys current git master to a given site
    """
    get_username()
    env.site.deploy()


@task
def restart():
    get_username()
    env.site.restart()


def get_username():
    env.user = prompt("Username on %s server:" % env.site.host,
                      default=getpass.getuser())
