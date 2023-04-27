#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['34.224.3.157', '54.210.134.30']
env.user = "ubuntu"


def do_clean(number=0):
    """ Cleans out-of-date archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
