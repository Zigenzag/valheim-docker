import os, argparse, re

class BaseClass:

    def _invoke(self, command: str):
        stream = os.popen(command)
        return stream.read()

class SteamCMD(BaseClass):
    
    def check_update(self):
        output = self._invoke(f'docker run --rm -i steamcmd /bin/bash /home/steam/steamcmd/check_update_valheim.sh')
        output = output.split(',')
        return re.search('([0-9]*)/', output[1]).group(1)
    
    def update(self):
        return self._invoke(f'docker run -i steamcmd -v /home/valheim/server:/home/steam/valheim-server /bin/bash /home/steam/steamcmd/update_valheim.sh --rm')

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
        print( self._invoke('docker-compose -f /home/valheim/valheim-docker/docker up --detach') )

    def stop(self):
        print( self._invoke('docker-compose -f /home/valheim/valheim-docker/docker down') )
    
    def backup(self):
        pass

if __name__ == '__main__':
    manager = ValheimManage()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--upgrade", help="Upgrade Valheim Server", action="store_true")
    parser.add_argument("--backup", help="Backup Valheim Server", action="store_true")
    parser.add_argument("--start", help="Start Valheim Server", action="store_true")
    parser.add_argument("--stop", help="Stop Valheim Server", action="store_true")
    args = parser.parse_args()

    if args.upgrade:
        manager.update()
    elif args.backup:
        manager.backup()
    elif args.start:
        manager.start()
    elif args.stop:
        manager.stop()