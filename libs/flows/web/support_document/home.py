import logging

from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.support_document.support_document_flow import SupportDocumentFlow

class Home(SupportDocumentFlow):
    flow_name = "home"

    def get_short_desc(self):
        return self.driver.get_text("short_desc")