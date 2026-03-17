import json
from MobileApps.libs.flows.ios.jweb_service_routing.jweb_service_routing_flow import JwebServiceRoutingFlow

class Weblet(JwebServiceRoutingFlow):
    flow_name = "weblet"
    # This Weblet flow navigates the Weblet portion of the referencce application
    # from the native context, which is requried after launching a plugin service

    def select_menu(self):
        """
        From the JWeb homepage, select the top left menu button
        """
        self.driver.click("menu_btn")

    def select_plugins_tab_from_menu(self):
        """
        From the expanded menu, select the plugins tab
        """
        self.driver.click("expand_plugins_menu_btn")

    def select_service_routing_plugin(self):
        """
        From the plugins tab, select the service routing plugin
        """
        self.driver.click("service_routing_plugin_link")
    
    def select_launch_service_options_availability_test_btn(self):
        """
        Selects the test btn from launch service options
        """
        self.driver.click("launch_service_options_availability_test_btn", displayed=False)
    
    def get_launch_service_options_result_text(self):
        """
        returns the result text after selecting the test btn from launch service options
        """
        return json.loads(self.driver.get_attribute("service_options_availability_result_text", "value"))

    def enter_service_availability_id(self, text):
        """
        Enter text value into service availability id
        """
        if self.driver.wait_for_object("service_availability_service_id", raise_e=False, timeout=3) is not False:
            self.driver.send_keys("service_availability_service_id", text)
        else:
            textbox = self.driver.wait_for_object("service_availability_service_id", displayed=False)
            textbox.clear()
            textbox.send_keys(text)

    def enter_launch_service_id(self, text):
        """
        Enter text value into service availability id
        """
        self.driver.wait_for_object("launch_service_svc_id")
        self.driver.send_keys("launch_service_svc_id", text)

    def enter_service_launch_data(self, text):
        """
        Enter text value into lanch data
        """
        self.driver.send_keys("service_launch_data", text)

    def select_weblet_back_btn(self):
        """
        After launching a service, selects the top navigation back btn titled 'Weblet'
        """
        self.driver.click("weblet_back_btn")

    def select_done_btn(self):
        """
        After launching a service, selects the top navigation back btn titled 'Done'
        """
        self.driver.click("done_btn")

    def select_close_service_options_test_btn(self):
        """
        Close the service options test
        """
        self.driver.click("close_service_options_test_btn", displayed=False)

    def verify_done_btn(self):
        """
        Verifies the back btn is present
        """
        return self.driver.wait_for_object("done_btn", raise_e=False)