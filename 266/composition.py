from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from os import getenv
from pathlib import Path
from typing import Any, List, NamedTuple, Optional
from urllib.error import URLError
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup  # type: ignore

TMP = getenv("TMP", "/tmp")
TODAY = date.today()
Candidate = NamedTuple("Candidate", [("name", str), ("votes", str)])
LeaderBoard = NamedTuple(
    "LeaderBoard",
    [
        ("Candidate", str),
        ("Average", str),
        ("Delegates", int),
        ("Contributions", str),
        ("Coverage", int),
    ],
)
Poll = NamedTuple(
    "Poll",
    [
        ("Poll", str),
        ("Date", str),
        ("Sample", str),
        ("Biden", float),
        ("Sanders", float),
        ("Gabbard", float),
        ("Spread", str),
    ],
)


@dataclass
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        path: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exist, it returns None.
    """

    name: str

    def __post_init__(self):
        filename = f"{TODAY}_{self.name}"
        self.path: Path = Path(TMP, filename)

    @property
    def data(self) -> Optional[str]:
        if self.path.exists():
            return self.path.read_text()
        return None


@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """

    url: str
    file: File

    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. It then reads it from the File and returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        if self.file.data is None:
            try:
                urlretrieve(self.url, self.file.path)
            except URLError:
                raise
        return self.file.data

    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        return Soup(self.data, "html.parser")


class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """

    web: Web

    def find_table(self, loc: int = 0) -> str:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
        return self.web.soup.find_all("table")[loc]

    @abstractmethod
    def parse_rows(self, table: Soup) -> List[Any]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as NamedTuple.

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass

    @abstractmethod
    def polls(self, table: int = 0) -> List[Any]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass

    @abstractmethod
    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
              Sanders: 142.0
              Gabbard: 6.0

    """

    web: Web

    def parse_rows(self, table: Soup) -> List[Poll]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        rows = [[cell.text for cell in row("td")] for row in table("tr")]
        return [
            Poll(
                t[0],
                t[1],
                t[2],
                float(t[3]) if t[3].isdigit() else 0.0,
                float(t[4]) if t[4].isdigit() else 0.0,
                float(t[5]) if t[5].isdigit() else 0.0,
                t[6],
            )
            for t in rows
            if len(t) > 0 and "RCP\xa0Average" not in t[0]
        ]

    def polls(self, table: int = 0) -> List[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        return self.parse_rows(self.find_table(table))

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        info = self.polls(loc)
        biden = sum(data.Biden for data in info)
        sanders = sum(data.Sanders for data in info)
        gabbard = sum(data.Gabbard for data in info)
        results = f"\n{self.__class__.__name__}\n"
        results += f"{'=' * len(results.strip())}\n"
        results += f"    Biden: {biden}\n"
        results += f"  Sanders: {sanders}\n"
        results += f"  Gabbard: {gabbard}\n"
        print(results)


@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    web: Web

    def parse_rows(self, table: Soup) -> List[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        names = ("Sanders", "Biden", "Bloomberg", "Warren", "Buttigieg", "Gabbard")
        rows = [[cell.text for cell in row("td")] for row in table("tr")]
        lb = []
        for t in rows:
            if len(t) == 5:
                name, polling, pledges, spent, news = t
                name = name.strip()
                for n in names:
                    if n in name:
                        name = name.replace(f"{n}{n}", n)
                        name = name.replace(f"Jr.{n}", "Jr.")
                        break
                polling = polling.strip()
                pledges = int(pledges.strip().replace("—", "0"))
                spent = spent.strip()
                news = int(news.split()[0].replace("#", ""))
                lb.append(LeaderBoard(name, polling, pledges, spent, news))
        return lb

    def polls(self, table: int = 0) -> List[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        return self.parse_rows(self.find_table(table))

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        spacing = 33
        info = self.polls(loc)
        results = f"\n{self.__class__.__name__}\n"
        results += f"{'=' * spacing}\n"
        for c in info[:5]:
            results += f"\n{c.Candidate.rjust(spacing)}\n"
            results += f"{'-' * spacing}\n"
            results += f"National Polling Average: {c.Average}\n"
            results += f"       Pledged Delegates: {c.Delegates}\n"
            results += f"Individual Contributions: {c.Contributions}\n"
            results += f"    Weekly News Coverage: {c.Coverage}\n"
        print(results)