import os
import sys
from data import Data

from Browser import Logs, Browser

class Config(Data):
    
    def __init__(self, path):
        Data.__init__(self, path)
        self.pkgs = ["PyQt5", "colorama", "pytube"]
        self.curPath = "\\".join(os.path.abspath(os.path.curdir).split("\\")[:-1])
        self.logsFile = f"{self.curPath}\\LOGS.txt"
        self.pPipFile = "\\".join(self.curPath.split("\\")[:-1])
        # print(self.pPipFile)

    def _config(self):
        logs = Logs()
        _installed = 0
        _data = self.load()
        isFailed = True
       
        for pkg in self.pkgs:
            try:
                os.system(f"pip install {pkg}")
                os.system(f"pip install {pkg} --upgrade")
                _installed += 1
            except:
                logs.addToLogs(f"Failed to install {pkg} !")

        if _installed == 3:
            _data['installed_all'] = True
            self.save(_data)
            isFailed = False
        else:
            logs.addToLogs("Failed to install all packages !")
            isFailed = True

        
        Browser.pringLOGS(self.curPath, logs=str(logs))
        return not isFailed     
