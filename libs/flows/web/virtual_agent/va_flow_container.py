import logging
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.virtual_agent.home import Home

class VAFlowContainer(object):
    def __init__(self, driver,  window_name=None):
        self.driver = driver
        self.fd = {"home": Home(driver)}

    @property
    def flow(self):
        return self.fd

    def navigate(self, url):
        self.driver.navigate(url)


        