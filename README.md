website
=======

This is our website, nothing really to see here that you cant see on the actual website


## INSTALL

create virtualenv and install requirements

```base
virtualenv e
. e/bin/activate
pip install -r requirements.txt
```

create default secret file with passwords

```
echo "MAIL_PASS = 'YOURPASS'" > app/secret.py
```

create the database
```
python manage.py syncdb
python manage.py migrate
```

run the app

```
python manage.py runserver
```

## production commands

In order to run these commands you need to create a secret.py file containing ssh password for
`fabric` user, like.

```
echo "BOT_PASS = 'YOURPASS'" > secret.py
```

**commands** 

Install on production (assumes you have python/pip/virtualenv/git)

```
fab production install
```

deploy

```
fab production deploy_web
```

make a backup (copies the database to local)

```
fab production backup
```

