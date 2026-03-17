import pytest
import random
from time import sleep
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_06_Pin_Or_Password_Printer_Info(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        """
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
        check_pin=cls.fc.fd["printersettings"].verify_log_in_with_pin_dialog(raise_e=False)
        if not check_pin:
            pytest.skip("Skip this test as the printer has no pin")

    @pytest.mark.regression
    def test_01_verify_country_language_isnot_change_after_clicking_cancel_btn_C57463024_C57463025_C57463026(self):
        """
        Cancel out from the "Find the printer PIN" dialog on Printer Information screen, verify country/language is not changed.
        Verify the "Submit" button does not show enabled until something is entered into the text box.
        Verify incorrect pin message shows under the pin text box.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57463024
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57463025
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57463026
        """
        self.fc.restart_hpx()
        self.__enter_printer_info_page()
        origin_result_1 = self.fc.fd["printersettings"].verify_country_result()
        origin_result_2 = self.fc.fd["printersettings"].verify_language_result()
        self.__select_country_or_language_to_test()
        self.__click_save_on_set_country_or_language_dialog()
        self.fc.fd["printersettings"].verify_submit_btn_status(enable=False)
        self.fc.fd["printersettings"].edit_sign_in_password('11111111')
        self.fc.fd["printersettings"].verify_submit_btn_status()
        self.fc.fd["printersettings"].click_sign_in_submit_btn()
        self.fc.fd["printersettings"].verify_incorrect_pin_text_display()
        self.__click_cancel_btn_on_input_pin_dialog()
        second_result_1 = self.fc.fd["printersettings"].verify_country_result()
        second_result_2 = self.fc.fd["printersettings"].verify_language_result()
        assert origin_result_1 == second_result_1 and origin_result_2 == second_result_2

    @pytest.mark.regression
    def test_02_verify_country_language_isnot_change_after_clicking_cancel_btn_C57463030_C57463031(self):
        """
        Turn off printer after the "Find the printer PIN" dialog shows.
        Click cancel/submit btn.
        Verify the "Find the printer PIN" dialog is dismissed and country/region is not changed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57463030
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57463031
        """
        self.fc.restart_hpx()
        self.__enter_printer_info_page()
        origin_result_1 = self.fc.fd["printersettings"].verify_country_result()
        origin_result_2 = self.fc.fd["printersettings"].verify_language_result()
        self.__select_country_or_language_to_test()
        self.__click_save_on_set_country_or_language_dialog()
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.fd["printersettings"].edit_sign_in_password(self.pin_num)
        self.fc.fd["printersettings"].click_sign_in_submit_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog()
        self.__click_cancel_btn_on_input_pin_dialog()
        third_result_1 = self.fc.fd["printersettings"].verify_country_result()
        third_result_2 = self.fc.fd["printersettings"].verify_language_result()
        assert origin_result_1 == third_result_1 and origin_result_2 == third_result_2
        
    @pytest.mark.regression
    def test_03_verify_country_language_isnot_change_after_clicking_cancel_btn_C57463032(self):
        """
        Turn off printer after changing country or language.
        Verify the "Find the printer PIN" dialog doesn't show after clicking save btn.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57463032
        """
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hpx()
        self.__enter_printer_info_page()
        self.__select_country_or_language_to_test()
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.fd["printersettings"].verify_set_country_or_language_dialog()
        self.fc.fd["printersettings"].click_set_save_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)
        self.fc.fd["printersettings"].verify_unable_to_set_printer_dialog()

    @pytest.mark.regression
    def test_04_verify_country_language_isnot_change_after_clicking_cancel_btn_C57463023_C57463033_C57463034_C57463038(self): 
        """
        The "Find the printer PIN" dialog doesn't show with non-secure printer.
        Verify that the "Find the printer PIN" dialog is dismissed after clicking cancel button or submit btn with correct pin.
        Verify printer country/language is changed.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57463023
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57463033
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57463034
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57463038
        """  
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hpx()
        self.__enter_printer_info_page()
        origin_result_1 = self.fc.fd["printersettings"].verify_country_result()
        origin_result_2 = self.fc.fd["printersettings"].verify_language_result()
        self.__select_country_or_language_to_test()
        self.p.fake_action_door_open()
        self.__click_save_on_set_country_or_language_dialog()
        self.__click_cancel_btn_on_input_pin_dialog()
        fourth_result_1 = self.fc.fd["printersettings"].verify_country_result()
        fourth_result_2 = self.fc.fd["printersettings"].verify_language_result()
        assert origin_result_1 == fourth_result_1 and origin_result_2 == fourth_result_2
        self.__select_country_or_language_to_test()
        self.__click_save_on_set_country_or_language_dialog()
        self.fc.fd["printersettings"].edit_sign_in_password(self.pin_num)
        self.fc.fd["printersettings"].click_sign_in_submit_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)
        fifth_result_1 = self.fc.fd["printersettings"].verify_country_result()
        fifth_result_2 = self.fc.fd["printersettings"].verify_language_result()
        assert fifth_result_1 != origin_result_1 or fifth_result_2 != origin_result_2

    @pytest.mark.regression
    def test_05_close_the_door_and_restore(self):
        """
        Restore printer settings to origin.
        """
        self.p.fake_action_door_close()
        self.fc.fd["printersettings"].click_country_dropdown()
        self.fc.fd["printersettings"].select_USA_country()
        if self.fc.fd["printersettings"].verify_set_country_or_language_dialog(raise_e=False):
            self.fc.fd["printersettings"].click_set_save_btn()
        self.fc.fd["printersettings"].click_language_dropdown()
        self.fc.fd["printersettings"].select_English_language()
        if self.fc.fd["printersettings"].verify_set_country_or_language_dialog(raise_e=False):
            self.fc.fd["printersettings"].click_set_save_btn()

    @pytest.mark.regression
    def test_06_delete_web_password_credential(self):
        self.fc.web_password_credential_delete()



    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __enter_printer_info_page(self):
        """
        click ip address to swipe down the bottom of printer info page.
        """
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].swipe_to_end()

    def __select_country_or_language_to_test(self):
        """
         Randomly select a country or language to change.
        """
        # change country/region or language
        if random.choice([True, False]):
        # Test country/region change
            self.fc.fd["printersettings"].verify_country_region_part()
            select_cou = self.fc.fd["printersettings"].get_country_region_text()
            self.fc.fd["printersettings"].click_country_dropdown()
            cou = self.fc.fd["printersettings"].verify_country_select_item(select_cou)
            cou.send_keys(Keys.UP, Keys.ENTER)
        else:
        # Test language change
            self.fc.fd["printersettings"].verify_language_part()
            select_lan = self.fc.fd["printersettings"].get_language_text()
            self.fc.fd["printersettings"].click_language_dropdown()
            lan = self.fc.fd["printersettings"].verify_language_select_item(select_lan)
            lan.send_keys(Keys.DOWN, Keys.ENTER)

    def __click_save_on_set_country_or_language_dialog(self):
        """
        click save button after changing the country or language and verify the printer with pin/password or not.
        """
        self.fc.fd["printersettings"].verify_set_country_or_language_dialog()
        self.fc.fd["printersettings"].click_set_save_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(raise_e=False)

    def __click_cancel_btn_on_input_pin_dialog(self):
        self.fc.fd["printersettings"].click_sign_in_cancel_btn()
        self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(invisible=True)
        
        