from MobileApps.libs.flows.android.hpx.hpx_flow import HPXFlow
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY


class HPXAdditionalSettings(HPXFlow):
    flow_name = "hpx_additional_settings"

    SERVER_STACK_SETTING_STR = "Server Stack"
    WEBAPP_STACK_SETTING_STR = "Web Apps Stack"
    
    DEV_STACK = "dev_server_stack"
    PIE_STACK = "pie_server_stack"
    STAGE_STACK = "stage_server_stack"
    PRODUCTION_STACK = "production_server_stack"
    
    WEBAPP_PIE_STACK = "pie_webapp_stack"
    WEBAPP_STAGE_STACK = "stage_webapp_stack"
    WEBAPP_PRODUCTION_STACK = "production_webapp_stack"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def open_select_settings_page(self):
        """
        Launch Select Settings Page Screen
        """
        package_name = PACKAGE.HPX(self.driver.session_data["pkg_type"])
        self.driver.start_activity(package_name, LAUNCH_ACTIVITY.SMART_DEV_SETTINGS)

    def change_stack_server(self, stack_name, webapp_stack_name):
        """
        This flow is used to change the stack server in HPX additional settings. 
        It is used to change both the Server stack and web apps stack.
        """
        stack_text_mapping = {
            self.DEV_STACK: "dev_server_stack",
            self.PIE_STACK: "pie_server_stack",
            self.STAGE_STACK: "stage_server_stack", 
            self.PRODUCTION_STACK: "production_server_stack",
        }
        
        webapp_stack_text_mapping = {
            self.WEBAPP_PIE_STACK: "pie_webapp_stack",
            self.WEBAPP_STAGE_STACK: "stage_webapp_stack",
            self.WEBAPP_PRODUCTION_STACK: "production_webapp_stack"
        }
        
        stack_text = stack_text_mapping.get(stack_name)
        webapp_stack_text = webapp_stack_text_mapping.get(webapp_stack_name)
        
        self.search_for_setting(self.SERVER_STACK_SETTING_STR)
        self.driver.click("server_stack_btn")
        self.driver.click(stack_text)

        self.search_for_setting(self.WEBAPP_STACK_SETTING_STR)
        self.driver.click("web_apps_stack_btn")
        self.driver.click(webapp_stack_text)

    def search_for_setting(self, search_txt):
        """
        Searches developer settings (HPX additional settings)
        """
        self.driver.click("search_btn", raise_e=False)
        self.driver.send_keys("search_txtbox", search_txt)
