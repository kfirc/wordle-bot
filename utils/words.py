import json
import zipfile
from pathlib import Path
import constants
from utils.common import Singleton


class EnglishWords(dict, metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._unzip_file()
        self._load_words()

    @staticmethod
    def _unzip_file():
        if Path(constants.JSONFILE_PATH).is_file():
            return

        with zipfile.ZipFile(constants.ZIPFILE_PATH) as zip_ref:
            zip_ref.extractall(constants.RESOURCES_DIR)

    def _load_words(self):
        with open(constants.JSONFILE_PATH) as word_file:
            self.update(json.load(word_file))
