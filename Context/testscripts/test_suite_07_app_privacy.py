import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_07_App_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.css = request.cls.fc.fd["css"]
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_back_button_on_manage_choice_page_C67872412(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choice_back_btn()
        self.app_consents.click_manage_choices_back_btn()
        self.app_consents.verify_your_data_and_privacy_title()
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not showing up on app consents page after clicking back button from manage choice page."

    @pytest.mark.regression
    def test_02_verify_decline_optional_data_C67872413(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_your_data_and_privacy_title()
        self.app_consents.verify_we_value_your_privacy_title()
        self.driver.swipe("decline_optional_data_btn", direction="down")
        assert self.app_consents.verify_decline_optional_data(), "Decline optional data button is not showing up."
        self.app_consents.click_decline_optional_data_button()

    @pytest.mark.regression
    def test_03_verify_continue_button_on_manage_choice_page_C67874093(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh, condition="Unknown")
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.driver.swipe("manage_choice_continue_btn", direction="down")
        self.css.maximize_hp()
        self.app_consents.verify_manage_choice_continue_btn()
        self.app_consents.click_manage_choice_continue_btn()
        assert self.app_consents.verify_continue_as_guest_button_show_up(), "Continue as guest button is not showing up after clicking on manage choice continue button."

    @pytest.mark.regression
    def test_04_verify_accept_all_button_on_app_consents_page_C67874094(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh, condition="Unknown")
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.app_consents.verify_app_only_consents_screen()
        self.driver.swipe("accept_all_button", direction="down")
        self.css.maximize_hp()
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.click_accept_all_button()
        assert self.app_consents.verify_continue_as_guest_button_show_up(), "Continue as guest button is not showing up after clicking on accept all button."
