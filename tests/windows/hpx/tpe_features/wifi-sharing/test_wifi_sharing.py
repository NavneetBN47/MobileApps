from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Wifi(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(5)

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["testudo"])
    def test_01_wifi_show_device_page_C39033312(self):
        self.fc.restart_myHP()
        time.sleep(2)

        assert bool(self.fc.verify_wifi_card_show_on_home_page()) is True, "wifi sharing page not displayed on home page"

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["pc_device"].verify_wifi_sharing_show_on_device_page()) is True, "wifi sharing page not displayed on device page"

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["testudo"])
    def test_02_check_wifi_sharing_ui_C38338468(self):
        self.fc.restart_myHP()
        time.sleep(2)

        assert bool(self.fc.verify_wifi_sharing_title_show()) is True, "wifi sharing title is not displayed"
        assert bool(self.fc.verify_wifi_sharing_subtitle_show()) is True, "wifi sharing subtitle is not displayed"
        assert bool(self.fc.verify_wifi_sharing_first_one_title_show()) is True, "wifi sharing first one title is not displayed"
        assert bool(self.fc.verify_wifi_sharing_first_one_image_show()) is True, "wifi sharing first one image is not displayed"
        assert bool(self.fc.verify_wifi_sharing_second_one_title_show()) is True, "wifi sharing second one title is not displayed"
        assert bool(self.fc.verify_wifi_sharing_second_one_image_show()) is True, "wifi sharing second one image is not displayed"
        assert bool(self.fc.verify_wifi_sharing_third_one_title_show()) is True, "wifi sharing third one title is not displayed"
        assert bool(self.fc.verify_wifi_sharing_third_one_image_show()) is True, "wifi sharing third one image is not displayed"
        assert bool(self.fc.verify_windows_network_settings_button_show()) is True, "windows network settings button is not displayed"
