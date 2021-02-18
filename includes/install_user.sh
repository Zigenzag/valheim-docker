#!/bin/bash
mkdir -p /home/valheim/server
mkdir -p /home/valheim/data
mkdir -p /home/valheim/logs/archive
cp /home/valheim/valheim-docker/includes/config_template /home/valheim/config
echo 'alias valheim_manage="python3 /home/valheim/valheim-docker/python/valheim-manage.py' >> ~/.bashrc