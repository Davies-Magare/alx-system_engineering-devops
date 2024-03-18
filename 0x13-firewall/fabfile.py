#!/usr/bin/python3
from fabric.api import *
from fabric.operations import put

# Define the host IP and SSH key file path in the env dictionary
env.hosts = ['100.26.174.14']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

# Define a Fabric task to send a file to the remote host
def send_file(file_path):
    # Upload the file to the remote host
    put('{}'.format(file_path))
    run('chmod u+x {}'.format(file_path))
    sudo('./{}'.format(file_path))

