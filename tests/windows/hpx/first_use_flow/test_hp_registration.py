import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
from SAF.misc import windows_utils
import pytest

pytest.app_info = "HPX"
class Test_Suite_HP_Registration(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)

    def test_01_show_first_launch_C31757772(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()
        
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        if self.fc.fd["hp_registration"].verify_hp_registration_show():
            text = self.fc.fd["hp_registration"].check_sub_title_text()
            assert text == "Register your PC for faster warranty support"

        self.fc.close_app()
        time.sleep(5)
        self.fc.launch_app()
        if self.fc.fd["hp_registration"].verify_hp_registration_show():
            assert self.fc.fd["hp_registration"].verify_hp_registration_show() is False

        

    def test_02_skipButton_C32224214(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()
            
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_welcome_module_show()) is True


    # def test_03_verify_links_clickable_online_C32151522(self, install_app):

    #     webpage = "PRIVACY"
    #     self.fc.re_install_app(install_app)
    #     time.sleep(5)
    #     self.fc.launch_app()

    #     if self.fc.fd["hp_login"].verfiy_login_page_show():
    #         self.fc.fd["hp_login"].close_login_page()

    #     if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
    #         self.fc.fd["hp_privacy_setting"].click_decline_all_button()

    #     if self.fc.fd["hp_registration"].verify_skip_button_show():
    #         time.sleep(5)
    #         self.fc.fd["hp_registration"].open_privacy_link()        
    #     time.sleep(5)
    #     self.web_driver.add_window(webpage)
    #     time.sleep(5)
    #     self.web_driver.switch_window(webpage)
    #     time.sleep(5)
    #     current_url = self.web_driver.get_current_url()
    #     assert current_url == "https://www.hp.com/us-en/privacy/privacy-central.html"
    
    def test_04_verify_register_button_status_C32151525(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()

        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        assert self.fc.fd["hp_registration"].registtation_button_is_selected() == "false"

        time.sleep(5)

        self.fc.fd["hp_registration"].enter_first_name("test1")
        time.sleep(3)
        self.fc.fd["hp_registration"].enter_last_name("atest02")
        time.sleep(3)
        self.fc.fd["hp_registration"].enter_email_address("email10323@gmail.com")
        time.sleep(3)

        assert self.fc.fd["hp_registration"].registtation_button_is_selected() == "true"

    def test_05_invalid_register_data_C32151527(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()
        
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()


        self.fc.fd["hp_registration"].enter_first_name("<><>></")
        time.sleep(3)
        assert self.fc.fd["hp_registration"].get_firstName_invalid_data_message() == "A valid first name is required."
        self.fc.fd["hp_registration"].enter_last_name("<><>></")
        time.sleep(3)
        assert self.fc.fd["hp_registration"].get_lastName_invalid_data_message() == "A valid last name is required."
        self.fc.fd["hp_registration"].enter_email_address("<><>></")
        time.sleep(3)
        self.fc.fd["hp_registration"].get_email_invalid_data_message()
        assert self.fc.fd["hp_registration"].get_email_invalid_data_message() == "A valid email is required."

    def test_06_complete_registration_C32151531(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()

        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        self.fc.fd["hp_registration"].complete_register("test01", "aaaa", "tsta101@gmail.com")
        assert self.fc.fd["hp_registration"].verify_register_success() is True

        generate_file = "C:\\ProgramData\\HP\\registration\\full_registration_request.xml"
        assert windows_utils.check_path_exist(self.driver.ssh, generate_file) is True
        time.sleep(2)
        self.fc.intial_environment()
    
    def test_07_show_hp_registration_first_launch_C33641078(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_app()
        
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        self.fc.fd["hp_registration"].verify_hp_registration_show()
        text = self.fc.fd["hp_registration"].check_sub_title_text()
        assert text == "Register your PC for faster warranty support"
    

    @pytest.mark.require_platform(["grogu"])
    def test_08_not_show_hp_registration_first_launch_on_hpone_C33267805(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_app()
        
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        self.fc.fd["hp_registration"].verify_hp_registration_show()

        self.fc.fd["hp_registration"].click_country_dropdown_list()
        time.sleep(2)

        assert self.fc.fd["hp_registration"].verify_hp_registration_show() is False

    
    def test_09_verify_country_dropdownlist_C32151524(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_app()
        
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        self.fc.fd["hp_registration"].verify_hp_registration_show()

        self.fc.fd["hp_registration"].click_country_dropdown_list()
        time.sleep(2)

        assert bool(self.fc.fd["hp_registration"].veify_country_uganda_show())
        assert bool(self.fc.fd["hp_registration"].veify_country_ukraine_show())
        assert bool(self.fc.fd["hp_registration"].veify_country_kingdom_show())


    def test_10_empty_register_data_C32151528(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_app()
        
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        self.fc.fd["hp_registration"].verify_hp_registration_show()


        self.fc.fd["hp_registration"].enter_first_name("   ")
        time.sleep(3)
        assert bool(self.fc.fd["hp_registration"].verify_firstName_invalid_data_message_show()) is False
        self.fc.fd["hp_registration"].enter_last_name("   ")
        time.sleep(3)
        assert bool(self.fc.fd["hp_registration"].verify_lastName_invalid_data_message_show()) is False
        self.fc.fd["hp_registration"].enter_email_address("goodyou123@outlook.com")
        time.sleep(3)
        assert bool(self.fc.fd["hp_registration"].verify_email_invalid_data_message_show()) is False
