import re
from .exceptions import VersionException


class VersionFinder:
    def __init__(self, file_path='./ml_flow/__init__.py'):
        self.version_file_path = file_path
        self.version = ''

    def find_version(self):
        try:
            with open(self.version_file_path) as f:
                for line in f:  # decoupling modules from setup, instead of importing here
                    match = re.fullmatch(r"__version__ *= *('.*')", line)

                    if match:
                        self.version, = match.groups()
                        break

                if not self.version:
                    raise VersionException('declare __version__')
        except FileNotFoundError:
            raise VersionException('parent package missing')

        return self.version


class LongDescriptionFinder:
    def __init__(self, file_path='./README.rst'):
        self.file_path = file_path

    def get_desc_from_readme(self):

        try:
            with open(self.file_path) as f:
                return f.read()
        except FileNotFoundError:
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True
