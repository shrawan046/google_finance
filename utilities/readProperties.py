import configparser
import os
from pathlib import Path
from configparser import ConfigParser


print("Read Property Current directory:", os.getcwd())
config_path = os.environ.get('CONFIG_PATH', 'Configurations/config.ini')
print("Config path:", config_path)
# config = configparser.RawConfigParser()
#config.read('Configurations/config.ini')
config = ConfigParser()
config.read(config_path)
print("Sections:", config.sections())


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('Settings', 'baseURL')
        return url

    @staticmethod
    def variable():
        var = config.get('variables', 'input')
        return var
