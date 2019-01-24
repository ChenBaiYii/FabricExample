#!/usr/bin/python3
# env example

from fabric.api import env
from fabric import api

env.hosts = ['localhost']


def show():
    print(f"execution on {env.host}")
    if env.host is "localhost":
        print('local')
        with api.cd("~"):
            api.local("ls -ll; uname -a; echo 'hosts env.'")
    else:
        print('remote')
        with api.cd("/"):
            api.run("uname -a")  # local test, safe
