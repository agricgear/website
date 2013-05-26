

from fabric.api import env, run, local, settings, sudo
from fabric.operations import get
from secret import *
from fabric.operations import get
import json
import os
from os.path import basename, dirname

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


FLATPAGE_TMPL = u"""
<title>{%% blocktrans %%}%(title)s{%% endblocktrans %%} </title>
<body>{%% blocktrans %%}%(content)s{%% endblocktrans %%}
</body>
"""
def render_flatpages(json_export_file):
    pages = json.loads(open(json_export_file).read())
    for p in pages:
        page = p['fields']
        try:
            os.makedirs('templates' + dirname(page['url']))
        except OSError:
            pass
        fname = 'templates' + page['url'] + ".html"
        print "writting " + fname
        content = FLATPAGE_TMPL % { 
            'content': unicode(page['content']),
            'title': unicode(page['title'])
        }
        open(fname, 'w').write(content.encode('utf-8'))

def makemessages():
    # dump data from flatpages
    local('python manage.py dumpdata flatpages | python -mjson.tool  > /tmp/1.json')
    # render 1.json temporally pages
    render_flatpages('/tmp/1.json')
    local('django-admin.py makemessages --ignore env -l en')

def compilemessages():
    local("python manage.py compilemessages -l en")
    local("rm -rf web/locale")
    local("cp -r locale web")

    
