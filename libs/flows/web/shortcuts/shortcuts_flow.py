from abc import ABCMeta
from MobileApps.libs.flows.web.web_flow import WebFlow


class NotSwitchToShortcutsWebViewException(Exception):
    pass

class Shortcutsflow(WebFlow):
    __metaclass__ = ABCMeta
    project = "shortcuts"
