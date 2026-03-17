import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Service_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.service_plugin = cls.fc.fd["service_routing_plugin"]
        cls.console = cls.fc.fd["console"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_service_routing_plugin(self):
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        if not self.service_plugin.verify_at_service_routing_plugin():
            self.home.select_plugin_from_home('service_routing')

    def test_01_validate_response_invalid_url(self):
        """
        C28711671: Give an invalid launch_data url scheme, expect an 'invalid options' message
        """
        self.service_plugin.enter_service_launch_data('{"url": "://localhost:3000/index.html#/eventing"}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'

    def test_02_validate_response_blank_url(self):
        """
        C29388288: Give an blank url scheme, expect an 'invalid options' message
        """
        self.service_plugin.enter_service_launch_data('{"url": ""}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'

    def test_03_verify_get_services_response(self):
        """
        C28698127: Selecting "Test" btn under getServices, expect a list of services known to the service router
        """
        self.service_plugin.select_get_services_test_btn()
        assert self.service_plugin.get_services_result()['services'] != ''

    def test_04_verify_service_availability_response(self):
        """
        C28698128: Selecting "Test" btn under getServiceAvailability, expect the availability of specific service
        """
        self.service_plugin.enter_service_availability_id("openUrl")
        self.service_plugin.select_get_service_availability_test_btn()
        assert self.service_plugin.get_service_availability_result()['serviceId'] == 'openUrl'
        self.service_plugin.enter_service_availability_id("not_a_real_service")
        self.service_plugin.select_get_service_availability_test_btn()
        assert self.service_plugin.get_service_availability_result()['errorType'] == 'serviceNotFound'

    def test_05_verify_launch_error_with_invalid_service_id(self):
        """
        C28702704: Launch a service with an invalid service id
        - Enter invalid service id into the service availability id field, and verify that 'serviceNotFound' error is produced
        """
        self.service_plugin.enter_service_availability_id("this_is_an_invalid_service_id")
        self.service_plugin.select_get_service_availability_test_btn()
        assert 'serviceNotFound' in self.service_plugin.get_service_availability_result()["errorType"]

    def test_06_verify_launch_error_with_unavailable_plugin(self):
        """
        C29391639: Launch a native service when a required plugin is not available
        - After trying to launch a native service which depends on unavailable plugin, verify error is thrown
        """
        self.service_plugin.enter_launch_service_id("NativeService_Invalid_Plugins")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_07_verify_launch_error_with_unavailable_service(self):
        """
        C29391640: Launch a native service when a required service is not available
        - After trying to launch a native service which depends on unavailable service, verify error is thrown
        """
        self.service_plugin.enter_launch_service_id("NativeService_Invalid_Services")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_08_verify_launch_error_required_plugin_unavailable(self):
        """
        C29391644: Launch a cloud service when a required plugin is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.service_plugin.enter_launch_service_id("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_09_verify_launch_error_required_service_unavailable(self):
        """
        C29391645: Launch a cloud service when a required service is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.service_plugin.enter_launch_service_id("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_10_retrieve_current_state_of_service_after_launching(self):
        """
        C28698130: Retrieve the current state of a service after launching it
        """
        self.service_plugin.enter_launch_service_id("openUrl")
        self.service_plugin.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_plugin.select_display_under_navbar_toggle()
        self.service_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_plugin.close_all_toast_popups()
        self.service_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'openUrl'
        assert service_instance_result['state'] == 'closed'

    def test_11_verify_refresh_the_list_of_supported_services(self, navigate_to_service_routing_plugin):
        """
        C29406175: Refresh the list of supported services from the repository
        """
        self.service_plugin.select_get_services_test_btn()
        assert 'services' in self.service_plugin.get_services_result()
        self.service_plugin.select_refresh_available_services_from_repo()
        self.service_plugin.select_get_services_test_btn()
        assert 'services' in self.service_plugin.get_services_result()

    def test_12_verify_close_serivce_instance(self):
        """
        C30299006: Close a service instance
        """
        self.service_plugin.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.service_plugin.enter_service_launch_data('{"test":"test"}')
        self.service_plugin.select_transition_drop_down_menu()
        self.service_plugin.select_transition_option_from_menu("forward")
        self.service_plugin.select_launch_service_test_btn()
        launch_result = self.service_plugin.get_service_launch_result()
        self.service_plugin.close_all_toast_popups()
        self.service_plugin.select_close_service_instance_test_btn()