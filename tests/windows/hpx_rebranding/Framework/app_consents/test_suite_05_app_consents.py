import logging
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("function_setup_to_reset_and_launch_myhp")
class Test_Suite_05_App_Consents(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.webdriver = utility_web_session
        request.cls.fc = FlowContainer(cls.driver)
        request.getfixturevalue("class_setup_fixture_ota_regression")
        cls.profile = cls.fc.fd["profile"]
        cls.app_consents = cls.fc.fd["app_consents"]
        cls.hpx_support = cls.fc.fd["hpx_support"]
        cls.fc.kill_hpx_process()
        cls.fc.kill_chrome_process()   
        request.cls.fc.change_system_region_to_china()
        request.cls.fc.close_and_restart_myhp_app()
        yield
        request.cls.fc.change_system_region_to_united_states()
        request.cls.fc.consent_transfer_out_consent_required(request.cls.driver.ssh,condition="False")

    @pytest.mark.regression
    def test_01_verify_other_consents_toggles_inactive_C53303875(self):
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")
        self.fc.consent_transfer_out_consent_required(self.driver.ssh,condition="True")
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_manage_choices_btn(), "Manage options button is not present"
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        assert self.app_consents.verify_data_transfer_consent_for_china(), "Data transfer consent is not visible"
        assert self.app_consents.verify_product_improvement_china_is_enabled() is False, "Product improvement button is clickable"
        assert self.app_consents.verify_advertising_china_is_enabled() is False, "Advertising button is clickable"
        self.app_consents.click_data_transfer_consent_for_china()
        assert self.app_consents.verify_product_improvement_china_is_enabled() is True, "Product improvement button is not clickable"
        assert self.app_consents.verify_advertising_china_is_enabled() is True, "Advertising button is not clickable"
        
    @pytest.mark.regression
    def test_02_verify_common_consents_screen_content_for_china_C53303870(self):
        self.fc.consent_allow_support(self.driver.ssh, condition="Unknown")
        assert self.app_consents.verify_app_only_consents_screen(), "App consents screen is not displayed for China region"
        test_data = [
            ("click_ai_terms_of_use_link", "HP AI Terms of Service | HP® Support", "AI Terms of Use"),
            ("click_terms_of_use_link", "HP App Terms of Use | HP® Support", "Terms of Use"),
            ("click_end_user_license_agreement_link", "End-User License Agreement | HP® Support", "End User License Agreement")
        ]
        for method, expected_tab_name, link_name in test_data:
            getattr(self.app_consents, method)()
            self.hpx_support.verify_browser_pane()
            actual_tab_name = self.hpx_support.get_browser_tab_name()
            logging.info(f"{link_name} Browser tab name is: {actual_tab_name}")
            logging.info(f"Expected text in tab name: {expected_tab_name}")
            assert expected_tab_name in actual_tab_name, f"Expected tab name to contain '{expected_tab_name}', but got '{actual_tab_name}'"
            self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_03_app_only_consents_screen_displayed_on_unmanaged_device_C60498995(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=False)
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen on unmanaged device"