from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class HPXFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "hpx"

    def __init__(self, driver):
        super(HPXFlow, self).__init__(driver)
        self.load_hpx_app_shared_ui()

    def load_hpx_app_shared_ui(self):
        ui_map = self.load_ui_map(system="ANDROID", project="hpx", flow_name="shared_obj")
        self.driver.load_ui_map("hpx", "shared_obj", ui_map)
        return True
