import json
from time import time
from selenium.common.exceptions import ElementClickInterceptedException
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class ServiceRoutingPlugin(JwebFlow):
    flow_name="service_routing_plugin"

    def select_get_services_test_btn(self):
        """
        Click the get services test btn
        """
        try:
            self.driver.click("get_services_test_button")
        except ElementClickInterceptedException:
            self.driver.swipe(direction="up", per_offset=0.7)
            self.driver.click("get_services_test_button")

    def select_refresh_available_services_from_repo(self):
        """
        Click refresh available services from Jarvis Service Repository toggle
        """
        try:
            self.driver.click("refresh_available_services_from_repo")
        except ElementClickInterceptedException:
            self.driver.swipe(direction="up", per_offset=0.7)
            self.driver.click("refresh_available_services_from_repo")

    def select_get_service_availability_test_btn(self):
        """
        Click the get services availability test btn
        """
        self.driver.click("get_service_availability_test_button")

    def select_launch_service_test_btn(self):
        """
        Click the launch services test btn
        """
        self.driver.click("launch_service_test_btn", timeout=8)

    def select_get_service_instance_test_btn(self):
        """
        Click the get service instance test btn
        """
        self.driver.click("get_service_instance_test_btn")

    def select_add_listener_test_btn(self):
        """
        Click the add listener test btn
        """
        self.driver.click("service_routing_add_listener")

    def select_event_close_button(self, index=0):
        """
        Click the event close btn of the toast notification pop up
        """
        self.driver.click("add_listener_event_close_btn", index=index)

    def close_all_toast_popups(self):
        """
        Continue closing the close button for toast pop ups
        """
        timeout = 15 + time()
        while timeout > time() and self.driver.wait_for_object("add_listener_event_close_btn", timeout=3, raise_e=False):
            self.select_event_close_button()

    def get_event_notification_text(self, get_json=True):
        """
        Return text found within the toast pop up
        """
        toast_text = self.driver.get_attribute("notification_toast_text", attribute="text")
        return json.loads(toast_text) if get_json else toast_text

    def get_service_availability_result(self):
        """
        Return JSON data found after clicking get services availability test btn
        """
        return json.loads(self.driver.wait_for_object("get_service_availability_result_txt").text)

    def get_services_result(self):
        """
        Return JSON data found after clicking get services test btn
        """
        return json.loads(self.driver.wait_for_object("get_services_result_txt").text)

    def get_service_launch_result(self):
        """
        Return JSON data found after clicking get service availability test btn
        """
        return json.loads(self.driver.wait_for_object("service_launch_result_txt").text)

    def get_service_instance_result(self):
        """
        Return JSON data found after clicking the get service instance test btn
        """
        return json.loads(self.driver.wait_for_object("get_service_instance_result_txt").text)

    def get_service_instance_svc_id(self):
        """
        Return value found inside of get_service_instance_svc_id entry field 
        """
        return self.driver.get_attribute(obj_name="get_service_instance_svc_id", attribute="value")

    def enter_service_availability_id(self, text):
        """
        Enter text value into service availability id
        """
        self.driver.send_keys("service_availability_service_id", text)

    def enter_launch_service_id(self, text):
        """
        Enter text value into service availability id
        """
        self.driver.send_keys("launch_service_svc_id", text)

    def enter_service_launch_data(self, text):
        """
        Enter text value into launch data
        """
        self.driver.send_keys("service_launch_data", text)

    def enter_get_service_instance_svc_id(self, text):
        """
        Enter text value into service instance svc id field
        """
        self.driver.send_keys("get_service_instance_svc_id", text)

    def select_transition_drop_down_menu(self):
        """
        Select transition type drop down menu from the launchService() menu
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

    def select_get_service_instance_launch_options_test_btn(self):
        """
        Select test btn under getServiceInstanceLaunchOptions() 
        """
        self.driver.click("launch_service_options_availability_test_btn")

    def verify_at_service_routing_plugin(self):
        """
        Return bool, verifying we are currently on the service routing plugin page
        """
        el = self.driver.wait_for_object("plugin_header_title", raise_e=False, timeout=3)
        return False if el is False else el.text == "Service Routing"

    def select_close_service_instance_test_btn(self):
        """
        Click close service instance test btn
        """
        self.driver.click("close_service_instance_test_button", displayed=False)
    
    def select_display_under_navbar_toggle(self):
        """
        Click display under navbar toggle switch
        """
        self.driver.click("display_under_navbar_switch")

    def get_launch_service_options_result_text(self):
        """
        returns the result text after selecting the test btn from launch service options
        """
        return json.loads(self.driver.wait_for_object("service_options_availability_result_text").text)