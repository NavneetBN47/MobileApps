import pytest

class Test_Suite_01_Service_Routing(object):

    @pytest.mark.servicerouting
    def test_01_verify_launch_native_service_available_plugins_services_C29391638(self):
        """
        C29391638: Launch a native service when the required plugins and services are available
            - Navigate to the Service Routing Plugin
            - Under launchService(), enter "HelloWorld" service id and click on test btn
            - Close the service returning to the Service Routing Plugin
            - Expecting a json value with service details returned under launchService()
        """
        self.service_routing.enter_launch_service_id("HelloWorld")
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.select_back_btn()
        launch_result = self.service_routing.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == 'helloWorld' 
        assert 'instanceId' in launch_result

    @pytest.mark.servicerouting
    def test_02_verify_state_of_launched_native_service_C29458310(self):
        """
        C29458310: Retrieve the current state of a service after launching it
            - Navigate to the Service Routing Plugin
            - Under launchService(), enter "HelloWorld" service id and click on test btn
            - Close the service returning to the Service Routing Plugin
            - Under getServiceInstance() click on test btn
            - Expecting json value to be returned detailing the closed state of the just launched service
        """
        self.service_routing.enter_launch_service_id("HelloWorld")
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.select_back_btn()
        self.service_routing.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'helloWorld'
        assert service_instance_result['state'] == 'closed'

    @pytest.mark.servicerouting
    def test_03_verify_launch_error_with_unavailable_plugin_C29391639(self):
        """
        C29391639: Launch a native service when a required plugin is not available
        -After trying to launch a native service which depends on unavailable pluging, verify error is thrown
        """
        self.service_routing.enter_launch_service_id("NativeService_Invalid_Plugins")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotFound'

    @pytest.mark.servicerouting
    def test_04_verify_launch_error_with_unavailable_service_C29391640(self):
        """
        C29391640: Launch a native service when a required service is not available
        -After trying to launch a native service which depends on unavailable service, verify error is thrown
        """
        self.service_routing.enter_launch_service_id("NativeService_Invalid_Services")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotFound'

    @pytest.mark.servicerouting
    def test_05_verify_launch_cloud_service_with_whitelisted_https_url_C29519784(self):
        """
        C29519784: Launch a cloud service with a whitelisted HTTPS URL when enforce whitelist toggle is ON
        """
        self.service_routing.select_custom_plugin_from_side_menu()
        self.service_routing.select_setting_tab()
        self.service_routing.select_toggle_under_settings_tab(True)
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.enter_launch_service_id("HelloWorld")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.select_left_go_back_button()
        result = self.service_routing.get_service_launch_result()
        assert result['state'] == 'launching'
        assert result['serviceId'] == 'helloWorld'
        assert result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        self.home.select_weblet_btn(raise_e=False)