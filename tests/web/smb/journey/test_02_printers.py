import pytest
import logging
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.smb.smb_utility import load_journey_printer_info
from selenium.common.exceptions import TimeoutException
pytest.app_info = "SMB"

class Test_02_Printer(object):

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
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.users = self.fc.fd["users"]
        self.printers = self.fc.fd["printers"]
        self.account = ma_misc.get_smb_account_info(self.stack + "_journey_testing")
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        self.hpid_tenantID = self.account["tenantID"]
        self.p_info = load_journey_printer_info(self.stack + "_journey_testing")
        
        yield # Cleanup:
        try:
            self.home.logout()
        except TimeoutException as err:
            # logout is 'best effort' only for this journey. We don't care if the logout fails here
            logging.info("Unable to complete teardown. {err}")


    def test_01_verify_printer_card_view_mfe(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519620
        #Verify printers card view mfe which opens by default
        logging.info("Using account: {self.hpid_username}")
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_smb_home_title_bar()        
        self.home.click_printers_menu_btn()

        #verifies printers card view table when table_load is false
        self.printers.verify_printers_page(table_load=False)
        self.printers.verify_printers_page_title()

    def test_02_verify_printer_table_view_mfe(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516045       
        logging.info("Using account: {self.hpid_username}")
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_smb_home_title_bar()        
        self.home.click_printers_menu_btn()

        #Printers card view opens by default
        self.printers.verify_printers_page(table_load=False)
        self.printers.verify_printers_page_title()

        #verifies printers table view when table_load is true
        self.printers.click_printer_table_view_button()
        self.printers.verify_printers_page(table_load=True)
    
   

        