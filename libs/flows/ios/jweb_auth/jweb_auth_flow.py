from abc import ABCMeta
from MobileApps.libs.flows.ios.ios_flow import IOSFlow

class JwebAuthFlow(IOSFlow):
    __metaclass__ = ABCMeta
    project = "jweb_auth"