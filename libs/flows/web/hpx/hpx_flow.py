from MobileApps.libs.flows.web.web_flow import WebFlow

class HPXFlow(WebFlow):
    project = "hpx"

    def __init__(self,driver):
        super(HPXFlow, self).__init__(driver)
        self.func_ignore_methods.append("load_hpx_app_shared_ui")
        self.load_hpx_app_shared_ui()

    def load_hpx_app_shared_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="hpx", flow_name="shared_obj")
        self.driver.load_ui_map("hpx", "shared_obj", ui_map)
        return True