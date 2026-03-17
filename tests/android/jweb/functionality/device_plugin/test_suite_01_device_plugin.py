import pytest
from MobileApps.resources.const.web.const import TEST_DATA 

pytest.app_info = "JWEB"

class Test_Suite_01_Device_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.device_plugin = cls.fc.fd["device_plugin"]
        # Language codes as of ISO 639-1
        cls.languages = TEST_DATA.ISO_LANGUAGE_LIST

    def test_01_verify_device_info(self):
        """
        verify pressing the test button in Device.getInfo() returns the information of a device
        
        TestRails -> C28698083
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("device")
        self.device_plugin.press_device_info_test_btn()
        device_info = self.device_plugin.return_device_info()
        assert device_info["platform"] == "android" 
        assert device_info["model"] != ""
        assert device_info["osVersion"] != ""

    def test_02_verify_device_language_code(self):
        """
        verify pressing the test button in Device.getLanguageCode() returns the device's current language locale code
        
        TestRails -> C28698084
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("device")
        self.device_plugin.press_language_test_btn()
        language_code = self.device_plugin.return_language_test_result()['value']
        assert language_code[:2].lower() in self.languages