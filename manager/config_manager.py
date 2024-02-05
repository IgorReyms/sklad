import json, os
import pathlib
class ConfigParser:
    def __init__(self, path = ''):
        if path == '':
            this = os.getcwd().split('manager')
            self.__path = this[0] + '\\config.json'

        self.config = self.__get_config()

    def __get_config(self):
        with open(self.__path, 'r') as f:
            config = json.load(f)
        return config

    def save_config(self) -> bool:
        with open(self.__path, 'w') as f:
            json.dump(self.config, f)
        return True


