# -*- coding: utf-8 -*-

from ..internal.deadhoster import DeadHoster


class StorageTo(DeadHoster):
    __name__ = "StorageTo"
    __type__ = "hoster"
    __version__ = "0.06"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?storage\.to/get/.+"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Storage.to hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("mkaay", "mkaay@mkaay.de")]
