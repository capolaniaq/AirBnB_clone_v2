#!/usr/bin/python3
"""Fabric script that generates a
.tgz archive from the contents of the web_static folder"""

from datetime import datetime
from fabric.api import run, local


def do_pack():
    """Function that generate the tgz file"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_tar = 'versions/web_static_{}.tgz'.format(date)
    local('mkdir -p versions')
    try:
        local('tar -cvzf {} ~/AirBnB_clone_v2/web_static/'.format(file_tar))
        return file_tar
    except:
        return None
