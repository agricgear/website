

from fabric.api import env, run, local, settings, sudo
from fabric.operations import get
from secret import *
from fabric.operations import get

def production():
  env.hosts = ['track.agroguia.es:2223']
  env.user = 'fabric'
  env.password = BOT_PASS
  env.deploy_folder = '/home/fabric/agroguia-website'

def copy_database():
  get("%(deploy_folder)s/dev.sqlite" % env)

def deploy_web():
  run("cd %(deploy_folder)s && ./deploy/stop.sh" % env)
  run("cd %(deploy_folder)s && cp dev.sqlite dev.sqlite.bak" % env)
  run("cd %(deploy_folder)s && git pull" % env)
  run("cd %(deploy_folder)s && ./env/bin/python manage.py collectstatic --noinput" % env)
  sudo("cp %(deploy_folder)s/cron/agricgear-website /etc/cron.d/" % env)
  run("cd %(deploy_folder)s && ./env/bin/pip install -r requirements.txt" % env)
  run("cd %(deploy_folder)s && ./deploy/start.sh" % env)

def backup():
    copy_database()
    
