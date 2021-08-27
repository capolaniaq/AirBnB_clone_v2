#!/usr/bin/python3
"""Fabric script that generates a
.tgz archive from the contents of the web_static folder"""

from datetime import datetime
import os
from fabric.api import run


def do_pack():
    date = datetime.strftime("%Y%m%d%H%M%S")
    file_tar = 'web_static_{}.tgz'.format(date)
    try:
        run('mkdir -p versions')
        run('tar -cvzf {} ~/AirBnB_clone_v2/web_static/'.format(file_tar))
        run('mv {} ~/versions'.format(file_tar))
    except:
        return None
