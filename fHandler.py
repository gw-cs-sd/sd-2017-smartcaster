import json

## Handles specific JSON file associated with a player / team.
class fHandler(object):
    def __init__(self, _FILE, _LAST, _FIRST):
        self.fn = _FILE
        self.last = _LAST
        self.first = _FIRST
    
    ## Open file, return JSON string.
    def load(self):
        with open(self.fn) as f:
            data = json.load(f)
        return (data)
    
    ## Get data under specific attribute.
    def get(self, _ATTR):
        sdata = self.load()
        return (sdata[_ATTR])
