from configparser import ConfigParser
import os

def project_root_folder():
    path = os.getcwd()
    return path

def load_settings():
    config = ConfigParser()
    config.read(project_root_folder()+'/config.ini')
    return config 

config = load_settings()

pass