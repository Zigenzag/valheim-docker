#!/bin/bash
mkdir -p /home/valheim/server
mkdir -p /home/valheim/data
mkdir -p /home/valheim/logs/archive
cp /home/valheim/valheim-docker/includes/config_template /home/valheim/valheim-docker/config
echo 'alias valheim_manage="python3 /home/valheim/valheim-docker/valheim-manage.py"' >> ~/.bashrc

docker build -t steamcmd -f docker/Dockerfile.steamcmd /home/valheim/valheim-docker