#!/bin/bash
export temp_ldpath=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/valheim/linux64:$LD_LIBRARY_PATH
export SteamAppId=892970

LOGFILE="${LOGDIR}/server.log"
LOGFILEARCHIVE="${LOGDIR}/archive/server_$(date +'%Y-%m-%d_%H-%M').log"

mkdir -p /valheim-data/log_archive
/valheim-server/valheim_server.x86_64 -nographics -batchmode -name "$SERVER_NAME" -port "$SERVER_PORT" -world "$SERVER_WORLD" -password "$SERVER_PASSWORD" -savedir "$DATADIR" -logfile "$LOGFILE"
cp "$LOGFILE" "$LOGFILEARCHIVE"

export LD_LIBRARY_PATH=$temp_ldpath
