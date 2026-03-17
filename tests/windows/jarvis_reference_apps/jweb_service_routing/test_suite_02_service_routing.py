import pytest

class Test_Suite_02_Service_Routing_Cloud_Services(object):

    @pytest.mark.servicerouting
    def test_01_verify_launch_cloud_service_with_any_https_url_C29391643(self):
        """
        C29391643: Launch a cloud service with any HTTPS Url and the required plugins and services available when whitelisting toggle is off
            - Whitelisting URL is toggled off by default in the Windows Service Routing Application
            - Navigate to the Service Routing Plugin
            - Under launchService(), enter service id for valid HTTPS URL ("7d65350e-64f6-4a2f-8191-0aa81d33e3c7") and click on test btn
            - Close the  service returning to the Service Routing Plugin
            - Expecting json value to be returned detailing the launching state of the service
        """
        self.service_routing.enter_launch_service_id("7d65350e-64f6-4a2f-8191-0aa81d33e3c7")
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.select_back_btn(hidden_button=True)
        launch_result = self.service_routing.get_service_launch_result()
        assert launch_result['state'] == 'launching'
        assert launch_result['serviceId'] == '7d65350e-64f6-4a2f-8191-0aa81d33e3c7'
        assert launch_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']

    @pytest.mark.servicerouting
    def test_02_verify_launch_error_required_plugin_unavailable_C29391644(self):
        """
        C29391644: Launch a cloud service when a required plugin is not available
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of a cloud service that depends on an unavailable plugin ("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
            - After clicking on the launchService() test btn, we expect a "serviceNotSupported" error to be returned
        """
        self.service_routing.enter_launch_service_id("eb4d02eb-fc75-4a59-aefa-d812a35e560a")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    @pytest.mark.servicerouting
    def test_03_verify_launch_error_required_service_unavailable_C29391645(self):
        """
        C29391645: Launch a cloud service when a required service is not available 
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of a cloud service that depends on an unavailable service ("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
            - After clicking on the launchService() test btn, we expect a "serviceNotSupported" error to be returned
        """
        self.service_routing.enter_launch_service_id("8a4c111f-568a-4e3c-a04b-fee1808b7e0e")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'serviceNotSupported'

    @pytest.mark.servicerouting
    def test_04_verify_current_state_post_cloud_service_launch_C29458311(self):
        """
        C29458311: Retrieve the current state of a cloud service after launching it
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of the available cloud service
            - Close the service, which should auto-populate the getServiceInstance() service id field with the last launched service
            - Under getServiceInstance() click on test btn
            - Expecting json value to be returned with service launch details including a closed state
        """
        self.service_routing.enter_launch_service_id("7d65350e-64f6-4a2f-8191-0aa81d33e3c7")
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.select_back_btn(hidden_button=True)
        self.service_routing.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == '7d65350e-64f6-4a2f-8191-0aa81d33e3c7'
        assert service_instance_result['state'] == 'closed'

    @pytest.mark.servicerouting
    def test_05_verify_launch_cloud_service_with_non_whitelisted_https_url_C29519785(self):
        """
        C29519785: Launch a cloud service with a non-whitelisted HTTPS URL and the required plugins and services available when enforce whitelist toggle is ON
        """
        self.service_routing.select_custom_plugin_from_side_menu()
        self.service_routing.select_setting_tab()
        self.service_routing.select_toggle_under_settings_tab(True)
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.enter_launch_service_id("google")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.back_btn_after_launching_activity()
        result = self.service_routing.get_service_launch_result()
        assert result['state'] == 'launching'
        assert result['serviceId'] == 'google'
        assert result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']