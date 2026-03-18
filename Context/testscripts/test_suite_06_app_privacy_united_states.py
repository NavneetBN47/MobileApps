import logging
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_06_App_Privacy_US(object):
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
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_consents_screen_content_us_C67872409(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_necessary_text_from_app_and_device_consents_screen()
        self.app_consents.verify_app_only_consents_screen()
        self._click_links()

    @pytest.mark.regression
    def test_02_verify_consents_with_choices_btn_us_C67872410(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_necessary_text_from_app_and_device_consents_screen()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()

    @pytest.mark.regression
    def test_03_verify_manage_choices_us_content_C67872411(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_necessary_text_from_app_and_device_consents_screen()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self._click_links()

######################################################################
#                               PRIVATE FUNCTIONS                    #
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
