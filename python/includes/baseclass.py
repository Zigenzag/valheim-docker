import os

class BaseClass:

    def _invoke(self, command: str):
        stream = os.popen(command)
        return stream.read()