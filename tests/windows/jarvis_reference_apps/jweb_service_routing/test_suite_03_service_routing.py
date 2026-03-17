import pytest

class Test_Suite_03_Service_Routing_URL_Validation(object):

    @pytest.mark.servicerouting
    def test_01_verify_launch_error_invalid_url_C29391646(self):
        """
        C29391646: Launch a cloud service with an invalid URL (not HTTPS or JWEB scheme)
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of a cloud service with a non-HTTPS URL, leaving the service launch data field blank
            - After clicking on the launchService() test btn, we expect an "invalidOptions" error to be returned
        """
        self.service_routing.enter_launch_service_id("NonHttps")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    @pytest.mark.servicerouting
    def test_02_verify_launch_error_bad_url_C29391647(self):
        """
        C29391647: Launch a cloud service with a blank URL
            - Navigate to the Service Routing Plugin
            - Under launchService() enter the service id of the cloud service with a blank URL, leaving the service launch data field blank
            - After clicking on the launchService() test btn, we expect an "invalidOptions" error to be returned
        """
        self.service_routing.enter_launch_service_id("BadURL")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'

    @pytest.mark.servicerouting
    def test_03_verify_launch_cloud_service_with_invalid_manifest_https_url_C32357878(self):
        """
        C32357878: Launch a cloud service with an invalid manifest HTTPS URL
        """
        self.service_routing.enter_launch_service_id("NonHttps")
        self.service_routing.enter_service_launch_data('')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_04_validate_response_invalid_url_C28711671(self):
        """
        C28711671:  Validate response when invalid URL is provided
        """
        self.service_routing.enter_service_launch_data('{"url": "://localhost:3000/index.html#/eventing"}')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'

    def test_05_validate_response_blank_url_C29388288(self):
        """
        C29388288: Validate response when blank URL is provided
        """
        self.service_routing.enter_service_launch_data('{"url": ""}')
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.get_service_launch_result()['errorType'] == 'invalidOptions'
        assert self.service_routing.get_service_launch_result()['reason'] == 'Invalid Url. Scheme not specified.'