import time
import logging

from MobileApps.libs.flows.web.web_flow import WebFlow

class VAFlow(WebFlow):
    project = "virtual_agent"

    def __init__(self, driver, context=None,  url=None):
        super(VAFlow, self).__init__(driver, context=context, url=url)