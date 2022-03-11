import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if not re.match(r'.*\.[a-z]{2,3}$', name):
            print(name)
            raise DomainException

        self.name = name
        
    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively

    def __str__(self):
        return self.name

    @classmethod
    def parse_url(cls, url: str):
        return Domain(url.split('://')[1].split('/')[0])

    @classmethod
    def parse_email(cls, email: str):
        return Domain(email.split('@')[1])
    