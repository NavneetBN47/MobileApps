import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_04_App_Consents(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup,utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.fd["profile"].minimize_chrome()
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.fc.consent_allow_marketing(cls.driver.ssh,"Unknown")
        cls.re = RegistryUtilities(cls.driver.ssh)

    @pytest.mark.regression
    def test_01_verify_ai_terms_of_use_link_C64750582(self):
        self.fc.launch_myHP_command()
        self.app_consents.click_accept_all_button()
        self.app_consents.click_continue_as_guest_button()
        self.css.maximize_hp()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.click_profile_settings_btn()
        self.app_consents.verify_ai_terms_of_use_link()
        self.app_consents.click_ai_terms_of_use_link()
        assert self.app_consents.verify_ai_terms_of_use_clicked_title("HP AI Terms of Service"), "AI Terms of Use link is not working as expected"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_02_verify_common_consents_status_after_click_on_accept_C53304070(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_decline_optional_data_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") == True
        assert self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected") == True
        assert self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") == True