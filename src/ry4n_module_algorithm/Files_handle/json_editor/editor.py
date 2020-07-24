import json
import os
import sys
from ..file_handle import *

def check_path(path: str):
    if os.path.exists(path):
        return path
    raise ValueError("Invalid path: {0}".format(path))
    

class JSON_Editor(FILE):
    
    # Totally overwrite
    def write(self):
        pass
    
    def content(self, to_json=False):
        if to_json:
            return json.loads(self.file.read())
        return self.file.read()