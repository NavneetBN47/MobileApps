import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_01_Welcome_Screen(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.css = request.cls.fc.fd["css"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]


    @pytest.mark.regression
    def test_01_verify_sign_in_and_continue_as_guest_btn_C53533727(self):
        self._function_setup()
        assert self.css.verify_myhp_title_bar(), "HP app title bar is not present/incorrect"
        self.app_consents.verify_continue_as_guest_button_show_up()
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"

    @pytest.mark.regression
    def test_02_upon_hpx_relaunch_welcome_screen_not_present_C53542592(self):
        self._function_setup()
        assert self.css.verify_myhp_title_bar(), "HP app title bar is not present/incorrect"
        self.app_consents.verify_continue_as_guest_button_show_up()
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.profile.title_bar_close_myhp()
        self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6", timeout=40)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.profile.verify_devicepage_avatar_btn(), "Profile icon is not present"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button on homepage is not present"

    @pytest.mark.regression
    def test_03_sign_in_welcome_screen_C53542819(self):
        self._function_setup()
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.css.click_sign_in_btn_welcome_page()
        assert self.hpx_support.verify_username_or_email_placeholder(), "Username or email placeholder is not present"
        assert self.hpx_support.verify_use_password_btn(), "Use password button is not present"
        assert self.hpx_support.verify_create_account_btn(), "Create account button is not present"
        assert self.hpx_support.verify_sign_in_mobile_num(), "Sign-In mobile number field is not present"
        self.profile.minimize_chrome()

    @pytest.mark.regression
    def test_04_continue_as_guest_welcome_screen_C53542821(self):
        self._function_setup()
        assert self.css.verify_myhp_title_bar(), "HP app title bar is not present/incorrect"
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.profile.verify_devicepage_avatar_btn(), "Profile icon is not present"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button on homepage is not present"

    @pytest.mark.regression
    def test_05_verify_hp_logo_on_welcome_screen_C53542798(self):
        assert self.profile.verify_myhp_logo()," Hp Logo is not present"
        self.fc.close_myHP()

######################################################################
#                               PRIVATE FUNCTIONS                    #
######################################################################

    def _function_setup(self):
        if self.app_consents.verify_accept_all_button_show_up():
            self.app_consents.click_accept_all_button()
