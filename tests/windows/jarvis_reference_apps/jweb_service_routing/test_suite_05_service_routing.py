import pytest

class Test_Suite_05_Service_Routing_Service_Management(object):

    @pytest.mark.servicerouting
    def test_01_verify_list_of_supported_services_C28698127(self):
        """
        C28698127: Retrieve the list of supported services
            - After navigating to the Service Routing Plugin, select the test btn under the getServices() tab
            - verify that the list of supported services is present
        """
        self.service_routing.select_get_services_test_btn()
        assert 'services' in self.service_routing.get_services_result(), "services not found in ServiceRouting.getServices()"

    @pytest.mark.servicerouting
    def test_02_verify_service_availability_using_service_id_C28698128(self):
        """
        C28698128: Verify the service availability using the service id
            - Navigate to the Service Routing Plugin
            - Within the getServiceAvailability() tab, enter a valid service_id ("C") and select the test btn
            - Expecting a json value with "serviceId": "C" to be returned
        """
        self.service_routing.enter_service_availability_id("C")
        self.service_routing.select_get_service_availability_test_btn()
        assert 'serviceId' in self.service_routing.get_service_availability_result()

    @pytest.mark.servicerouting
    def test_03_verify_launch_error_with_invalid_service_id_C28702704(self):
        """
        C28702704: Launch a service with an invalid service id
            - Navigate to the Service Routing Plugin
            - Within the getServiceAvailability() tab, enter an invalid service_id and select the test btn
            - Expecting a serviceNotFound error message
        """
        self.service_routing.enter_service_availability_id("this_is_an_invalid_service_id")
        self.service_routing.select_get_service_availability_test_btn()
        assert 'serviceNotFound' in self.service_routing.get_service_availability_result()["errorType"]

    @pytest.mark.servicerouting
    def test_04_verify_refresh_the_list_of_supported_services_C29406175(self):
        """
        C29406175: Refresh the list of supported services from the repository
        """
        self.service_routing.select_get_services_test_btn()
        assert 'services' in self.service_routing.get_services_result(), "services not found in ServiceRouting.getServices()"
        self.home.select_home_btn()
        self.home.select_settings_btn()
        self.home.change_stack('Local')
        self.home.select_weblet_btn(raise_e=False)
        self.service_routing.select_refresh_available_services_from_repo()
        self.service_routing.select_get_services_test_btn()
        assert 'services' in self.service_routing.get_services_result(), "services not found in ServiceRouting.getServices()"

    @pytest.mark.servicerouting
    def test_05_verify_close_service_instance_C30299006(self):
        """
        C30299006: Close a service instance
        """
        self.service_routing.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.service_routing.enter_service_launch_data('{"test":"test"}')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.select_close_service_instance_test_btn()
        assert 'CLOSED' in self.service_routing.get_event_notification_text()