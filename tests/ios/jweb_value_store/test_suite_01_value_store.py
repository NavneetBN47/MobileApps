import pytest
pytest.app_info = "JWEB_VALUE_STORE"

class Test_Suite_01_Value_Store(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_value_store_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_value_store_setup

        cls.home = cls.fc.fd["home"]
        cls.native = cls.fc.fd["native"]
        cls.value_store_plugin = cls.fc.fd["value_store_plugin"]

    def test_01_verify_native_screen(self):
        """
        C36117612: Verify the Native screen tab in value
            - Verify the Get, Set, Remove buttons are present on the Native Tab
        """
        self.native.verify_native_view_buttons()

    def test_02_verify_weblet_screen(self):
        """
        C36117613: Verify the Weblet screen tab in value
            - Verify the Get, Set, Remove buttons are present in the Value Store Weblet
        """
        self.home.select_weblet_tab_nav()
        self.value_store_plugin.verify_weblet_view_buttons()
