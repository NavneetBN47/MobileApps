import pytest

pytest.app_info = "JWEB_SERVICE_ROUTING"

class Test_Suite_01_Service_Routing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_service_routing_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_service_routing_setup

        cls.home = cls.fc.fd["home"]
        cls.service_routing = cls.fc.fd["service_routing"]
        cls.service_routing_plugin = cls.fc.fd["service_routing_plugin"]

    @pytest.fixture(scope="function")
    def navigate_to_service_routing_plugin(self):
        self.fc.flow_load_home_screen()
        self.home.select_service_routing_tab()
        self.service_routing.select_settings_btn()
        self.service_routing.select_settings_checkbox("enable_mocked_data_checkbox", False)
        self.driver.press_key_back()
        self.home.select_weblet_tab()

    @pytest.fixture(scope="function")
    def enable_mocked_data(self):
        self.fc.flow_load_home_screen()
        self.home.select_service_routing_tab()
        self.service_routing.select_settings_btn()
        self.service_routing.select_settings_checkbox("enable_mocked_data_checkbox", True)
        self.driver.press_key_back()
        self.home.select_weblet_tab()

    @pytest.fixture(scope="function")
    def enable_enforce_url(self):
        self.fc.flow_load_home_screen()
        self.home.select_service_routing_tab()
        self.service_routing.select_settings_btn()
        self.service_routing.select_settings_checkbox("enable_mocked_data_checkbox", False)
        self.service_routing.select_settings_checkbox("enforce_url_checkbox", True)
        self.driver.press_key_back()
        self.home.select_weblet_tab()

    def test_01_verify_list_of_supported_services(self, navigate_to_service_routing_plugin):
        """
        C28698127: Retrieve the list of supported services 
        - After selecting test btn in getServices() tab, verify that a list of supported services is present 
        """
        self.service_routing_plugin.select_get_services_test_btn()
        assert 'services' in self.service_routing_plugin.get_services_result()

    def test_02_verify_service_availability_using_service_id(self, navigate_to_service_routing_plugin):
        """
        C28698128: Verify the service availability using the service id
        - After selecting test btn in getServices() tab, verify that a list of supported services is present
        """
        self.service_routing_plugin.enter_service_availability_id("HelloWorld")
        self.service_routing_plugin.select_get_service_availability_test_btn()
        assert 'serviceId' in self.service_routing_plugin.get_service_availability_result()

    def test_03_verify_launch_error_with_invalid_service_id(self, navigate_to_service_routing_plugin):
        """
        C28702704: Launch a service with an invalid service id
        - Enter invalid service id into the service availability id field, and verify that 'serviceNotFound' error is produced
        """
        self.service_routing_plugin.enter_service_availability_id("this_is_an_invalid_service_id")
        self.service_routing_plugin.select_get_service_availability_test_btn()
        assert 'serviceNotFound' in self.service_routing_plugin.get_service_availability_result()["errorType"]

    def test_04_verify_launch_native_service_available_plugins_services(self, navigate_to_service_routing_plugin):
        """
        C29391638: Launch a native service when the required plugins and services are available
        - Launching native service, assert launch service result
        """
        self.service_routing_plugin.enter_launch_service_id("HelloWorld")
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'HelloWorld' 
        assert launch_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']

    def test_05_verify_launch_error_with_unavailable_plugin(self, navigate_to_service_routing_plugin):
        """
        C29391639: Launch a native service when a required plugin is not available
        - After trying to launch a native service which depends on unavailable plugin, verify error is thrown
        """
        self.service_routing_plugin.enter_launch_service_id("NativeService_Invalid_Plugins")
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_06_verify_launch_error_with_unavailable_service(self, navigate_to_service_routing_plugin):
        """
        C29391640: Launch a native service when a required service is not available
        - After trying to launch a native service which depends on unavailable service, verify error is thrown
        """
        self.service_routing_plugin.enter_launch_service_id("NativeService_Invalid_Services")
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_07_verify_state_of_launched_native_service(self, navigate_to_service_routing_plugin):
        """
        C29458310: Retrieve the current state of a native service after launching it
        - After launching service, verify getServiceInstance() result is valid
        """
        self.service_routing_plugin.enter_launch_service_id("HelloWorld")
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_routing_plugin.close_all_toast_popups()
        self.service_routing_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'HelloWorld'
        assert service_instance_result['state'] == 'closed'

    def test_08_verify_launch_cloud_service_with_any_https_url(self, enable_mocked_data):
        """
        C29391643: Launch a cloud service with any HTTPS URL and the required plugins and services available when enforce whitelist toggle is OFF
        - After enforcing whitelist toggle is off, and launching cloud service with https url, verify service results
        """
        self.service_routing_plugin.enter_launch_service_id("google")
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_routing_plugin.close_all_toast_popups()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'google'
        assert launch_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']
    
    def test_09_verify_launch_error_required_plugin_unavailable(self, enable_mocked_data):
        """
        C29391644: Launch a cloud service when a required plugin is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.service_routing_plugin.enter_launch_service_id("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_10_verify_launch_error_required_service_unavailable(self, enable_mocked_data):
        """
        C29391645: Launch a cloud service when a required service is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.service_routing_plugin.enter_launch_service_id("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'serviceNotFound'

    def test_11_verify_launch_error_invalid_url(self, enable_mocked_data):
        """
        C29391646: Launch a cloud service with an invalid URL (not HTTPS nor JWEB scheme)
        - Launch a cloud service with an invalid URL, verify error
        """
        self.service_routing_plugin.enter_launch_service_id("NonHttps")
        self.service_routing_plugin.enter_service_launch_data('')
        self.service_routing_plugin.select_transition_drop_down_menu()
        self.service_routing_plugin.select_transition_option_from_menu("forward")
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'serviceNotSupported'
        assert self.service_routing_plugin.get_service_launch_result()['reason'] == 'Expected https or jweb URL scheme.'

    def test_12_verify_launch_error_bad_url(self, enable_mocked_data):
        """
        C29391647: Launch a cloud service with a blank URL 
        - Launch a cloud service with an blank URL, verify error
        """
        self.service_routing_plugin.enter_launch_service_id("BadURL")
        self.service_routing_plugin.enter_service_launch_data('')
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'

    def test_13_verify_current_state_post_cloud_service_launch(self, navigate_to_service_routing_plugin):
        """
        C29458311: Retrieve the current state of a cloud service after launching it
        - Launch a cloud service, verify status after launch
        """
        self.service_routing_plugin.enter_launch_service_id("OnboardingCenter")
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_routing_plugin.close_all_toast_popups()
        self.service_routing_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'OnboardingCenter'
        assert service_instance_result['state'] == 'closed'

    def test_14_verify_launch_cloud_service_with_whitelisted_https_url(self, enable_enforce_url):
        """
        C29519784: Launch a cloud service with a whitelisted HTTPS URL when enforce whitelist toggle is ON
        """
        self.service_routing_plugin.enter_launch_service_id("HelloWorld")
        self.service_routing_plugin.enter_service_launch_data('')
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'HelloWorld'
        assert launch_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']

    def test_15_verify_refresh_the_list_of_supported_services(self, navigate_to_service_routing_plugin):
        """
        C29406175: Refresh the list of supported services from the repository
        """
        self.service_routing_plugin.select_get_services_test_btn()
        assert 'services' in self.service_routing_plugin.get_services_result()
        self.fc.navigate_and_change_stack_option('Pie')
        self.fc.flow_load_home_screen()
        self.home.select_service_routing_tab()
        self.home.select_weblet_tab()
        self.service_routing_plugin.select_refresh_available_services_from_repo()
        self.service_routing_plugin.select_get_services_test_btn()
        assert 'services' in self.service_routing_plugin.get_services_result()
    
    def test_16_retrieve_current_state_of_service_after_launching(self, enable_enforce_url):
        """
        C28698130: Retrieve the current state of a service after launching it
        """
        self.service_routing_plugin.enter_launch_service_id("openUrl")
        self.service_routing_plugin.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_routing_plugin.select_display_under_navbar_toggle()
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_routing_plugin.close_all_toast_popups()
        self.service_routing_plugin.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing_plugin.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'openUrl'
        assert service_instance_result['state'] == 'closed'

    def test_17_validate_response_invalid_url(self, enable_mocked_data):
        """
        C28711671: Validate response when the URL is invalid
        """
        self.service_routing_plugin.enter_service_launch_data('{"url": "://localhost:3000/index.html#/eventing"}')
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing_plugin.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_18_validate_response_blank_url(self, enable_mocked_data):
        """
        C29388288: Validate response when the URL is blank
        """
        self.service_routing_plugin.enter_service_launch_data('{"url": ""}')
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing_plugin.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_19_launch_open_url_service_using_whitelisted_https_url_navbar_off(self, enable_enforce_url):
        """
        C33548601:  Launch openUrl service using a whitelisted HTTPS URL with navbar off
        """
        self.service_routing_plugin.enter_launch_service_id("openUrl")
        self.service_routing_plugin.enter_service_launch_data('{"url":"https://www.hpsmart.com"}')
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.driver.press_key_back() is not True

    def test_20_launch_open_url_service_using_whitelisted_https_url_navbar_on(self, enable_enforce_url):
        """
        C33548602: Launch openUrl service using whitelisted https URL with navbar on
        """
        self.service_routing_plugin.enter_launch_service_id("openUrl")
        self.service_routing_plugin.enter_service_launch_data('{"url":"https://www.hpsmart.com"}')
        self.service_routing_plugin.select_display_under_navbar_toggle()
        self.service_routing_plugin.select_launch_service_test_btn()
        assert self.driver.press_key_back() is not True

    def test_21_verify_launch_cloud_service_with_non_whitelisted_https_url(self, enable_mocked_data):
        """
        C29519785: Launch a cloud service with a non-whitelisted HTTPS URL and the required plugins and services available when enforce whitelist toggle is ON
        """
        self.service_routing_plugin.enter_launch_service_id("google")
        self.service_routing_plugin.enter_service_launch_data('')
        self.service_routing_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_routing_plugin.close_all_toast_popups()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'google'
        assert launch_result['instanceId'] == self.service_routing_plugin.get_service_launch_result()['instanceId']

    def test_22__verify_launch_cloud_service_with_invalid_manifest_https_url(self, enable_mocked_data):
        """
        C32357878: Launch a cloud service with an invalid manifest HTTPS URL
        """
        self.service_routing_plugin.enter_launch_service_id("InvalidManifest")
        self.service_routing_plugin.enter_service_launch_data('')
        self.service_routing_plugin.select_launch_service_test_btn()
        result = self.service_routing_plugin.get_service_launch_result()
        assert self.service_routing_plugin.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    def test_23_retrieve_launch_options_from_current_service(self, enable_mocked_data):
        """
        C29408939: Retrieve the launch options from the current service instance of a cloud service
        - Verify that launch options are maintained
        """
        self.service_routing_plugin.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.service_routing_plugin.enter_service_launch_data('{"test":"test"}')
        self.service_routing_plugin.select_transition_drop_down_menu()
        self.service_routing_plugin.select_transition_option_from_menu("forward")
        self.service_routing_plugin.select_launch_service_test_btn()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        self.service_routing_plugin.select_get_service_instance_launch_options_test_btn()
        service_instance_result = self.service_routing_plugin.get_launch_service_options_result_text()
        assert service_instance_result['serviceOptions']['test'] == 'test'
        assert service_instance_result['transitionType'] == 'FORWARD'
        assert service_instance_result['serviceId'] == "abcdefaa-c338-4d40-8185-3dd13d88999f"
    
    def test_24_verify_close_serivce_instance(self, enable_mocked_data):
        """
        C30299006: Close a service instance
        """
        self.service_routing_plugin.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.service_routing_plugin.enter_service_launch_data('{"test":"test"}')
        self.service_routing_plugin.select_transition_drop_down_menu()
        self.service_routing_plugin.select_transition_option_from_menu("forward")
        self.service_routing_plugin.select_launch_service_test_btn()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        self.service_routing_plugin.close_all_toast_popups()
        self.home.select_service_routing_tab()
        self.home.select_weblet_tab()
        self.service_routing_plugin.select_close_service_instance_test_btn()

    def test_25_retrieve_launch_options_from_current_instance_service(self, enable_mocked_data):
        """
        C29458363: Retrieve the launch options from the current service instance of a service
        - Verify that launch options are maintained
        """
        self.service_routing_plugin.enter_launch_service_id("openUrl")
        self.service_routing_plugin.enter_service_launch_data('{"url": "https://appassets.androidplatform.net/Weblets/index.html"}')
        self.service_routing_plugin.select_transition_drop_down_menu()
        self.service_routing_plugin.select_transition_option_from_menu("forward")
        self.service_routing_plugin.select_launch_service_test_btn()
        launch_result = self.service_routing_plugin.get_service_launch_result()
        self.service_routing_plugin.close_all_toast_popups()
        self.service_routing_plugin.select_get_service_instance_launch_options_test_btn()
        service_instance_result = self.service_routing_plugin.get_launch_service_options_result_text()
        assert service_instance_result['serviceOptions']['url'] == 'https://appassets.androidplatform.net/Weblets/index.html'
        assert service_instance_result['transitionType'] == 'FORWARD'
        assert service_instance_result['serviceId'] == "openUrl"