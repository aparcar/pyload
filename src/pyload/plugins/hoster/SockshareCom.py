# -*- coding: utf-8 -*-

from ..internal.deadhoster import DeadHoster


class SockshareCom(DeadHoster):
    __name__ = "SockshareCom"
    __type__ = "hoster"
    __version__ = "0.11"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?sockshare\.com/(mobile/)?(file|embed)/(?P<ID>\w+)"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Sockshare.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [
        ("jeix", "jeix@hasnomail.de"),
        ("stickell", "l.stickell@yahoo.it"),
        ("Walter Purcaro", "vuolter@gmail.com"),
    ]
