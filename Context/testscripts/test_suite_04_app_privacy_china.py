import logging
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_04_App_Privacy_China(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.energy_consumption = request.cls.fc.fd["energy_consumption"]
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_validate_app_only_consents_screen_content_for_china_C53304041(self):
        self.fc.change_system_region_to_china()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"    

    @pytest.mark.regression
    def test_02_validate_manage_choice_china_C53304043(self):
        self.fc.change_system_region_to_china()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choice_body_text()
        self._click_links()
        assert self.app_consents.verify_manage_choice_continue_btn(), "Failed to verify continue button on manage choice screen"

    @pytest.mark.regression
    def test_03_verify_manage_choice_page_content_C53304049(self):
        self.fc.change_system_region_to_china()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choice_body_text()
        self._click_links()
        assert self.app_consents.verify_manage_choice_continue_btn(), "Failed to verify continue button on manage choice screen"

    @pytest.mark.regression
    def test_04_verify_buttons_on_manage_choice_china_C53304044(self):
        self.fc.change_system_region_to_china()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choice_continue_btn() 
        assert self.app_consents.verify_manage_choice_back_btn()

    @pytest.mark.regression
    def test_05_verify_data_transfer_on_manage_choice_screen_C53304045(self):
        self.fc.change_system_region_to_china()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        assert self.app_consents.verify_data_transfer_consent_for_china()

######################################################################
#                           PRIVATE FUNCTIONS                        #
######################################################################

    def _click_links(self):
        self.driver.swipe(distance=5)
        self.app_consents.verify_product_improvement_toggle_off()
        self.app_consents.verify_advertising_toggle_off()
        self.app_consents.click_advertising_here_link()
        self.hpx_support.verify_browser_pane()
        self.energy_consumption.get_webpage_url()
        assert "hpsmart.com/us/en/plain/data-sharing-notice" in self.energy_consumption.get_webpage_url(), "Failed to verify Advertising link webpage URL"
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Advertising link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()
        self.app_consents.click_terms_of_use_link()
        self.hpx_support.verify_browser_pane()
        self.energy_consumption.get_webpage_url()
        assert "support.hp.com/" in self.energy_consumption.get_webpage_url(), "Failed to verify Terms of Use link webpage URL"
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Terms of Use link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()
        self.app_consents.click_end_user_license_agreement_link()
        self.hpx_support.verify_browser_pane()
        self.energy_consumption.get_webpage_url()
        assert "https://support.hp.com/" in self.energy_consumption.get_webpage_url(), "Failed to verify End User License Agreement link webpage URL"
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"End User License Agreement link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()
        return True
