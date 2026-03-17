import pytest
from time import sleep

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.app = cls.fc.fd["app_plugin"]

    def test_01_listener_status(self):
        """
        C28909515: Verify if a toast pops up when using back button after adding listener
        C28909517: Verify if a toast doesn't pop up when using back button after removing listener
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("app")
        self.app.select_add_listener_btn()
        assert self.app.get_pop_up_toast_text() == "Listener added"
        sleep(5)
        self.driver.press_key_back()
        assert self.app.get_pop_up_toast_text() == "Back button pressed!"
        self.app.select_remove_listener_btn()
        assert self.app.get_pop_up_toast_text() == "Listener removed"
        sleep(5)
        self.driver.press_key_back()
        assert self.home.verify_main_page() != False

    def test_02_listener_stays_within_app_plugin(self):
        """
        C28909519: Verify if listener is removed when leaving App plugin
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("app")
        self.app.select_add_listener_btn()
        assert self.app.get_pop_up_toast_text() == "Listener added"
        sleep(5)
        self.home.select_plugin_from_home("device")
        self.driver.press_key_back()
        assert self.app.verify_app_plugin() != False
        self.driver.press_key_back()
        assert self.home.verify_main_page() != False