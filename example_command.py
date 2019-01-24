from fabric.api import env, roles, run, execute

env.roledefs = {
    'remote_1': ['root@192.168.1.1'],
    'remote_2': ['root@192.168.1.2'],
    'remote_3': ['root@192.168.1.3']
}

env.password = "strong"


@roles('remote_1')
def task1():
    run('echo hello 1')


@roles('remote_2')
def task2():
    run('echo hello 2')


@roles('remote_3')
def task3():
    run('echo hello 3')


def go():
    execute(3)
    execute(1)
    execute(2)
