from abc import ABCMeta
from MobileApps.libs.flows.windows.windows_flow import WindowsFlow
from MobileApps.libs.ma_misc import ma_misc
import logging


class HPXFlow(WindowsFlow):
    __metaclass__ = ABCMeta
    project = "hpx"

    def __init__(self,driver):
        super(HPXFlow, self).__init__(driver)
        self.func_ignore_methods.append("load_hpx_app_shared_ui")
        self.load_hpx_app_shared_ui()

    def load_hpx_app_shared_ui(self):
        ui_map = self.load_ui_map(system="WINDOWS", project="hpx", flow_name="shared_obj")
        self.driver.load_ui_map("hpx", "shared_obj", ui_map)
        return True
