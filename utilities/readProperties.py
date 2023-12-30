import configparser

config = configparser.RawConfigParser()
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
