import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

##############################################################
#    One simulator printer doesn't support go to EWS page      #
##############################################################

pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_03_Password_And_Pin_Advanced_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        """
        Can't enter to EWS page with simulated printer.

        Check the test printer with pin/password or not.
        If the printer doesn't have PIN/password, skip all tests.
        """
        cls.fc.launch_hpx_to_home_page()
        cls.fc.add_a_printer(cls.p)
        cls.fc.fd["devicesMFE"].verify_windows_dummy_printer(cls.printer_name, timeout=30)
        cls.fc.fd["devicesMFE"].click_windows_dummy_printer(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].click_view_all_button()
        cls.fc.fd["printersettings"].verify_progress_bar()
        cls.fc.fd["printersettings"].verify_advanced_settings_item()
        cls.fc.fd["printersettings"].select_advanced_settings_item()
        cls.fc.fd["printersettings"].verify_ews_page()
        cls.fc.fd["printersettings"].click_network_summary_tile()
        cls.has_pin = cls.fc.fd["printersettings"].verify_log_in_with_pin_dialog(raise_e=False)

    @pytest.fixture(autouse=True)
    def skip_if_no_pin(self, request):
        # Only skip for secure prompt tests, not for test_01
        if request.function.__name__ != "test_01_verify_no_secure_prompt_C57462993" and not self.has_pin:
            pytest.skip("Skip secure prompt tests as the printer has no pin/password.")


    @pytest.mark.regression
    def test_01_verify_no_secure_prompt_C57462993(self):
        """
        Verify pin prompt does not show with printer has no pin/password.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462993
        """
        if self.has_pin:
            pytest.skip("Skip test as the printer has pin/password.")
        
    @pytest.mark.regression
    def test_02_verify_cancel_with_secure_prompt_C57462923_C57462925_C57462992(self):
        """
        Cancel out from the Advanced Settings secure prompt, verify locked feature cannot be accessed.
        Visit all features in Advanced Settings (EWS) with a non secure printer, verify password prompt does not show.
        Cancel out from the Advanced Settings secure prompt (Pin), verify locked feature cannot be accessed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462923
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462925
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462992
        """
        self.fc.restart_hpx()
        self.__go_to_ews_and_make_pin_dialog_shows()
        self.__click_cancel_on_pin_dialog()
        self.fc.fd["printersettings"].click_ews_home_title()
        self.fc.fd["printersettings"].verify_tile_are_locked()

    @pytest.mark.regression
    def test_03_verify_offline_printer_with_clicking_cancel_on_secure_prompt_C57462930_C57462996(self):
        """
        Verify secure prompt is dismissed, the locked feature cannot be displayed.
        Trigger pin prompt in Advanced Settings (EWS), turn off printer, cancel on dialog, verify secure prompt is dismissed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462930
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462996
        """
        self.fc.restart_hpx()
        self.__go_to_ews_and_make_pin_dialog_shows()
        self.fc.trigger_printer_offline_status(self.p)
        self.__click_cancel_on_pin_dialog()
        self.fc.fd["printersettings"].click_ews_home_title()
        self.fc.fd["printersettings"].click_network_summary_tile()
        self.fc.fd["printersettings"].verify_general_title_not_show()

    @pytest.mark.regression
    def test_04_verify_offline_printer_with_clicking_submit_on_secure_prompt_C57462929_C57462995(self):
        """
        Verify secure prompt is dismissed, the locked feature is not open.
        Turn off printer when the Advanced Settings(EWS) secure prompt shows, enter pin, verify locked feature is not open.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462929
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462995
        """
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hpx()
        self.__go_to_ews_and_make_pin_dialog_shows()
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.fd["printersettings"].enter_pin_num(self.pin_num)
        self.fc.fd["printersettings"].click_submit_btn()
        self.fc.fd["printersettings"].verify_general_title_not_show()
    
    @pytest.mark.regression
    def test_05_verify_locked_feature_not_open_when_input_error_pin_on_secure_prompt_C57462991_C57462924(self):
        """
        Enter incorrect pin on the Advanced Settings secure prompt, verify error message shows and dialog is still present.
       
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462991
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462924
        """
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hpx()
        self.__go_to_ews_and_make_pin_dialog_shows()
        self.__input_error_pin_several_times(times=1)
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog()
        self.fc.fd["printersettings"].verify_incorrect_pin_text_display()
        
    @pytest.mark.regression
    def test_06_verify_ews_is_blocked_when_input_error_pin_several_times_on_secure_prompt_C57462931_C57462932_C57462998_C57462999(self):
        """
        Input incorrect pin/passwprd several times and EWS will be blocked but user can still access other pages in the app.
        verify secure prompt is not displayed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462931
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462932
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462998
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462999
        """
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hpx()
        self.__go_to_ews_and_make_pin_dialog_shows()
        self.__input_error_pin_several_times()
        self.fc.fd["printersettings"].verify_ews_session_locked()
        self.fc.fd["printersettings"].click_ews_home_title()
        self.fc.fd["printersettings"].verify_tile_are_locked()
        self.fc.fd["printersettings"].click_network_summary_tile()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)

    @pytest.mark.regression
    def test_07_verify_printer_error_with_clicking_cancel_on_secure_prompt_C57462920_C57462921_C57462997(self):
        """
        Generate any printer error, enter password on the Advanced Settings (EWS) secure prompt, verify locked feature opens.
        Generate any printer error, cancel on the Advanced Settings (EWS) secure prompt, verify secure prompt is dismissed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462920
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462921
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462997

        """
        self.__make_pin_dialog_displays()
        self.p.fake_action_door_open()
        self.__click_cancel_on_pin_dialog()
        self.__make_pin_dialog_displays()
        self.fc.fd["printersettings"].enter_pin_num(self.pin_num)
        self.fc.fd["printersettings"].click_submit_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)
        self.fc.fd["printersettings"].verify_sign_out_text_display()

    @pytest.mark.regression
    def test_08_verify_printer_error_with_clicking_submit_on_secure_prompt_C57462988(self):
        """
        Generate any printer error, go to Advanced Settings (EWS) to visit a lock feature, enter pin, verify locked feature opens.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462988
        """
        self.p.fake_action_door_close()
        self.fc.restart_hpx()
        self.__go_to_advanced_settings_page()
        self.fc.fd["printersettings"].verify_ews_page()
        self.p.fake_action_door_open()
        self.fc.fd["printersettings"].click_sign_in_link()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog()
        self.__input_correct_pin_and_submit()

    @pytest.mark.regression
    def test_09_trigger_printer_error_with_submit_correct_pin_on_secure_prompt_C57462989(self):
        """
        Go to Printer Settings (EWS) to visited a locked feature, generate any printer error, verify Pin prompt shows and flow continues.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462989
        """
        self.p.fake_action_door_close()
        self.fc.restart_hpx()
        self.__go_to_advanced_settings_page()
        self.fc.fd["printersettings"].verify_ews_page()
        self.fc.fd["printersettings"].click_sign_in_link()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog()
        self.p.fake_action_door_open()
        self.__input_correct_pin_and_submit()

    @pytest.mark.regression
    def test_10_enter_correct_pin_and_verify_feature_opens_C57462990(self):
        """
        Enter correct pin on the Advanced Settings secure prompt, verify locked feature opens.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462990
        """
        self.p.fake_action_door_close()
        self.fc.restart_hpx()
        self.__go_to_ews_and_make_pin_dialog_shows()
        self.__input_correct_pin_and_submit()

    @pytest.mark.regression
    def test_11_delete_web_password_credential(self):
        self.fc.web_password_credential_delete()



    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __go_to_ews_and_make_pin_dialog_shows(self):
        """
        Go to EWS page and make the pin/password dialog shows.
        """
        self.__go_to_advanced_settings_page()
        self.__make_pin_dialog_displays()

    def __go_to_advanced_settings_page(self):
        """
        Go to EWS page in HPX.
        """
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_advanced_settings_item()
        self.fc.fd["printersettings"].select_advanced_settings_item()
        
    def __make_pin_dialog_displays(self):
        """
        Go to pin/password dialog with secure printer.
        """
        self.fc.fd["printersettings"].verify_ews_page()
        self.fc.fd["printersettings"].click_network_summary_tile()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog()

    def __click_cancel_on_pin_dialog(self):
        """
        Click cancel button on PIN dialog and confirm dialog is missing.
        """
        self.fc.fd["printersettings"].click_sign_in_cancel_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)

    def __input_correct_pin_and_submit(self):
        """
        Input pin and make sure sign out shows.
        """
        self.fc.fd["printersettings"].enter_pin_num(self.pin_num)
        self.fc.fd["printersettings"].click_submit_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)
        self.fc.fd["printersettings"].verify_sign_out_text_display()

    def __input_error_pin_several_times(self, times=3, pin_num="22222222"):
        """
        Repeat enter incorrect password on the secure prompt dialog and click Submit several times.
        """
        for _ in range(times):
            self.fc.fd["printersettings"].enter_pin_num(pin_num)
            self.fc.fd["printersettings"].click_submit_btn()