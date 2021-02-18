from .baseclass import BaseClass
import re

class SteamCMD(BaseClass):
    
    def check_update(self):
        output = self._invoke(f'docker run --rm -i steamcmd /bin/bash /home/steam/steamcmd/check_update_valheim.sh')
        output = output.split(',')
        return re.search('([0-9]*)/', output[1]).group(1)
    
    def update(self):
        return self._invoke(f'docker run -i steamcmd -v /home/valheim/server:/home/steam/valheim-server /bin/bash /home/steam/steamcmd/update_valheim.sh --rm')