# -*- coding: utf-8 -*-

from ..internal.xfsaccount import XFSAccount


class TusfilesNet(XFSAccount):
    __name__ = "TusfilesNet"
    __type__ = "account"
    __version__ = "0.11"
    __status__ = "testing"

    __pyload_version__ = "0.5"

    __description__ = """Tusfile.net account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("guidobelix", "guidobelix@hotmail.it")]

    PLUGIN_DOMAIN = "tusfiles.net"

    VALID_UNTIL_PATTERN = r'<span class="label label-default">(.+?)</span>'
    TRAFFIC_LEFT_PATTERN = r'<td><img src="//www\.tusfiles\.net/i/icon/meter\.png" alt=""/></td>\n<td>&nbsp;(?P<S>[\d.,]+)'
