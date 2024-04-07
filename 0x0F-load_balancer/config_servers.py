#!/usr/bin/python3
"""Create and Distribute archive to remote web servers."""

from fabric.api import env, put, run, sudo
import os


env.user = 'ubuntu'
env.key_filename = "/home/vagrant/.ssh/school"
env.hosts = ['52.87.154.26']  # Define multiple hosts

def check():
    run('put 1-install_load_balancer')
    run('sudo ./1-install_load_balancer')
