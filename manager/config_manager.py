import json, os
class ConfigParser:
    def __init__(self, path = ''):
        if path == '':
            this = os.path.abspath(__file__)
            this = this.split('sklad')
            self.__path = this[0] + '/sklad/config.json'
        self.config = self.__get_config()

    def __get_config(self):
        with open(self.__path, 'r') as f:
            config = json.load(f)
        return config

    def save_config(self) -> bool:
        with open(self.__path, 'w') as f:
            json.dump(self.config, f)
        return True

