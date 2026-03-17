import pytest 
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

class Test_03_SMB_Account(object):

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
        self.printers = self.fc.fd["printers"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder()

    def test_01_verify_account_profile_personal_tab_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516438
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        
        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("account_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "account_screenshot/{}_account_localization.png".format(self.locale))

        # self.account.verify_account_profile_screen_title()
        self.account.verify_cancel_button_is_not_displayed()
        self.account.enter_first_name("update_")
        self.account.verify_cancel_button_is_displayed()
        self.account.verify_apply_changes_button_is_displayed()

    def test_02_verify_personal_tab_contextual_footer_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516438
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()
        
        # Get acount details 
        user_first_name=self.account.get_first_name()
        user_last_name=self.account.get_last_name()
        user_phonenumber=self.account.get_phonenumber()
       
        # update account details 
        self.account.enter_first_name("update_"+user_first_name)
        self.account.enter_last_name("update_"+user_last_name)
        self.account.enter_phonenumber("15157792345")

        self.account.click_cancel_button()
       
        # Verify Accounts detaild should not update after select Cancel 
        self.account.verify_first_name(user_first_name)
        self.account.verify_last_name(user_last_name)
        self.account.verify_phonenumber(user_phonenumber) 

        #verify Phone number field invalid error message
        self.account.enter_phonenumber("000")
        self.account.verify_phonenumber_field_invalid_error_msg()

    def test_03_verify_update_personal_details(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516439
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516437
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()

        # Get the logged account details 
        user_first_name=self.account.get_first_name()
        user_last_name=self.account.get_last_name()
       
        # update personal details 
        self.account.enter_first_name("update_"+user_first_name)
        self.account.enter_last_name("update_"+user_last_name)
        self.account.click_apply_button()
        self.account.verify_toast_notification()  

        # Verify updated personal details
        self.account.dismiss_toast()
        self.account.verify_first_name("update_"+user_first_name)
        self.account.verify_last_name("update_"+user_last_name)
        
        # reverback updated account details
        self.account.enter_first_name(user_first_name)
        self.account.enter_last_name(user_last_name)

        # click apply changes
        self.account.click_apply_button()
        self.account.verify_toast_notification()

    def test_04_verfify_update_organization_details(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516456
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516458
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.click_organization_tab()

        # Get organization details 
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc()

        # update organization details 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)
        self.account.click_apply_button()
        # self.account.verify_toast_notification()

        # Verify organization details
        self.account.dismiss_toast()
        self.account.verify_organization_name("update_"+org_name)
        self.account.verify_organization_desc("update_"+org_desc)

        # reverback updated organization details
        self.account.enter_organization_name(org_name)
        self.account.enter_organization_desc(org_desc)
        self.account.click_apply_button()
        # self.account.verify_toast_notification()

    def test_05_verify_account_profile_organization_tab_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30726006
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.click_organization_tab()
        self.account.verify_cancel_button_is_not_displayed()
        self.account.enter_organization_name("update_")
        self.account.verify_cancel_button_is_displayed()
        self.account.verify_apply_changes_button_is_displayed()

    def test_06_verfify_organization_tab_contextual_footer_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516457
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.click_organization_tab()

        # Get organization details 
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc()

        # update organization details 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)
        self.account.click_cancel_button()

        # Verify organization details are reverted back to previous
        self.account.verify_organization_name(org_name)
        self.account.verify_organization_desc(org_desc)

    def test_07_verfify_unsaved_changes_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516462
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.click_organization_tab()

        # Update organization details
        self.account.enter_organization_desc("Organization Name")

        # Navigate to users without saving organization details
        self.home.click_users_menu_btn()

        # Verfify Unsaved chnages pop-up
        self.account.verify_unsaved_changes_popup_title()
        self.account.verify_unsaved_changes_popup_desc()
        self.account.verify_unsaved_changes_popup_cancel_button()
        self.account.verify_unsaved_changes_popup_leave_button()

    def test_08_verify_unsaved_popup_cancel_button_functinality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519060
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()
       
        # update account details 
        self.account.enter_first_name("update_")

        #Navigate to home screen without saving account details
        self.home.click_home_menu_btn()

        # Verify unsaved chnages pop-up
        self.account.click_unsaved_changes_popup_cancel_button()

        # Verify acount profile screen
        # self.account.verify_account_profile_screen_title()

    def test_09_verify_unsaved_popup_leave_button_functinality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519061
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()
       
        # update account details 
        self.account.enter_first_name("update_")
        self.account.enter_last_name("update_")

        #Navigate to Home screen without saving account details
        self.home.click_home_menu_btn()
        self.account.click_unsaved_changes_popup_leave_button()

        #Verify Home screen
        self.home.verify_smb_home_title_bar()

    def test_10_verify_apply_changes_button_disabled_functionality_in_personal_tab(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519063
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()

        # update account details 
        self.account.enter_first_name("update_")

        # Verify the apply changes button is enabled
        self.account.verify_apply_button_status("enabled")

        # Clear First name 
        self.account.clear_firstname_text()

        # Verify the apply changes button is disabled
        self.account.verify_apply_button_status("disabled")

    def test_11_verify_apply_changes_button_disabled_functionality_in_organizational_tab(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519069
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()
        self.account.click_organization_tab()

        # update organization details 
        self.account.enter_organization_desc("Organization Name")

        # Verify the apply changes button is enabled
        self.account.verify_apply_button_status("enabled")

        # Clear First name 
        self.account.clear_organization_name()

        # Verify the apply changes button is disabled
        self.account.verify_apply_button_status("disabled")

    def test_12_verfify_switching_to_personal_tab_without_saving_organization_details(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516461
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.click_organization_tab()

        # Update Organization details
        self.account.enter_organization_desc("Organization Name")

        # Naviate to persional tab without saving organization details
        self.account.click_personal_tab()

        # Verify that user should not navigate to Personal tab
        self.account.verify_personal_tab_is_not_selected()
       
    def test_13_verfify_switching_to_organization_tab_without_saving_personal_details(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516442
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()

        # Update personnal details
        self.account.enter_first_name("update_")

        # Naviate to organization tab without saving personal details
        self.account.click_organization_tab()

        # Verify that user should not navigate to Organization tab
        self.account.verify_organization_tab_is_not_selected()
    
    def test_14_verify_language_change_to_germany_in_preferences_language_tab(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_language_tab()
        
        #Changing language to Portuguese
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("German (Germany)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.click_language_tab_apply_button()

        self.home.verify_home_menu_btn()
        self.home.click_printers_menu_btn()
        #verify side menu names in Portuguese
        assert "Startseite" == self.home.get_home_menu_btn_text()
        assert "Benutzer" == self.home.get_users_menu_btn_text()
        assert "Drucker" == self.home.get_printers_menu_btn_text() 
        assert "Lösungen" == self.home.get_solutions_menu_btn_text()
        assert "Nachhaltigkeit" == self.home.get_sustainability_menu_btn_text()
        assert "Konto" == self.home.get_account_menu_btn_text()
        assert "HP Instant Ink" == self.home.get_hpinstantink_menu_btn_text()
        assert "Hilfe-Center" == self.home.get_help_center_menu_text()

        #verify Printers screen title in Portuguese
        assert "Drucker" == self.printers.get_printers_page_title()
        assert "Anzeigen und Verwalten aller Drucker, die Ihrer Organisation zugewiesen sind." == self.printers.get_printers_page_desc()
        self.printers.verify_printer_table_refresh_button()
        self.printers.verify_printer_table_search_box()
        self.printers.verify_printer_table_view_button()
        self.printers.verify_printer_card_view_button()

        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        #verify Account Profile Preferences title in Portuguese
        assert "Einstellungen" == self.account.get_preferences_screen_title()
        
        #Reverting language to English
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Englisch (Indien)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.click_language_tab_apply_button()
        
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_language_tab()

        #verify Account Profile Preferences title in English
        assert "Preferences" == self.account.get_preferences_screen_title()

    def test_15_verify_language_change_to_spanish_in_preferences_language_tab(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_language_tab()
        
        #Changing language to Portuguese
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Spanish (Spain)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.click_language_tab_apply_button()

        self.home.verify_home_menu_btn()
        self.home.click_printers_menu_btn()
        #verify side menu names in Portuguese
        assert "Inicio" == self.home.get_home_menu_btn_text()
        assert "Usuarios" == self.home.get_users_menu_btn_text()
        assert "Impresoras" == self.home.get_printers_menu_btn_text() 
        assert "Soluciones" == self.home.get_solutions_menu_btn_text()
        assert "Sostenibilidad" == self.home.get_sustainability_menu_btn_text()
        assert "Cuenta" == self.home.get_account_menu_btn_text()
        assert "HP Instant Ink" == self.home.get_hpinstantink_menu_btn_text()
        assert "Centro de ayuda" == self.home.get_help_center_menu_text()

        #verify Printers screen title in Portuguese
        assert "Impresoras" == self.printers.get_printers_page_title()
        assert "Accede a y gestiona todas las impresoras vinculadas a tu organización." == self.printers.get_printers_page_desc()
        self.printers.verify_printer_table_refresh_button()
        self.printers.verify_printer_table_search_box()
        self.printers.verify_printer_table_view_button()
        self.printers.verify_printer_card_view_button()

        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        #verify Account Profile Preferences title in Portuguese
        assert "Preferencias" == self.account.get_preferences_screen_title()
        
        #Reverting language to English
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Inglés (Estados Unidos)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.click_language_tab_apply_button()

        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   

        #verify Account Profile Preferences title in English
        assert "Preferences" == self.account.get_preferences_screen_title()