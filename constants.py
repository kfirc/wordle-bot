import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = f'{ROOT_DIR}/resources'
ZIPFILE_PATH = f'{RESOURCES_DIR}/words_dictionary.zip'
JSONFILE_PATH = f'{RESOURCES_DIR}/words_dictionary.json'

# Wordle
NUMBER_OF_TRIES = 6
NUMBER_OF_LETTERS = 5
