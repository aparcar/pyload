# -*- coding: utf-8 -*-

from ..internal.deadhoster import DeadHoster


class UploadhereCom(DeadHoster):
    __name__ = "UploadhereCom"
    __type__ = "hoster"
    __version__ = "0.17"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?uploadhere\.com/\w{10}"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Uploadhere.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]
