import pytest
from MobileApps.resources.const.web.const import TEST_DATA 

pytest.app_info = "JWEB"

class Test_Suite_01_Device_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, jweb_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.device_plugin = cls.fc.fd["device_plugin"]
        # Language codes as of ISO 639-1
        cls.languages = TEST_DATA.ISO_LANGUAGE_LIST

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_device_plugin(self):
        if not self.device_plugin.verify_at_device_plugin():
            self.driver.restart_app()
            self.home.select_webview_mode(raise_e=False)
            self.home.select_jweb_reference_btn(raise_e=False)
            self.home.select_url_go_btn(raise_e=False)
            self.home.select_plugin_from_home("device")

    def test_01_verify_device_info(self):
        """
        verify pressing the test button in Device.getInfo() returns the information of a device
        
        TestRails -> C28698083
        """
        self.device_plugin.press_device_info_test_btn()
        device_info = self.device_plugin.return_device_info()
        assert device_info["platform"].lower() == 'windows'

    def test_02_verify_device_language_code(self):
        """
        verify pressing the test button in Device.getLanguageCode() returns the device's current language locale code
        
        TestRails -> C28698084
        """
        self.device_plugin.press_language_test_btn()
        language_code = self.device_plugin.return_language_test_result()['value']
        assert language_code[:2].lower() in self.languages 

    def test_03_verify_whether_the_network_connection_status_is_available(self):
        """
        Verify whether the network connection status is available in the Device.getInfo() method

        TestRails -> C57072615
        """
        self.device_plugin.press_device_info_test_btn()
        device_info = self.device_plugin.return_device_info()
        assert device_info["isInternetConnected"].lower() == 'true'

    def test_04_verify_the_response_in_the_device_getinfo_when_the_device_is_having_arm_architecture(self):
        """
        Verify the response in the Device.getInfo() when the device is having ARM architecture

        TestRails -> C59251494
        """
        self.device_plugin.press_device_info_test_btn()
        device_info = self.device_plugin.return_device_info()
        assert device_info["architecture"] == 'x64'

    def test_05_validating_the_device_api_to_extract_the_appearance_when_device_display_dark_settings(self):
        """
        Validating the Device API to extract the appearance information of the device- when device display has dark settings
 
        TestRails -> C33618420
        """ 
        self.device_plugin.press_device_info_test_btn()
        result = self.device_plugin.return_device_info()
        assert result["appearance"] == "light"
        assert result["isInternetConnected"] == "true"
 
    def test_06_validating_the_device_api_to_extract_the_appearance_when_device_display_light_settings(self):
        """
        Validating the Device API to extract the appearance information of the device- when device display has light settings
 
        TestRails -> C33618422
        """
        self.device_plugin.press_device_info_test_btn()
        result = self.device_plugin.return_device_info()
        assert result["appearance"] != "dark"
        assert result["isInternetConnected"] == "true"