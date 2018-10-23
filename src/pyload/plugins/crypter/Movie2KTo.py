# -*- coding: utf-8 -*-

from ..internal.deadcrypter import DeadCrypter


class Movie2KTo(DeadCrypter):
    __name__ = "Movie2KTo"
    __type__ = "crypter"
    __version__ = "0.56"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?movie2k\.to/(.+)\.html"
    __config__ = [("enabled", "bool", "Activated", True)]

    __description__ = """Movie2k.to decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("4Christopher", "4Christopher@gmx.de")]
