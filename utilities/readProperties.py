import configparser
import os

config  =   configparser.RawConfigParser()
file = os.path.abspath(os.curdir)+"\\configurations\\config.ini"
config.read(file)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo' , 'baseURL')
        return url
    
    @staticmethod
    def getEmail():
        email= config.get('commonInfo','email')
        return email
    @staticmethod
    def getPassword():
        password    =   config.get('commonInfo' , 'password')
        return password