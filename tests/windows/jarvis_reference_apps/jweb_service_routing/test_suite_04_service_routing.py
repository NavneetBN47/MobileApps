import pytest

class Test_Suite_04_Service_Routing_Advanced_Operations(object):

    @pytest.mark.servicerouting
    def test_01_retrieve_launch_options_from_current_service_C29408939(self):
        """
        C29408939: Retrieve the launch options from the current service instance of a cloud service
            - Navigate to the Service Routing Plugin
            - Under launchService() enter service id of the local JWeblet service, inserting valid service launch options
            - Under launchService() set transition type to forward and select test
            - Navigate back to the Service Routing Plugin and under getServiceInstanceLaunchOptions() click test
            - Expecting json value to be returned detailing current service launch options, transition type, and service id
        """
        self.service_routing.enter_launch_service_id("abcdefaa-c338-4d40-8185-3dd13d88999f")
        self.service_routing.enter_service_launch_data('{"test":"test"}')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.select_launch_service_options_availability_test_btn()
        service_option_results = self.service_routing.get_launch_service_options_result_text()
        assert service_option_results['serviceOptions'] == {'test': 'test'}
        assert service_option_results['transitionType'] == 'forward'
        assert service_option_results['serviceId'] == "abcdefaa-c338-4d40-8185-3dd13d88999f"

    @pytest.mark.servicerouting
    def test_02_retrieve_current_state_of_service_after_launching_C65858262(self):
        """
        C65858262: Retrieve the current state of a service after launching it
        """
        self.service_routing.enter_launch_service_id("openUrl")
        self.service_routing.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_routing.select_toggle_under_launch_service(True)
        self.service_routing.select_launch_service_test_btn()
        self.service_routing.select_back_btn(hidden_button=True)
        self.service_routing.select_get_service_instance_test_btn()
        service_instance_result = self.service_routing.get_service_instance_result()
        assert service_instance_result['instanceId'] == self.service_routing.get_service_launch_result()['instanceId']
        assert service_instance_result['serviceId'] == 'openUrl'
        assert service_instance_result['state'] == 'closed'

    @pytest.mark.servicerouting
    def test_03_retrieve_launch_options_from_current_service_instance_C65858260(self):
        """
        C65858260: Retrieve the launch options from the current service instance of the service
        """
        self.service_routing.enter_launch_service_id("openUrl")
        self.service_routing.enter_service_launch_data('{"url": "jweb://localhost/index.html"}')
        self.service_routing.select_transition_drop_down_menu()
        self.service_routing.select_transition_option_from_menu("forward")
        self.service_routing.select_launch_service_test_btn()
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.select_launch_service_options_availability_test_btn()
        service_instance_launch_result = self.service_routing.get_launch_service_options_result_text()
        assert service_instance_launch_result['serviceOptions'] == self.service_routing.get_launch_service_options_result_text()['serviceOptions']
        assert service_instance_launch_result['serviceId'] == 'openUrl'
        assert service_instance_launch_result['transitionType'] == 'forward'

    def test_04_launch_openUrl_service_using_whitelisted_HTTPS_URL_navbar_off_C33548601(self):
        """
        C33548601: Launch the openUrl service using a whitelisted HTTPS URL with DisplayUnderNavbar off
        """
        self.service_routing.select_custom_plugin_from_side_menu()
        self.service_routing.select_setting_tab()
        self.service_routing.select_toggle_under_settings_tab(True)
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.enter_launch_service_id("openUrl")
        self.service_routing.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_routing.select_toggle_under_launch_service(False)
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.verify_done_btn() is not True

    def test_05_launch_openUrl_service_using_whitelisted_HTTPS_URL_navbar_on_C33548602(self):
        """
        C33548602: Launch the openUrl service using a whitelisted HTTPS URL with DisplayUnderNavbar on
        """
        self.service_routing.select_custom_plugin_from_side_menu()
        self.service_routing.select_setting_tab()
        self.service_routing.select_toggle_under_settings_tab(True)
        self.weblet_home.select_plugin_from_home("service routing")
        self.service_routing.enter_launch_service_id("openUrl")
        self.service_routing.enter_service_launch_data('{"url": "https://www.hpsmartdev.com"}')
        self.service_routing.select_toggle_under_launch_service(True)
        self.service_routing.select_launch_service_test_btn()
        assert self.service_routing.verify_done_btn() is not True