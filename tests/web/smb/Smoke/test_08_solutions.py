import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

class Test_08_SMB_Solutions(object):

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
        self.solutions = self.fc.fd["solutions"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder()        

    def test_01_verify_solutions_ui_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516295
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519152
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519147
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        
        #verify solution page
        self.home.click_solutions_menu_btn()

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("solutions_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "solutions_screenshot/{}_solutions_localization.png".format(self.locale))

        self.solutions.verify_solutions_title()
        self.solutions.verify_solutions_description()
       
        #verify hp plus section
        self.solutions.verify_solutions_hp_plus_title()
        self.solutions.verify_solutions_hp_plus_status()
        hp_plus_desc="HP Plus (or HP+) is a revolutionary printing solution that comes free with select HP OfficeJet and LaserJet Printers"
        assert hp_plus_desc==self.solutions.verify_solutions_hp_plus_description()
        self.solutions.verify_solutions_printers_status_activated_text()
        self.solutions.verify_solutions_learn_more_about_hp_plus_link()
        
        #verify smart security
        self.solutions.verify_solutions_smart_security_title()
        self.solutions.verify_solutions_smart_security_description()
        self.solutions.verify_solutions_smart_security_button()
        
        #verify print anywhere
        self.solutions.verify_solutions_print_anywhere_title()
        self.solutions.verify_solutions_print_anywhere_description()
        self.solutions.verify_solutions_print_anywhere_button()

        #verify sustainability forest first
        self.solutions.verify_solutions_sustainability_forest_first_title()
        self.solutions.verify_solutions_sustainability_forest_first_description()
        self.solutions.verify_solutions_sustainability_forest_first_button()
        
        if self.solutions.verify_solutions_hp_smart_pro_is_displayed(displayed=False) ==True:
            logging.info("HP Smart Pro entitlenment is not active")
        else:    
            #verify hp smart pro section
            self.solutions.verify_solutions_discover_all_features_link()
            self.solutions.verify_solutions_hp_smart_pro_title()
            self.solutions.verify_solutions_hp_smart_pro_status()
            hp_pro_desc="HP Smart Pro gives users access to additional features in the HP Smart App"
            assert hp_pro_desc == self.solutions.verify_solutions_hp_smart_pro_description()
        
            #verify hp smart pro scan destinations
            self.solutions.verify_solutions_scan_destinations_title()
            self.solutions.verify_solutions_scan_destinations_description()

            #verify hp smart pro advanced scan
            self.solutions.verify_solutions_advanced_scan_title()
            self.solutions.verify_solutions_advanced_scan_description()