from collections import namedtuple
import os
import sys
import yaml

absolute_path = os.path.dirname(os.path.abspath(__file__))

Config = namedtuple("Config", ['env', 'account_id', 'region', 'bot_token'])

def get_config(env: str = "dev") -> Config:
    with open(f"{absolute_path}/{env}.yml", "r") as config:
        try:
            config_dict = yaml.safe_load(config)
            return Config(**config_dict)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit()
