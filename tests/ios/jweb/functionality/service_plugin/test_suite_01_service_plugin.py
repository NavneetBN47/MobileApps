import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Service_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.service_plugin = cls.fc.fd["service_routing_plugin"]
        cls.native_weblet = cls.fc.fd["weblet"]
        cls.web_home = cls.fc.fd["web_home"]
        cls.settings_plugin = cls.fc.fd["settings_plugin"]
        cls.console = cls.fc.fd["console"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_service_routing_plugin(self):
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("service_routing")

    def test_01_verify_list_of_supported_services(self):
        """
        C28698127: Retrieve the list of supported services 
        - After selecting test btn in getServices() tab, verify that a list of supported services is present 
        """
        self.service_plugin.select_get_services_test_btn()
        assert 'services' in self.service_plugin.get_services_result()

    def test_02_verify_service_availability_using_service_id(self):
        """
        C28698128: Verify the service availability using the service id
        - After selecting test btn in getServices() tab, verify that a list of supported services is present
        """
        self.native_weblet.enter_service_availability_id("C")
        self.service_plugin.select_get_service_availability_test_btn()
        assert self.service_plugin.get_service_availability_result()['errorType'] == 'serviceNotFound'

    def test_03_verify_launch_error_with_invalid_service_id(self):
        """
        C28702704: Launch a service with an invalid service id
        - Enter invalid service id into the service availability id field, and verify that 'serviceNotFound' error is produced
        """
        self.native_weblet.enter_service_availability_id("this_is_an_invalid_service_id")
        self.service_plugin.select_get_service_availability_test_btn()
        assert 'serviceNotFound' in self.service_plugin.get_service_availability_result()["errorType"]

    def test_04_verify_launch_error_with_unavailable_plugin(self):
        """
        C29391639: Launch a native service when a required plugin is not available
        - After trying to launch a native service which depends on unavailable plugin, verify error is thrown
        """
        self.native_weblet.enter_launch_service_id("NativeService_Invalid_Plugins")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_05_verify_launch_error_with_unavailable_service(self):
        """
        C29391640: Launch a native service when a required service is not available
        - After trying to launch a native service which depends on unavailable service, verify error is thrown
        """
        self.native_weblet.enter_launch_service_id("NativeService_Invalid_Services")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_06_verify_launch_error_required_plugin_unavailable(self):
        """
        C29391644: Launch a cloud service when a required plugin is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.native_weblet.enter_launch_service_id("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_07_verify_launch_error_required_service_unavailable(self):
        """
        C29391645: Launch a cloud service when a required service is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.native_weblet.enter_launch_service_id("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_08_validate_response_invalid_url(self):
        """
        C28711671: Validate response when invalid URL is provided
        """
        self.native_weblet.enter_service_launch_data('{"url": "://localhost:3000/index.html#/eventing"}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotSupported'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Expected https or jweb URL scheme'

    def test_09_validate_response_blank_url(self):
        """
        C29388288: Validate response when blank URL is provided
        """
        self.native_weblet.enter_service_launch_data('{"url": ""}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Invalid service options'

    def test_10_retrieve_current_state_of_service_after_launching(self):
        """
        C28698130: Retrieve the current state of a service after launching it
        """
        self.home.select_plugin_from_home('settings')
        self.home.select_enforce_navigation_toggle()
        self.home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_plugin.select_display_under_navbar_toggle()
        self.service_plugin.select_launch_service_test_btn()
        self.native_weblet.select_done_btn()
        self.service_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'openUrl'
        assert service_instance_result['state'] == 'closed'

    def test_11_launch_open_url_service_using_whitelisted_https_url_navbar_off(self):
        """
        C33548601: Launch openUrl service using whitelisted https URL with navbar off
        """
        self.home.select_plugin_from_home('settings')
        self.home.select_enforce_navigation_toggle()
        self.home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url":"https://www.hpsmart.com"}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.native_weblet.verify_done_btn() is not True

    def test_12_launch_open_url_service_using_whitelisted_https_url_navbar_on(self):
        """
        C33548602: Launch openUrl service using whitelisted https URL with navbar on
        """
        self.home.select_plugin_from_home('settings')
        self.home.select_enforce_navigation_toggle()
        self.home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url":"https://www.hpsmart.com"}')
        self.service_plugin.select_display_under_navbar_toggle()
        self.service_plugin.select_launch_service_test_btn()
        assert self.native_weblet.verify_done_btn() is not False