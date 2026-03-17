import time
import logging

from MobileApps.libs.flows.web.web_flow import WebFlow

class SupportDashboardFlow(WebFlow):
    project = "support_dashboard"

    def __init__(self, driver, context=None, url=None, window_name="main"):
        super(SupportDashboardFlow, self).__init__(driver, context=context, url=url, window_name=window_name)