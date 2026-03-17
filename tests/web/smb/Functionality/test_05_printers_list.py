import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_05_SMB_Printers(object):

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

    def test_01_verify_printer_table_view_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516077
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30529379
        #https://hp-testrail.external.hp.com/index.php?/cases/view/31269302
        
        expected_table_headers = ["PRINTER NAME", "LOCATION", "CONNECTIVITY","DEVICE STATUS","SECURITY STATUS"]
        self.printers.click_printer_table_view_button()  
        self.printers.select_page_size_new("100")            
        #get printer count from printers page
        printer_page_printer_count = self.printers.get_printers_count()

        if printer_page_printer_count == 0:
            self.printers.verify_printer_table_empty_text()          
        else:       
            assert expected_table_headers == self.printers.verify_printer_table_headers()

    def test_02_verify_printer_card_view_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519658
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519665
        #https://hp-testrail.external.hp.com/index.php?/cases/view/31269304

        self.printers.click_printer_table_view_button() 
        self.printers.select_page_size_new("100")
        #get printer count from printers page
        printer_page_printer_count = self.printers.get_printers_count()      
        self.printers.click_printer_card_view_button()

        if printer_page_printer_count == 0:
            self.printers.verify_printer_card_view_empty_text()          
        else:          
            self.printers.verify_printer_details_screen_printer_name()
    
    def test_03_verify_table_view_printer_details(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516067
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516068

        self.printers.click_printer_table_view_button()
        self.printers.select_page_size_new("100")
        #verify printer table view with printer details screen 
        self.printers.click_table_header_by_name("connectivity")
        self.printers.click_table_header_by_name("connectivity")
        entry_detail = self.printers.get_printers_info_in_table_view()
        self.printers.click_first_entry_link()
        assert entry_detail == self.printers.get_printer_details_in_printer_details_screen()

    def test_04_verify_card_view_printer_details(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519659
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519660

        self.printers.click_card_view_connected_printer_link()
        self.printers.verify_connectivity_status_in_printer_details_screen("connected")