import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self) -> int:
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        l = [element.strip() for line in self.config.get('tox', 'envlist').strip('\n').splitlines() for element in line.strip(',').split(',')]
        return l

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        return {self.config.get(section, 'basepython') for section in self.config.sections() if self.config.has_option(section,'basepython')}