import configparser
import os
from pathlib import Path
from configparser import ConfigParser

<<<<<<< HEAD
config_path= os.environ.get('CONFIG_PATH', 'Configurations/config.ini')
#config = configparser.RawConfigParser()
config= ConfigParser()
config.read('Configurations/config.ini')
=======

config = configparser.RawConfigParser()
config.read('google_finance/Configurations/config.ini')
>>>>>>> c4a4a623eb2299b9694118ac1a8c572ea7d66af7


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('URL', 'baseURL')
        return url

    @staticmethod
    def variable():
        var = config.get('variables','input')
        return var
