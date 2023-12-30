import configparser
import os
from pathlib import Path


config = configparser.RawConfigParser()
config.read('google_finance/Configurations/config.ini')


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('URL', 'baseURL')
        return url

    @staticmethod
    def variable():
        var = config.get('variables','input')
        return var
