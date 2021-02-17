from includes.steamcmd import SteamCMD
from includes.baseclass import BaseClass
import os, sys

class ValheimManage(BaseClass):

    def _invoke(self, command: str):
        stream = os.popen(command)
        return stream.read()

    def update(self):
        continue_update = False
        steamcmd = SteamCMD()
        change_number = steamcmd.check_update()

        with open('/home/valheim/server/version', 'r') as filehandle:
            change_file = filehandle.read()
            if change_number == change_file:
                continue_update = True

        if continue_update:
            self.stop()
            steamcmd.update()
            with open('/home/valheim/server/version', 'w') as filehandle:
                filehandle.write(change_number)
            self.start()
    
    def start(self):
        print( self._invoke('cd /home/valheim/valheim-docker/docker && docker-compose up --detach') )

    def stop(self):
        print( self._invoke('cd /home/valheim/valheim-docker/docker && docker-compose down') )
    
    def backup(self):
        pass

if __name__ == '__main__':
    manager = ValheimManage()
    if "update" in sys.argv:
        manager.update()
    elif "backup" in sys.argv:
        manager.backup()