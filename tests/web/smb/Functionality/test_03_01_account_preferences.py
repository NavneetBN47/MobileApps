import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

class Test_03_01_SMB_Account_Preferences(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.account = self.fc.fd["account"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder()
    
    def test_01_verify_preferences_screen_required_toggle_button(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519083
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
                
        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("account_preferences_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "account_preferences_screenshot/{}_account_localization.png".format(self.locale))

        self.account.click_preferences_tab()
        self.account.click_preferences_privacy_tab()
        # by default required toggle button status is true and should not allow user to change the status
        assert True == self.account.get_required_toggle_button_status()

    def test_02_verify_preferences_screen_printer_analytics_toggle_button(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519084
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_privacy_tab()

        #get actual printer analytics status(True/False)
        actual_status = self.account.get_printer_analytics_toggle_button_status()
        self.account.click_printer_analytics_toggle_button()

        #get printer analytics notification status(ON/OFF)
        updated_status = self.account.get_printer_analytics_toggle_button_status()

        assert actual_status != updated_status

        #reverting back the toggle status
        self.account.click_printer_analytics_toggle_button()

    def test_03_verify_preferences_screen_advertising_toggle_button(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519085
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_privacy_tab()

        #get actual advertising status(True/False)
        actual_status = self.account.get_advertising_toggle_button_status()
        self.account.click_advertising_toggle_button()

        #get updated advertising status(ON/OFF)
        updated_status = self.account.get_advertising_toggle_button_status()

        assert actual_status != updated_status

        # reverting back the toggle status
        self.account.click_advertising_toggle_button()

    def test_04_verify_preferences_screen_learn_more_hyperlink(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519082
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_privacy_tab()
        self.account.click_learn_more_hyperlink()
        self.account.verify_new_tab_opened()

    def test_05_verify_account_preferences_language_tab_search_functionality(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        # #Verify valid search functionality
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Portuguese (Brazil)")
        self.account.verify_preferred_language_result_in_language_dropdown()
        self.account.clear_preferred_language_in_language_dropdown()

        #Verify invalid search functionality
        self.account.enter_preferred_language_in_language_dropdown("test")
        self.account.verify_language_dropdown_no_items_msg()
        self.account.clear_preferred_language_in_language_dropdown()

        #verify multiple search functionality
        self.account.enter_preferred_language_in_language_dropdown("Portuguese")
        self.account.verify_preferred_language_multiple_result_in_language_dropdown()
        self.account.clear_preferred_language_in_language_dropdown()

    def test_06_verify_account_preferences_language_tab_contextual_footer(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()
        initial_title = self.account.get_preferences_screen_title()

        # #Verify valid search functionality
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Portuguese (Brazil)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.verify_language_tab_apply_button()
        self.account.verify_language_tab_cancel_button()

        self.account.click_language_tab_cancel_button()
        assert initial_title == self.account.get_preferences_screen_title()

    def test_07_verfify_account_preferences_unsaved_changes_popup(self):
        # 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        # #Verify valid search functionality
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Portuguese (Brazil)")
        self.account.select_preferred_language_in_language_dropdown()

        # Navigate to users without saving language changes
        self.home.click_users_menu_btn()

        # Verfify Unsaved chnages pop-up
        self.account.verify_preferences_unsaved_changes_popup_title()
        self.account.verify_preferences_unsaved_changes_popup_desc()
        self.account.verify_preferences_unsaved_changes_popup_cancel_button()
        self.account.verify_preferences_unsaved_changes_popup_leave_button()

    def test_08_verify_account_preferences_unsaved_popup_cancel_button_functinality(self):
        # 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        # #Verify valid search functionality
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Portuguese (Brazil)")
        self.account.select_preferred_language_in_language_dropdown()

        # Navigate to users without saving language changes
        self.home.click_users_menu_btn()

        # Verify unsaved changes pop-up
        self.account.click_preferences_unsaved_changes_popup_cancel_button()

        # Verify preferences - language tab screen
        self.account.verify_language_tab_title()

    def test_09_verify_account_preferences_unsaved_popup_leave_button_functinality(self):
        # 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        # #Verify valid search functionality
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Portuguese (Brazil)")
        self.account.select_preferred_language_in_language_dropdown()

        #Navigate to Home screen without saving account details
        self.home.click_home_menu_btn()
        self.account.click_preferences_unsaved_changes_popup_leave_button()

        #Verify Home screen
        self.home.verify_smb_home_title_bar()