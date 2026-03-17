from MobileApps.libs.flows.base_flow import BaseFlow

class CommonFlow(BaseFlow):
    system = "common"

    def __init__(self, driver, platform=None):
        super(CommonFlow, self).__init__(driver, platform=platform)
        self.load_common_system_ui()

    def load_common_system_ui(self):
        ui_map = self.load_ui_map(system="COMMON", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map)
        return True