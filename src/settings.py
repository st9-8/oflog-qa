from pathlib import Path

import logging
import configparser


BASE_DIR = Path(__file__).resolve().parent.parent

config = configparser.ConfigParser()
config.read(BASE_DIR / 'config.ini')


# ONTOLOGY LOCATION
BASE_URI = config['ONTOLOGY']['BASE_URI']

# DATA HEADERS FIELDS
SUBJECT = config['COMMON']['SUBJECT_FIELD']
ACTION = config['COMMON']['ACTION_FIELD']
OBJECT = config['COMMON']['OBJECT_FIELD']
DATE = config['COMMON']['DATE_FIELD']
INFORMATION = config['COMMON']['INFORMATION_FIELD']
IP = config['COMMON']['IP_FIELD']


# DATA LOCATION VARIABLES
DATA_FOLDER = BASE_DIR / config['DATA']['DATA_FOLDER']
DATA_FILE = config['DATA']['DATA_FILE']
GRAPH_FOLDER = BASE_DIR / config['DATA']['GRAPH_FOLDER']

DATE_RANGE = '30min'    # Examples: 1h30min, 1H(hours), 2D(days), 2W(weeks), 2M(months)

# Logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s[%(levelname)s]: %(message)s', datefmt='%Y-%m-%d-%H-%M-%S')
