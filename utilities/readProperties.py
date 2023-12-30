import configparser
import os
from pathlib import Path

"""""
path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")   """""

config = configparser.RawConfigParser()
#config.read(config_path)
config.read('/Configurations/config.ini')


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('URL', 'baseURL')
        return url

    @staticmethod
    def variable():
        var = config.get('variables','input')
        return var
