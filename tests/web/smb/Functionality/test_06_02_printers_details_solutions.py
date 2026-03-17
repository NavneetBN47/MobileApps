import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_06_02_SMB_Printers_Details_Solutions(object):

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
        self.printers = self.fc.fd["printers"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_printers_menu_btn()
        self.home.click_printers_menu_btn()
        return self.printers.verify_printers_page(table_load=False)

    def test_01_verify_printer_solutions_tab_smart_security_manage_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519777
        
        # To verify manage link in smart security  
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.click_printer_solutions_tab()
        if self.printers.verify_printer_details_solutions_smart_security_title_is_displayed() is True:
            self.printers.click_printer_solutions_smart_security_manage_link()
            self.printers.verify_smart_security_setting_page()

    def test_02_verify_printer_solutions_tab_print_anywhere_manage_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519778
        
        # To verify manage link in print anywhere  
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.click_printer_solutions_tab()
        if self.printers.verify_printer_solutions_print_anywhere_manage_link_is_displayed() is True:
            self.printers.click_printer_solutions_print_anywhere_manage_link()
            self.printers.verify_print_anywhere_screen_title()
        else:
            logging.info("Print anywhere link is not present under Solutions tab.")

    def test_03_verify_printer_solutions_tab_sustainability_learn_more_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519780
        
        # To verify learn more link in sustainability
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.click_printer_solutions_tab()
        if self.printers.verify_printer_solutions_sustainability_learn_more_link_is_displayed() is True:
            self.printers.click_printer_solutions_sustainability_learn_more_link()
            self.printers.verify_sustainability_screen_title()
        else:
            logging.info("Sustainability learn more link is not present under Solutions tab.")