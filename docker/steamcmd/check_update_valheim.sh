#/bin/bash
./steamcmd.sh +login anonymous +app_info_update 1 +app_info_print 896660 +quit | grep "AppID : 896660"