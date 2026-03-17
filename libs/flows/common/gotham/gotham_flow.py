from abc import ABCMeta
from MobileApps.libs.flows.common.common_flow import CommonFlow
from MobileApps.libs.ma_misc import ma_misc
import logging


class GothamFlow(CommonFlow):
    __metaclass__ = ABCMeta
    project = "gotham"

    def __init__(self, driver):
        super(GothamFlow, self).__init__(driver)
        self.load_gotham_app_shared_ui()

    def load_gotham_app_shared_ui(self):
        ui_map = self.load_ui_map(system="COMMON", project="gotham", flow_name="shared_obj")
        self.driver.load_ui_map("gotham", "shared_obj", ui_map)
        return True
        