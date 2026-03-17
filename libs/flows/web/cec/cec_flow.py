from abc import ABCMeta
from MobileApps.libs.flows.web.web_flow import WebFlow


class CECflow(WebFlow):
    __metaclass__ = ABCMeta
    project = "cec"
