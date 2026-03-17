import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

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
        self.attachment_path = conftest_misc.get_attachment_folder()   

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("printers_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "_screenshhomeot/{}_printers_localization.png".format(self.locale))

        self.home.click_printers_menu_btn()
        return self.printers.verify_printers_page(table_load=False)
   
    def test_01_verify_printers_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516064
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519654

        #verify printer details
        self.printers.verify_printers_page_title()
        self.printers.verify_printers_page_desc()
        self.printers.verify_printer_table_refresh_button()
        self.printers.verify_printer_table_last_updated_date_time()
        self.printers.verify_printer_table_search_box()
        self.printers.verify_printer_table_view_button()
        self.printers.verify_printer_card_view_button()

    def test_02_verify_printers_refresh_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516072
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519655

        cur_time = self.printers.get_sync_time_info()
        self.printers.click_refresh_button()

        # Verify and wait for printers table data load
        self.printers.verify_printers_page(table_load=False)

        new_time = self.printers.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Page last updated ")[1], self.driver.get_timezone(), "%m/%d/%Y at %I:%M:%S %p. Select a printer for detailed information.") == True
        assert new_time != cur_time

    @pytest.mark.parametrize('search_string',  ["invalidname","LaserJet"])
    def test_03_verify_printer_table_view_search_functionality(self,search_string ):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516075
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516076
         
        self.printers.click_printer_table_view_button()
        self.printers.click_table_header_by_name("device_name")
        self.printers.search_printers(search_string, timeout=20)
        self.printers.click_search_clear_button()

    @pytest.mark.parametrize('search_string',  ["invalidname","LaserJet"])
    def test_04_verify_printer_card_view_search_functionality(self,search_string ):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519656
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519657

        # Verify card view data and search printer details
        self.printers.search_printers_card_view(search_string, timeout=20)
        self.printers.click_search_clear_button()

    def test_05_pagination(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516070
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516071
        
        self.printers.click_printer_table_view_button()
        self.printers.verify_all_page_size_options_new([10,25,50,100])
        self.printers.verify_table_displaying_correctly_new(10, page=1)
        self.printers.verify_table_displaying_correctly_new(25, page=1)
        self.printers.verify_table_displaying_correctly_new(50, page=1)
        self.printers.verify_table_displaying_correctly_new(100, page=1)

    def test_06_verify_default_sort(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516073

        self.printers.click_printer_table_view_button()
        self.printers.select_page_size_new("100")
        self.printers.click_table_header_by_name("connectivity")
        self.printers.verify_table_sort("connectivity",["Not connected","Connected"])

    def test_07_verify_sort_change(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516074
        
        self.printers.click_printer_table_view_button()
        self.printers.select_page_size_new("100")
        # To verify sort button in printer table view  
        self.printers.click_table_header_by_name("connectivity")
        self.printers.verify_printers_page(table_load=True)
        self.printers.click_table_header_by_name("connectivity")
        self.printers.verify_table_sort("connectivity",["Connected","Not connected"])