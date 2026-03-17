import pytest
from time import sleep
from MobileApps.resources.const.web.const import TEST_DATA 

pytest.app_info = "JWEB"

class Test_Suite_01_Service_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, jweb_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        # cls.web_home = cls.fc.fd["web_home"]
        cls.service_plugin = cls.fc.fd["service_plugin"]
        # Language codes as of ISO 639-1
        cls.languages = TEST_DATA.ISO_LANGUAGE_LIST

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_service_routing_plugin(self):
        self.driver.restart_app()
        self.home.select_webview_mode(raise_e=False)
        self.home.select_jweb_reference_btn(raise_e=False)
        self.home.select_url_go_btn(raise_e=False)
        self.home.select_custom_plugins_tab_from_menu()
        self.home.select_settings_tab_from_menu()
        self.home.change_service_routing_stack('MOCK')
        self.home.select_plugin_from_home("Service Routing")

    def test_01_verify_list_of_supported_services(self):
        """
        C28698127: Retrieve the list of supported services
            - After navigating to the Service Routing Plugin, select the test btn under the getServices() tab
            - verify that the list of supported services is present
        """
        self.service_plugin.select_get_services_test_btn()
    
    def test_02_verify_launch_error_with_invalid_service_id(self):
        """
        C28702704: Launch a service with an invalid service id
            - Navigate to the Service Routing Plugin
            - Within the getServiceAvailability() tab, enter an invalid service_id and select the test btn
            - Expecting a serviceNotFound error message
        """
        self.service_plugin.enter_service_availability_id("this_is_an_invalid_service_id")
        self.service_plugin.select_get_service_availability_test_btn()
        assert 'serviceNotFound' in self.service_plugin.get_service_availability_result()["errorType"]

    def test_03_verify_launch_error_with_unavailable_plugin(self):
        """
        C29391639: Launch a native service when a required plugin is not available
        -After trying to launch a native service which depends on unavailable pluging, verify error is thrown
        """
        self.service_plugin.enter_launch_service_id("NativeService_Invalid_Plugins")
        self.service_plugin.enter_service_launch_data('')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_04_verify_launch_error_with_unavailable_service(self):
        """
        C29391640: Launch a native service when a required service is not available
        -After trying to launch a native service which depends on unavailable service, verify error is thrown
        """
        self.service_plugin.enter_launch_service_id("NativeService_Invalid_Services")
        self.service_plugin.enter_service_launch_data('')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_05_validate_response_invalid_url(self):
        """
        C28711671:  Validate response when invalid URL is provided
        """
        self.service_plugin.enter_service_launch_data('{"url": "://localhost:3000/index.html#/eventing"}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_06_validate_response_blank_url(self):
        """
        C29388288: Validate response when blank URL is provided
        """
        self.service_plugin.enter_service_launch_data('{"url": ""}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_07_retrieve_current_state_of_service_after_launching(self):
        """
        C28698130: Retrieve the current state of a service after launching it
        """
        self.service_plugin.enter_launch_service_id("openUrl")
        self.service_plugin.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_plugin.select_toggle_under_launch_service(True)
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        self.service_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'openUrl'
        assert service_instance_result['state'] == 'closed'

    def test_08_launch_openUrl_service_using_whitelisted_HTTPS_URL_navbar_off(self):
        """
        C33548601: Launch the openUrl service using a whitelisted HTTPS URL with DisplayUnderNavbar off
        """
        self.home.select_custom_plugins_tab_from_menu()
        self.home.select_settings_tab_from_menu()
        self.home.select_enforce_navigation_toggle()
        self.home.select_plugin_from_home("Service Routing")
        self.service_plugin.enter_launch_service_id("openUrl")
        self.service_plugin.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_plugin.select_toggle_under_launch_service(False)
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.verify_done_btn() is not True

    def test_09_launch_openUrl_service_using_whitelisted_HTTPS_URL_navbar_on(self):
        """
        C33548602: Launch the openUrl service using a whitelisted HTTPS URL with DisplayUnderNavbar on
        """
        self.home.select_custom_plugins_tab_from_menu()
        self.home.select_settings_tab_from_menu()
        self.home.select_enforce_navigation_toggle()
        self.home.select_plugin_from_home("Service Routing")
        self.service_plugin.enter_launch_service_id("openUrl")
        self.service_plugin.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_plugin.select_toggle_under_launch_service(True)
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.verify_done_btn() is not True

    def test_10_verify_launch_error_bad_url(self):
        """
        C29391647: Launch a cloud service with a blank URL
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of the cloud service with a blank URL, leaving the service launch data field blank
            - After clicking on the launchService() test btn, we expect an "invalidOptions" error to be returned
        """
        self.service_plugin.enter_launch_service_id("BadURL")
        self.service_plugin.enter_service_launch_data('')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_11_verify_service_availability_using_service_id(self):
        """
        C28698128: Verify the service availability using the service id
            - Navigate to the Service Routing Plugin
            - Within the getServiceAvailability() tab, enter a valid service_id ("C") and select the test btn
            - Expecting a json value with "serviceId": "C" to be returned
        """
        self.service_plugin.enter_service_availability_id("C")
        self.service_plugin.select_get_service_availability_test_btn()
        assert 'serviceId' in self.service_plugin.get_service_availability_result()

    def test_12_verify_launch_native_service_available_plugins_services(self):
        """
        C29391638: Launch a native service when the required plugins and services are available
            - Navigate to the Service Routing Plugin
            - Under launchService(), enter "HelloWorld" service id and click on test btn
            - Close the service returning to the Service Routing Plugin
            - Expecting a json value with service details returned under launchService()
        """
        self.service_plugin.enter_launch_service_id("HelloWorld")
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        launch_result = self.service_plugin.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'helloWorld' 
        assert 'instanceId' in launch_result

    def test_13_verify_state_of_launched_native_service(self):
        """
        C29458310: Retrieve the current state of a service after launching it
            - Navigate to the Service Routing Plugin
            - Under launchService(), enter "HelloWorld" service id and click on test btn
            - Close the service returning to the Service Routing Plugin
            - Under getServiceInstance() click on test btn
            - Expecting json value to be returned detailing the closed state of the just launched service
        """
        self.service_plugin.enter_launch_service_id("HelloWorld")
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        self.service_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'helloWorld'
        assert service_instance_result['state'] == 'closed'

    def test_14_verify_launch_cloud_service_with_any_https_url(self):
        """
        C29391643: Launch a cloud service with any HTTPS Url and the required plugins and services available when whitelisting toggle is off
            - Whitelisting URL is toggled off by default in the Windows Service Routing Application
            - Navigate to the Service Routing Plugin
            - Under launchService(), enter service id for valid HTTPS URL ("7d65350e-64f6-4a2f-8191-0aa81d33e3c7") and click on test btn
            - Close the  service returning to the Service Routing Plugin
            - Expecting json value to be returned detailing the launching state of the service
        """
        self.service_plugin.enter_launch_service_id("7d65350e-64f6-4a2f-8191-0aa81d33e3c7")
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        launch_result = self.service_plugin.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == '7d65350e-64f6-4a2f-8191-0aa81d33e3c7'
        assert launch_result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']

    def test_15_verify_launch_error_required_plugin_unavailable(self):
        """
        C29391644: Launch a cloud service when a required plugin is not available
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of a cloud service that depends on an unavailable plugin ("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
            - After clicking on the launchService() test btn, we expect a "serviceNotSupported" error to be returned
        """
        self.service_plugin.enter_launch_service_id("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotSupported'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Service Dependencies Are Missing'

    def test_16_verify_launch_error_required_service_unavailable(self):
        """
        C29391645: Launch a cloud service when a required service is not available 
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of a cloud service that depends on an unavailable service ("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
            - After clicking on the launchService() test btn, we expect a "serviceNotSupported" error to be returned
        """
        self.service_plugin.enter_launch_service_id("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result()['errorType'] == 'serviceNotSupported'
        assert self.service_plugin.get_service_launch_result()['reason'] == 'Service Dependencies Are Missing'

    def test_17_verify_current_state_post_cloud_service_launch(self):
        """
        C29458311: Retrieve the current state of a cloud service after launching it
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of the available cloud service
            - Close the service, which should auto-populate the getServiceInstance() service id field with the last launched service
            - Under getServiceInstance() click on test btn
            - Expecting json value to be returned with service launch details including a closed state
        """
        self.service_plugin.enter_launch_service_id("7d65350e-64f6-4a2f-8191-0aa81d33e3c7")
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        self.service_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == '7d65350e-64f6-4a2f-8191-0aa81d33e3c7'
        assert service_instance_result['state'] == 'closed'

    def test_18_verify_launch_cloud_service_with_whitelisted_https_url(self):
        """
        C29519784: Launch a cloud service with a whitelisted HTTPS URL when enforce whitelist toggle is ON
        """
        self.service_plugin.select_custom_plugin_from_side_menu()
        self.service_plugin.select_setting_tab()
        self.service_plugin.select_toggle_under_settings_tab(True)
        self.home.select_plugin_from_home("Service Routing")
        self.service_plugin.enter_launch_service_id("HelloWorld")
        self.service_plugin.enter_service_launch_data('')
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        result = self.service_plugin.get_service_launch_result()
        assert result['state'] == 'launching'
        assert result['serviceId'] == 'helloWorld'
        assert result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']

    def test_19_verify_launch_cloud_service_with_non_whitelisted_https_url(self):
        """
        C29519785: Launch a cloud service with a non-whitelisted HTTPS URL and the required plugins and services available when enforce whitelist toggle is ON
        """
        self.home.select_custom_plugins_tab_from_menu()
        self.home.select_settings_tab_from_menu()
        self.home.select_enforce_navigation_toggle()
        self.home.select_plugin_from_home("Service Routing")
        self.service_plugin.enter_launch_service_id("google")
        self.service_plugin.enter_service_launch_data('')
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_back_btn(hidden_button=True)
        result = self.service_plugin.get_service_launch_result()
        assert result['state'] == 'launching'
        assert result['serviceId'] == 'google'
        assert result['instanceId'] == self.service_plugin.get_service_launch_result()['instanceId']

    def test_20_verify_close_service_instance(self):
        """
        C30299006: Close a service instance
        """
        self.service_plugin.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.service_plugin.enter_service_launch_data('{"test":"test"}')
        self.service_plugin.select_transition_drop_down_menu()
        self.service_plugin.select_transition_option_from_menu("forward")
        self.service_plugin.select_launch_service_test_btn()
        self.home.select_plugin_from_home("Service Routing")
        self.service_plugin.select_close_service_instance_test_btn()
        assert 'CLOSED' in self.service_plugin.get_event_notification_text()

    def test_21_retrieve_launch_options_from_current_service_instance(self):
        """
        C29458363: Retrieve the launch options from the current service instance of the service
        """
        self.service_plugin.enter_launch_service_id("openUrl")
        self.service_plugin.enter_service_launch_data('{"url": "jweb://localhost/index.html"}')
        self.service_plugin.select_transition_drop_down_menu()
        self.service_plugin.select_transition_option_from_menu("forward")
        self.service_plugin.select_launch_service_test_btn()
        self.home.select_plugin_from_home("Service Routing")
        self.service_plugin.select_launch_service_options_availability_test_btn()
        service_instance_launch_result = self.service_plugin.get_launch_service_options_result_text()
        assert service_instance_launch_result['serviceOptions'] == self.service_plugin.get_launch_service_options_result_text()['serviceOptions']
        assert service_instance_launch_result['serviceId'] == 'openUrl'
        assert service_instance_launch_result['transitionType'] == 'forward'