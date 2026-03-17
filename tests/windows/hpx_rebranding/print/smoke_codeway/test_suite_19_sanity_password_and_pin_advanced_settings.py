import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"

@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_19_Sanity_Password_And_Pin_Advanced_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name = cls.p.get_printer_information()['model name']


    @pytest.mark.smoke
    def test_01_verify_ews_with_locked_feature_with_secure_printer_C57462918_C57462922_C57462986(self):
        """
        Visit any locked feature in Advanced Settings (EWS) with a secure printer, verify password prompt shows.
        Enter correct password on the Advanced Settings secure prompt, verify locked feature opens.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462918
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462922
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462986
        HPXG-2753:[Performance] The Printer Settings screen displays nothing for about 10 seconds after clicking the "View all" of "Print Settings".
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_advanced_settings_item()
        self.fc.fd["printersettings"].verify_ews_page()
        self.fc.fd["printersettings"].click_network_summary_tile()
        check_pin=self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(raise_e=False)
        if not check_pin:
            pytest.skip("Skip this test as the printer has no pin")
        self.pin_num = self.p.get_pin()
        self.fc.fd["printersettings"].enter_pin_num(self.pin_num)
        self.fc.fd["printersettings"].click_sign_in_submit_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)
        self.fc.fd["printersettings"].verify_sign_out_text_display()