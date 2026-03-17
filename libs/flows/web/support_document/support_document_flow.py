import time
import logging

from MobileApps.libs.flows.web.web_flow import WebFlow

class SupportDocumentFlow(WebFlow):
    project = "support_document"

    def __init__(self, driver, context=None, url=None, window_name="main"):
        super(SupportDocumentFlow, self).__init__(driver, context=context, url=url, window_name=window_name)