import yaml
import os


class Config:
    config_file_path = './config.yml'
    cfg = {}

    def load_config(self) -> None:
        """Loads config from file"""
        with open(self.config_file_path, 'r') as f:
            self.cfg = yaml.safe_load(f.read())

    def write_config(self) -> None:
        """Writes config to file"""
        self.cfg = {'api_key': input('API Key:').strip()}
        with open(self.config_file_path, 'w') as f:
            f.write(yaml.dump(self.cfg))

    def __init__(self):
        if os.path.isfile(self.config_file_path):
            self.load_config()
        else:
            self.write_config()
