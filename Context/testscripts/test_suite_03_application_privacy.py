import logging
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_03_Application_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.profile = request.cls.fc.fd["profile"]
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_accept_all_button_layout_C53304030(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"

    @pytest.mark.regression
    def test_02_verify_decline_optional_data_button_layout_C53304031(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_decline_optional_data_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"

    @pytest.mark.regression
    def test_03_verify_manage_choices_button_layout_on_app_only_consents_screen_C53304032(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()

    @pytest.mark.regression
    def test_04_verify_app_only_consents_manage_choices_screen_content_C53304033(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.get_necessary_text_from_manage_choice_consent_screen()
        self.driver.swipe(distance=5)
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
        self.app_consents.click_hp_privacy_statement_link()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"HP Privacy Statement link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_05_verify_back_button_layout_C53304034(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.verify_manage_choices_back_btn()
        self.app_consents.click_manage_choices_back_btn()
        self.app_consents.verify_app_only_consents_screen()
