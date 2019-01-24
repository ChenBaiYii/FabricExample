#!/usr/bin/python3
# fabric hello

from fabric.api import local, settings, abort, cd, run
from fabric.contrib.console import confirm


def hello(name="world"):
    print("hello {}".format(name))


def test():
    with settings(warn_only=True):  # warn_only 把退出换为警告
        result = local('py -c "import os; print(os.getcwd())"')  # local 本地执行命令
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")  # 手动停止任务


def cd_cmd():
    code_dir = '~'
    with settings(warn_only=True):
        if run("test -d {}".format(code_dir)).failed:
            run(f"git clone user@vcshost:/path/to/repo/.git {code_dir}")
    with cd(code_dir):
        run('ls .')  # 在远程执行命令api
