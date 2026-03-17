import json
from selenium.common.exceptions import *
from time import time
from MobileApps.libs.flows.windows.jweb_service_routing.jweb_service_routing_flow import JwebServiceRoutingFlow

class ServiceRoutingPlugin(JwebServiceRoutingFlow):
    flow_name = "service_routing_plugin"

    def select_get_services_test_btn(self):
        """
        Click the get services test btn in ServiceRouting.getServices()
        """
        timeout = time() + 10
        get_service_text_result = False
        while timeout > time() and not get_service_text_result:
            self.swipe_to_object("get_services_test_button", direction="up")
            self.driver.click("get_services_test_button", raise_e=False)
            get_service_text_result = "services" in self.get_services_result()

    def swipe_to_object(self, obj, direction="down"):
        """
        Within Service Routing Plugin, swipe to an object given a direction
        """
        for _ in range(10):
            if not self.driver.wait_for_object(obj, raise_e=False, timeout=1):
                self.driver.swipe(anchor_element="service_routing_header", direction=direction)
            else:
                return True
        else:
            return False
    
    def get_services_result(self):
        """
        Returns 'Result' text in ServiceRouting.getServices()
        """
        self.swipe_to_object("get_services_test_result", direction="up")
        return self.driver.get_attribute("get_services_test_result", "text", displayed=False)

    def enter_service_availability_id(self, text):
        """
        Enter text value into service availability id in ServiceRouting.getServiceAvailability()
        """
        self.driver.click("service_availability_service_id", displayed=False)
        self.driver.send_keys("service_availability_service_id", text)

    def select_get_service_availability_test_btn(self):
        """
        Click the get services availability test btn in ServiceRouting.getServiceAvailability()
        """
        self.driver.click("get_service_availability_test_button", displayed=False)

    def get_service_availability_result(self):
        """
        Return JSON data found after clicking get services availability test btn in ServiceRouting.getServiceAvailability()
        """
        return json.loads(self.driver.get_attribute("get_service_availability_result_txt", "text", displayed=False))
    
    def enter_launch_service_id(self, text):
        """
        Enter text value into service availability id in ServiceRouting.launchService()
        """
        self.driver.click("launch_service_svc_id", displayed=False)
        self.driver.send_keys("launch_service_svc_id", text)

    def select_launch_service_test_btn(self):
        """
        Click the launch services test btn in ServiceRouting.launchService()
        """
        self.driver.click("launch_service_test_btn", displayed=False)

    def enter_service_launch_data(self, text):
        """
        Enter text value into service availability id in ServiceRouting.launchService()
        """
        self.driver.click("service_launch_data", displayed=False)
        self.driver.send_keys("service_launch_data", text)

    def select_transition_drop_down_menu(self):
        """
        Select transition type drop down menu in ServiceRouting.launchService()
        """
        self.driver.click("transition_type_drop_down_menu")

    def select_transition_option_from_menu(self, option):
        """
        After opening transition type drop down menu, select one of three options
        """
        option.lower()
        if option == "none":
            self.driver.click("transition_type_none")
        elif option == "forward":
            self.driver.click("transition_type_forward")
        elif option == "backward":
            self.driver.click("transition_type_backward")
        else:
            raise NameError("transition option:{} not present from transition drop down menu".format(option))

    def get_service_launch_result(self):
        """
        Return JSON data found after clicking get service availability test btn in ServiceRouting.launchService()
        """
        return json.loads(self.driver.get_attribute("service_launch_result_txt", "text", displayed=False))
    
    def select_get_service_instance_test_btn(self):
        """
        Click the get service instance test btn in ServiceRouting.getServiceInstance()
        """
        self.driver.click("get_service_instance_test_btn", displayed=False)

    def get_service_instance_result(self):
        """
        Return JSON data found after clicking the get service instance test btn in ServiceRouting.getServiceInstance()
        """
        return json.loads(self.driver.get_attribute("get_service_instance_result_txt", "text", displayed=False))
    
    def select_launch_service_options_availability_test_btn(self):
        """
        Selects the test btn from launch service options in ServiceRouting.getServiceInstanceLaunchOptions()
        """
        self.driver.click("launch_service_options_availability_test_btn", displayed=False)

    def get_launch_service_options_result_text(self):
        """
        returns the result text after selecting the test btn in ServiceRouting.getServiceInstanceLaunchOptions()
        """
        return json.loads(self.driver.get_attribute("service_options_availability_result_text", "text", displayed=False))

    def select_back_btn(self, hidden_button=False):
        """
        Clicks on back btn after launching activity
        """
        self.driver.click("back_btn", delay=1) if not hidden_button else self.driver.click("hidden_back_btn", delay=1)

    def select_go_back_btn(self, hidden_button=False):
        """
        Clicks on back btn after launching activity
        """
        self.driver.click("go_back_btn", delay=1) if not hidden_button else self.driver.click("hidden_back_btn", delay=1) 

    def select_refresh_available_services_from_repo(self):
        """
        Click refresh available services from Jarvis Service Repository toggle
        """
        try:
            self.driver.click("refresh_available_services_from_repo")
        except NoSuchElementException:
            self.swipe_to_object("refresh_available_services_from_repo", direction="up")
            self.driver.click("refresh_available_services_from_repo")

    def select_close_service_instance_test_btn(self):
        """
        Click the close service instance test btn in ServiceRouting.closeServiceInstance()
        """
        self.swipe_to_object("close_service_instance_test_btn", direction="down")
        self.driver.click("close_service_instance_test_btn")

    def select_toggle_under_launch_service(self, value):
        """
        Click toggle under launch service
        """
        self.driver.check_box("display_under_navbar_switch", uncheck=not value)

    def select_custom_plugin_from_side_menu(self):
        """
        Select custom plugin from side menu drop down
        """
        self.driver.click("custom_plugin_dropdown", displayed=False)

    def select_setting_tab(self):
        """
        Select setting tab from custom plugin from side menu drop down
        """
        self.driver.click("settings_side_menu", displayed=False)

    def select_toggle_under_settings_tab(self, value):
        """
        Click settings to toggle navigation white list enforcement
        """
        self.driver.check_box("toggle_enforce_navigation_whitelist", uncheck=not value)

    def select_left_go_back_button(self, hidden_button=False):
        """
        Clicks on back btn after launching activity
        """
        self.driver.click("left_go_back_btn") 
        
    def verify_done_btn(self):
        """
        Verifies the back btn is present
        """
        return self.driver.wait_for_object("hidden_back_btn", raise_e=False)
    
    def get_event_notification_text(self):
        """
        Return text found within the toast pop up
        """
        return self.driver.wait_for_object("notification_toast_text", displayed =False).text

    def back_btn_after_launching_activity(self):
        """
        Clicks on back btn after launching activity
        """
        self.driver.click("hidden_back_btn")