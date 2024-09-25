import toml

class Config:
    def __init__(self): 
        self.config = toml.load("config.toml")
    
    def get(self):
        return self.config
    
    def getDefined(self):
        return self.config.get("defined")
    
    def getSettings(self):
        return self.config.get("settings")
    

config = Config()