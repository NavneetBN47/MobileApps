import pytest
from time import sleep
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

    def test_01_verify_account_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519059
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_account_menu_btn()

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("account_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "account_screenshot/{}_account_localization.png".format(self.locale))

        self.home.click_account_menu_btn()
        self.account.verify_account_screen_title()
        self.account.verify_account_screen_description()
        self.account.verify_account_profile_tab_title()
        self.account.verify_account_profile_tab_description()
        self.account.verify_preferences_tab_title()
        self.account.verify_preferences_tab_description()
        # self.account.verify_shipping_tab_title()
        # self.account.verify_shipping_tab_description()
        # self.account.verify_billing_tab_title()
        # self.account.verify_billing_tab_description()

    def test_02_verify_account_profile_personal_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516436
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()
        # self.account.verify_account_profile_screen_description()

        self.account.verify_firstname()
        self.account.verify_firstname_label()

        self.account.verify_lastname()
        self.account.verify_lastname_label()

        self.account.verify_email()
        self.account.verify_email_label()

        self.account.verify_phonenumber_label()

        self.account.verify_change_password_link()

    def test_03_verify_change_password_link(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516444
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.verify_change_password_link()
        self.account.click_change_password_link()
        self.account.verify_new_tab_opened()
    
    def test_04_verify_account_profile_organization_tab_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516455
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516459
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        self.account.click_organization_tab()
        self.account.verify_uid_label()
        self.account.verify_uid()
        self.account.verify_uid_is_disabled()  
        self.account.verify_organizations_name()
        self.account.verify_organization_name_label()
        self.account.verify_organization_description()
        self.account.verify_organization_desc_label()
        self.account.verify_organization_country()
        self.account.verify_organization_country_label()
    
    def test_05_verify_account_preferences_screen_privacy_tab_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519072
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_privacy_tab()
        self.account.verify_preferences_screen_title()
        self.account.verify_preferences_screen_description()
        self.account.verify_privacy_tab_title()
        self.account.verify_learn_more_hyperlink_text()
        self.account.verify_required_label()
        self.account.verify_required_description()
        self.account.verify_printer_analytics_label()
        self.account.verify_printer_analytics_description()
        self.account.verify_advertising_label()
        self.account.verify_advertising_description()

    def test_06_verify_account_preferences_screen_notifications_tab_ui(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab() 
        if self.account.verify_preferences_notification_tab_displayed() is True:
            self.account.click_preferences_notifications_tab()
            self.account.verify_notifications_tab_title()
            self.account.verify_notifications_tab_description()
            self.account.verify_notification_type_printer_and_service_status()
            self.account.verify_notification_type_printer_and_service_status_description()
            initial_status = self.account.get_notification_type_printer_and_service_toggle_button_status()
            if initial_status == "On":
                self.account.verify_notification_type_printer_and_service_toggle_button_on_status()
            else:
                self.account.verify_notification_type_printer_and_service_toggle_button_off_status()

            self.account.click_notification_type_printer_and_service_status_toggle_button()
            expected_options= ["Notification Type","Email"]
            assert expected_options == self.account.get_notifications_table_headers()
            self.account.verify_notifications_table_header_notification_type()
            self.account.verify_notifications_table_header_email()
            # self.account.verify_positive_toast_notification()
            sleep(10)
            assert initial_status != self.account.get_notification_type_printer_and_service_toggle_button_status()
    
    def test_07_verify_account_preferences_screen_language_tab_ui(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_language_tab()
        self.account.verify_language_tab_title()

        self.account.verify_language_tab_description()
        self.account.verify_language_tab_dropdown()

    def test_08_verify_language_change_in_preferences_language_tab(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_language_tab()
        
        #Changing language to Portuguese
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Portuguese (Brazil)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.click_language_tab_apply_button()

        self.home.verify_home_menu_btn()
        self.home.click_printers_menu_btn()
        #verify side menu names in Portuguese
        assert "Página Inicial" == self.home.get_home_menu_btn_text()
        assert "Usuários" == self.home.get_users_menu_btn_text()
        assert "Impressoras" == self.home.get_printers_menu_btn_text() 
        assert "Soluções" == self.home.get_solutions_menu_btn_text()
        assert "Sustentabilidade" == self.home.get_sustainability_menu_btn_text()
        assert "Conta" == self.home.get_account_menu_btn_text()
        assert "HP Instant Ink" == self.home.get_hpinstantink_menu_btn_text()
        assert "Central de Ajuda" == self.home.get_help_center_menu_text()

        #verify Printers screen title in Portuguese
        assert "Impressoras" == self.printers.get_printers_page_title()
        assert "Visualizar e gerenciar todas as impressoras vinculadas à sua organização." == self.printers.get_printers_page_desc()
        self.printers.verify_printer_table_refresh_button()
        self.printers.verify_printer_table_search_box()
        self.printers.verify_printer_table_view_button()
        self.printers.verify_printer_card_view_button()

        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()
        self.account.click_preferences_language_tab()

        #verify Account Profile Preferences title in Portuguese
        assert "Preferências" == self.account.get_preferences_screen_title()
        
        #Reverting language to English
        self.account.click_language_tab_dropdown()
        self.account.enter_preferred_language_in_language_dropdown("Inglês (Estados Unidos)")
        self.account.select_preferred_language_in_language_dropdown()
        self.account.click_language_tab_apply_button()

        self.home.click_account_menu_btn()
        self.account.click_preferences_tab()   
        self.account.click_preferences_language_tab()

        #verify Account Profile Preferences title in English
        assert "Preferences" == self.account.get_preferences_screen_title()