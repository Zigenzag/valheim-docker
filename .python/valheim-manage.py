from includes.steamcmd import SteamCMD
import sys, os

class ValheimManage:
    def update(self):
        continue_update = False
        steamcmd = SteamCMD()
        change_number = steamcmd.check_update()

        with open('/home/valheim/server/version', 'r') as filehandle:
            change_file = filehandle.read()
            if change_number == change_file:
                continue_update = True

        if continue_update:
            steamcmd.update()
            with open('/home/valheim/server/version', 'w') as filehandle:
                filehandle.write(change_number)
    
    def backup(self):
        pass

if __name__ == '__main__':
    manager = ValheimManage()
    if "update" in sys.argv:
        manager.update()
    elif "backup" in sys.argv:
        manager.backup()