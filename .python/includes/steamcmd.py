import os, re

class SteamCMD:

    def invoke(self, command: str):
        stream = os.popen(command)
        return stream.read()
    
    def check_update(self):
        output = self.invoke(f'docker run --rm -i steamcmd /bin/bash /home/steam/steamcmd/check_update_valheim.sh')
        output = output.split(',')
        return re.search('([0-9]*)/', output[1]).group(1)
    
    def update(self):
        return self.invoke(f'docker run --rm -i -v /home/valheim/server:/home/steam/valheim-server :steamcmd /bin/bash /home/steam/steamcmd/update_valheim.sh')