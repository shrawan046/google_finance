import configparser
import os
from pathlib import Path
from configparser import ConfigParser

config_path = os.environ.get('CONFIG_PATH', 'Configurations/config.ini')
# config = configparser.RawConfigParser()
#config.read('Configurations/config.ini')
config = ConfigParser()
config.read(config_path)


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('URL', 'baseURL')
        return url

    @staticmethod
    def variable():
        var = config.get('variables', 'input')
        return var
