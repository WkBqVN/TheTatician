import configparser
import os

class GameConfig:
    _instance=None
    config_path= "Config" + os.sep + "GameConfig.conf"

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(self.config_path)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameConfig, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get_int_config(self,zone_name,field_name):
        return self._config.getint(zone_name,field_name)

    def get_field_config(self,zone_name,field_name):
        return self._config.get(zone_name,field_name)

    def get_config(self):
        return self._config


