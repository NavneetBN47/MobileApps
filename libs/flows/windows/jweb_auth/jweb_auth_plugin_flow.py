from abc import ABCMeta
from MobileApps.libs.flows.windows.windows_flow import WindowsFlow

class JwebAuthFlow(WindowsFlow):
    __metaclass__ = ABCMeta
    project = "jweb_auth"