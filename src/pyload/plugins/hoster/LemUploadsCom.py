# -*- coding: utf-8 -*-

from ..internal.deadhoster import DeadHoster


class LemUploadsCom(DeadHoster):
    __name__ = "LemUploadsCom"
    __type__ = "hoster"
    __version__ = "0.07"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"https?://(?:www\.)?lemuploads\.com/\w{12}"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """LemUploads.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("t4skforce", "t4skforce1337[AT]gmail[DOT]com")]
