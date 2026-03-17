import pytest
pytest.app_info = "JWEB_SERVICE_ROUTING"

class Test_Suite_01_Service_Routing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_service_routing_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_service_routing_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.native_weblet = cls.fc.fd["weblet"]
        cls.web_home = cls.fc.fd["web_home"]
        cls.settings_plugin = cls.fc.fd["settings_plugin"]
        cls.service_routing = cls.fc.fd["service_routing"]

        # Set stack to Mock
        cls.fc.navigate_and_change_stack_option('Mock')

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_weblet(self):
        """
        Launch application and select the weblet tab
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab_btn()
        
    def test_01_verify_list_of_supported_services(self):
        """
        C28698127: Retrieve the list of supported services 
        - After selecting test btn in getServices() tab, verify that a list of supported services is present 
        """
        self.service_routing.select_get_services_test_btn()
        assert 'services' in self.service_routing.get_services_result()

    def test_02_verify_service_availability_using_service_id(self):
        """
        C28698128: Verify the service availability using the service id
        - After selecting test btn in getServices() tab, verify that a list of supported services is present
        """
        self.native_weblet.enter_service_availability_id("C")
        self.service_routing.select_get_service_availability_test_btn()
        assert 'id' in self.service_routing.get_service_availability_result()

    def test_03_verify_launch_error_with_invalid_service_id(self):
        """
        C28702704: Launch a service with an invalid service id
        - Enter invalid service id into the service availability id field, and verify that 'serviceNotFound' error is produced
        """
        self.native_weblet.enter_service_availability_id("this_is_an_invalid_service_id")
        self.service_routing.select_get_service_availability_test_btn()
        assert 'serviceNotFound' in self.service_routing.get_service_availability_result()["errorType"]

    def test_04_verify_launch_native_service_available_plugins_services(self):
        """
        C29391638: Launch a native service when the required plugins and services are available
        - Launching native service, assert launch service result
        """
        self.native_weblet.enter_launch_service_id("HelloWorld")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_weblet_back_btn()
        
        launch_result = self.service_routing.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'HelloWorld' 
        assert launch_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']

    def test_05_verify_launch_error_with_unavailable_plugin(self):
        """
        C29391639: Launch a native service when a required plugin is not available
        - After trying to launch a native service which depends on unavailable plugin, verify error is thrown
        """
        self.native_weblet.enter_launch_service_id("NativeService_Invalid_Plugins")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    def test_06_verify_launch_error_with_unavailable_service(self):
        """
        C29391640: Launch a native service when a required service is not available
        - After trying to launch a native service which depends on unavailable service, verify error is thrown
        """
        self.native_weblet.enter_launch_service_id("NativeService_Invalid_Services")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    def test_07_verify_state_of_launched_native_service(self):
        """
        C29458310: Retrieve the current state of a native service after launching it
        - After launching service, verify getServiceInstance() result is valid
        """
        self.native_weblet.enter_launch_service_id("HelloWorld")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_weblet_back_btn()
        self.service_routing.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'HelloWorld'
        assert service_instance_result['state'] == 'closed'

    def test_08_verify_launch_cloud_service_with_any_https_url(self):
        """
        C29391643: Launch a cloud service with any HTTPS URL and the required plugins and services available when enforce whitelist toggle is OFF
        - After enforcing whitelist toggle is off, and launching cloud service with https url, verify service results
        """
        self.web_home.select_plugin_from_home("settings")
        self.settings_plugin.select_enforce_navigation_toggle(False)
        self.web_home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("7d65350e-64f6-4a2f-8191-0aa81d33e3c7")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_done_btn()

        launch_result = self.service_routing.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == '7d65350e-64f6-4a2f-8191-0aa81d33e3c7'
        assert launch_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
    
    def test_09_verify_launch_error_required_plugin_unavailable(self):
        """
        C29391644: Launch a cloud service when a required plugin is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.native_weblet.enter_launch_service_id("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    def test_10_verify_launch_error_required_service_unavailable(self):
        """
        C29391645: Launch a cloud service when a required service is not available
        - Launch a cloud service when a required plugin is not available, verify error
        """
        self.native_weblet.enter_launch_service_id("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    def test_11_verify_launch_error_invalid_url(self):
        """
        C29391646: Launch a cloud service with an invalid URL (not HTTPS nor JWEB scheme)
        - Launch a cloud service with an invalid URL, verify error
        """
        self.native_weblet.enter_launch_service_id("NonHttps")
        self.native_weblet.enter_service_launch_data('')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        assert 'serviceNotSupported' in self.service_routing.get_service_launch_result()['errorType']
        assert 'Expected https' in self.service_routing.get_service_launch_result()['reason']

    def test_12_verify_launch_error_bad_url(self):
        """
        C29391647: Launch a cloud service with a blank URL 
        - Launch a cloud service with an blank URL, verify error
        """
        self.native_weblet.enter_launch_service_id("BadURL")
        self.native_weblet.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'

    def test_13_verify_current_state_post_cloud_service_launch(self):
        """
        C29458311: Retrieve the current state of a cloud service after launching it
        - Launch a cloud service, verify status after launch
        """
        self.native_weblet.enter_launch_service_id("7d65350e-64f6-4a2f-8191-0aa81d33e3c7")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_done_btn()
        self.service_routing.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == '7d65350e-64f6-4a2f-8191-0aa81d33e3c7'
        assert service_instance_result['state'] == 'closed'

    def test_14_retrieve_launch_options_from_current_service(self):
        """
        C29408939: Retrieve the launch options from the current service instance of a cloud service
        - Verify that launch options are maintained
        """
        self.native_weblet.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.native_weblet.enter_service_launch_data('{"test":"test"}')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_menu()
        self.native_weblet.select_plugins_tab_from_menu()
        self.native_weblet.select_service_routing_plugin()
        self.native_weblet.select_launch_service_options_availability_test_btn()
        service_option_results = self.native_weblet.get_launch_service_options_result_text()
        assert service_option_results['serviceOptions'] == {'test': 'test'}
        assert service_option_results['transitionType'] == 'forward'
        assert service_option_results['serviceId'] == "abcdefaa-c338-4d40-8185-3dd13d88999f"

    def test_15_verify_launch_cloud_service_with_whitelisted_https_url(self):
        """
        C29519784: Launch a cloud service with a whitelisted HTTPS URL when enforce whitelist toggle is ON
        """
        self.web_home.select_plugin_from_home("settings")
        self.settings_plugin.select_enforce_navigation_toggle(True)
        self.web_home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("HelloWorld")
        self.native_weblet.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_weblet_back_btn()
        launch_result = self.service_routing.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'HelloWorld'
        assert launch_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']

    def test_16_verify_launch_cloud_service_with_invalid_manifest_https_url(self):
        """
        C32357878: Launch a cloud service with an invalid manifest HTTPS URL
        """
        self.native_weblet.enter_launch_service_id("NonHttps")
        self.native_weblet.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        result = self.service_routing.get_service_launch_result()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Expected https or jweb URL scheme'

    def test_17_verify_close_service_instance(self):
        """
        C30299006: Close a service instance
        """
        self.native_weblet.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.native_weblet.enter_service_launch_data('{"test":"test"}')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_menu()
        self.native_weblet.select_plugins_tab_from_menu()
        self.native_weblet.select_service_routing_plugin()
        self.native_weblet.select_close_service_options_test_btn()
        assert 'closed' in self.service_routing.get_event_notification_text(get_json=False)

    def test_18_verify_refresh_the_list_of_supported_services(self):
        """
        C29406175: Refresh the list of supported services
        """
        self.service_routing.select_get_services_test_btn()
        assert 'services' in self.service_routing.get_services_result()
        self.fc.navigate_and_change_stack_option('Pie')
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab_btn()
        self.service_routing.select_refresh_available_services_from_repo()
        self.service_routing.select_get_services_test_btn()
        assert 'services' in self.service_routing.get_services_result()

    def test_19_validate_response_invalid_url(self):
        """
        C28711671: Validate response when invalid URL is provided
        """
        self.native_weblet.enter_service_launch_data('{"url": "://localhost:3000/index.html#/eventing"}')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Expected https or jweb URL scheme'

    def test_20_validate_response_blank_url(self):
        """
        C29388288: Validate response when blank URL is provided
        """
        self.native_weblet.enter_service_launch_data('{"url": ""}')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Invalid service options'

    def test_21_retrieve_current_state_of_service_after_launching(self):
        """
        C28698130: Retrieve the current state of a service after launching it
        """
        self.web_home.select_plugin_from_home("settings")
        self.settings_plugin.select_enforce_navigation_toggle(True)
        self.web_home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_routing.select_display_under_navbar_toggle()
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_done_btn()
        self.service_routing.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'openUrl'
        assert service_instance_result['state'] == 'closed'

    def test_22_retrieve_launch_options_from_current_service_instance(self):
        """
        C29458363: Retrieve the launch options from the current service instance of a service
        """
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url": "jweb://localhost/index.html"}')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_menu()
        self.native_weblet.select_plugins_tab_from_menu()
        self.native_weblet.select_service_routing_plugin()
        self.native_weblet.select_launch_service_options_availability_test_btn()
        service_option_results = self.native_weblet.get_launch_service_options_result_text()
        assert service_option_results['serviceOptions'] == self.native_weblet.get_launch_service_options_result_text()['serviceOptions']
        assert service_option_results['transitionType'] == 'forward'
        assert service_option_results['serviceId'] == "openUrl"

    def test_23_launch_open_url_service_using_whitelisted_https_url_navbar_off(self):
        """
        C33548601: Launch openUrl service using whitelisted https URL with navbar off
        """
        self.web_home.select_plugin_from_home("settings")
        self.settings_plugin.select_enforce_navigation_toggle(True)
        self.web_home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url":"https://www.hpsmart.com"}')
        self.service_routing.select_launch_service_test_btn()
        assert self.native_weblet.verify_done_btn() is not True
    
    def test_24_launch_open_url_service_using_whitelisted_https_url_navbar_on(self):
        """
        C33548602: Launch openUrl service using whitelisted https URL with navbar on
        """
        self.web_home.select_plugin_from_home("settings")
        self.settings_plugin.select_enforce_navigation_toggle(True)
        self.web_home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("openUrl")
        self.native_weblet.enter_service_launch_data('{"url":"https://www.hpsmart.com"}')
        self.service_routing.select_display_under_navbar_toggle()
        self.service_routing.select_launch_service_test_btn()
        assert self.native_weblet.verify_done_btn() is not False

    def test_25_verify_launch_cloud_service_with_non_whitelisted_https_url(self):
        """
        C29519785: Launch a cloud service with a non-whitelisted HTTPS URL and the required plugins and services available when enforce whitelist toggle is ON
        """
        self.fc.navigate_and_change_stack_option('Mock')
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab_btn()
        self.web_home.select_plugin_from_home("settings")
        self.settings_plugin.select_enforce_navigation_toggle(True)
        self.web_home.select_plugin_from_home("service_routing")
        self.native_weblet.enter_launch_service_id("google")
        self.native_weblet.enter_service_launch_data('')
        self.service_routing.select_display_under_navbar_toggle()
        self.service_routing.select_launch_service_test_btn()
        self.native_weblet.select_weblet_back_btn()
        launch_result = self.service_routing.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'google'
        assert launch_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']