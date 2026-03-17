import pytest
import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.gotham.web_popup import WEBPOPUP
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_01_Web_Popup(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.webpopup = WEBPOPUP(cls.driver)

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_click_open_app_checkbox(self):
        self.web_driver.set_size("phone")
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.click_accept_all_btn()
        self.ows_value_prop.select_native_value_prop_buttons(index=1)
        self.web_driver.wait_for_new_window(timeout=15)
        self.web_driver.add_window('web_login')
        time.sleep(3)
        self.web_driver.switch_window('web_login')
        self.web_driver.set_size("max")
        time.sleep(2)
        self.hpid.login(self.login_info["email"], self.login_info["password"])
        if self.webpopup.verify_save_password_popup():
            self.webpopup.click_save_password_never_button()
        self.webpopup.click_always_allow_checkbox()
        self.webpopup.click_web_hpid_open_btn()
        self.home.verify_home_screen()

    def test_02_close_web_windows(self):
        self.web_driver.set_size("phone")
        self.web_driver.set_size('min')
        
