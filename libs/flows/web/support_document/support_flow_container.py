import logging
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.support_document.home import Home

class SupportFlowContainer(object):
    def __init__(self, driver,  window_name=None):
        self.driver = driver
        self.fd = {"home": Home(driver, window_name=window_name)}

    @property
    def flow(self):
        return self.fd

    def navigate(self, url):
        self.driver.navigate(url)