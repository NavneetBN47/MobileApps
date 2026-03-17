import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest

pytest.app_info = "HPX"
class Test_Suite_Dropbox(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)

    def test_01_show_sigi_in_error_message_C32242364(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()

        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()
        
        time.sleep(2)
        self.fc.fd["dropbox"].enter_sign_in_email("<><>></")
        time.sleep(2)
        assert self.fc.fd["dropbox"].get_sign_in_email_error_message() == "A valid email is required."
    
    def test_02_show_sign_up_error_message_C32242437(self):
        
        time.sleep(2)
        self.fc.fd["dropbox"].navigate_to_sign_up_page()
        assert self.fc.fd["dropbox"].verify_sign_up_header_show() is True

        time.sleep(2)
        self.fc.fd["dropbox"].enter_sign_up_first_name("<><>></")
        time.sleep(3)
        assert self.fc.fd["dropbox"].get_firstName_invalid_data_message() == "A valid first name is required."
        self.fc.fd["dropbox"].enter_sign_up_last_name("<><>></")
        time.sleep(3)
        assert self.fc.fd["dropbox"].get_lastName_invalid_data_message() == "A valid last name is required."
        self.fc.fd["dropbox"].enter_sign_up_email_address("<><>></")
        time.sleep(3)
        self.fc.fd["dropbox"].get_email_invalid_data_message()
        assert self.fc.fd["dropbox"].get_email_invalid_data_message() == "A valid email is required."

    def test_03_skipButton_C32239561(self, install_app):

        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()


        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()

        time.sleep(2)
        self.fc.fd["dropbox"].click_skip_button()
        assert self.fc.fd["express_vpn"].verify_express_vpn_header_show() is True

    # def test_04_links_clickable_online(self, install_app):
        
    #     self.fc.re_install_app(install_app)
    #     time.sleep(5)
    #     self.fc.launch_app()

    #     if self.fc.fd["hp_login"].verfiy_login_page_show():
    #         self.fc.fd["hp_login"].close_login_page()

    #     if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
    #         self.fc.fd["hp_privacy_setting"].click_decline_all_button()
    #     assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
    #     self.fc.fd["hp_registration"].click_skip_button()
        
    #     self.fc.fd["dropbox"].navigate_to_sign_up_page()
    #     time.sleep(3)
    #     self.fc.fd["dropbox"].click_terms_link()
    #     time.sleep(2)
    #     webpage = "DROPBOX"
    #     self.web_driver.add_window(webpage)
    #     time.sleep(2)
    #     self.web_driver.switch_window(webpage)
    #     time.sleep(2)
    #     current_url = self.web_driver.get_current_url()
    #     assert current_url == "https://www.dropbox.com/terms"


    def test_05_sign_in_not_exist_user_C32161008(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()

        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()

        time.sleep(2)
        self.fc.fd["dropbox"].enter_sign_in_email("1111-21221@123.com")
        self.fc.fd["dropbox"].enter_sign_in_passwd("123456789")
        time.sleep(2)
        self.fc.fd["dropbox"].click_sign_in_button()
        time.sleep(2)

        assert self.fc.fd["dropbox"].get_sign_in_not_exist_user_message() == "The provided user information isn’t valid."

    def test_06_sign_up_exist_user_message_C32160936(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()
            
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()
        
        time.sleep(2)
        self.fc.fd["dropbox"].navigate_to_sign_up_page()
        assert self.fc.fd["dropbox"].verify_sign_up_header_show() is True

        time.sleep(2)
        self.fc.fd["dropbox"].enter_sign_up_first_name("aatest")
        self.fc.fd["dropbox"].enter_sign_up_last_name("aac")
        self.fc.fd["dropbox"].enter_sign_up_email_address("goodyou@hp.com")
        self.fc.fd["dropbox"].enter_sign_up_email_passwd("123456")
        time.sleep(2)
        self.fc.fd["dropbox"].click_sign_up_checkbox()
        time.sleep(2)
        self.fc.fd["dropbox"].click_sign_up_button()
        time.sleep(2)

        assert self.fc.fd["dropbox"].get_sign_up_exist_user_message() == "This e-mail is already taken."
