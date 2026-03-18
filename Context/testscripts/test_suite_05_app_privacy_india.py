import logging
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_05_App_Privacy_India(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_validate_app_only_screen_content_for_india_C53304047(self):
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"

    @pytest.mark.regression
    def test_02_verify_buttons_layout_on_app_ony_consents_screen_C53304055(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Accepted")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.verify_decline_optional_data()

    @pytest.mark.regression
    def test_03_verify_app_only_consents_screen_content_C67872406(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Accepted")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_your_data_and_privacy_title()
        self._click_links()

    @pytest.mark.regression
    def test_04_verify_buttons_layout_on_manage_choice_screen_C53304058(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Accepted")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choice_continue_btn()
        self.app_consents.verify_manage_choice_back_btn()

    @pytest.mark.regression
    def test_05_verify_buttons_layout_on_app_only_consents_screen_C67872408(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Accepted")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.verify_decline_optional_data() 

    @pytest.mark.regression
    def test_06_verify_app_device_consents_contents_C67872414(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.verify_your_data_and_privacy_title()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self._click_links()

    @pytest.mark.regression
    def test_07_verify_buttons_on_app_consents_page_C67872415(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")      
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.verify_decline_optional_data()

    @pytest.mark.regression
    def test_08_verify_manage_choice_page_contents_C67872416(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown") 
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choice_body_text()
        self.app_consents.verify_your_data_and_privacy_title()
        self._click_links()

    @pytest.mark.regression
    def test_09_verify_buttons_on_manage_choice_page_C67872417(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")   
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.driver.swipe("manage_choice_continue_btn", direction="down")
        self.app_consents.verify_manage_choice_continue_btn()
        self.app_consents.verify_manage_choice_back_btn()

    @pytest.mark.regression
    def test_10_validate_manage_choice_screen_C67872407(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Accepted")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")    
        self.fc.change_system_region_to_india()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choice_body_text()
        self.app_consents.verify_your_data_and_privacy_title()
        self._click_links()

######################################################################
#                           PRIVATE FUNCTIONS                        #
######################################################################

    def _click_links(self):
        self.driver.swipe(distance=5)
        self.app_consents.click_advertising_here_link()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Advertising link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()
        self.app_consents.click_terms_of_use_link()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Terms of Use link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()
        self.app_consents.click_end_user_license_agreement_link()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"End User License Agreement link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()
