#!/usr/bin/env bash
# Script for to configure the web-servers fordeployment wed statics
apt-get update
apt-get install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\talias\t/data/web_static/current/;\n\tautoindex off;\n\t}' /etc/nginx/sites-available/default
service nginx restart