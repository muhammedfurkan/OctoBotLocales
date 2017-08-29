"""
octeon_locale reader
"""
import os.path
from pprint import pprint
class LocaleError(Exception):
    pass

class InvalidLocale(LocaleError):
    pass

def read(path):
    with open(os.path.normpath(path),) as f:
        data = f.read().split("--- ")[1:]
        if data == []:
            raise InvalidLocale("Invalid Locale file. Doesnt contain any strings")
        readed = {}
        for string in data:
            readed[string.split("\n")[0].strip()] = "\n".join(string.split("\n")[1:])[:-1].replace('\\n', '\n')
        return readed

if __name__ == '__main__':
    pprint(read("core/en.octeon_locale"))
    pprint(read("core/ru.octeon_locale"))