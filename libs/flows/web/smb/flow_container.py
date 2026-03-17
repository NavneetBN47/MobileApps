from MobileApps.libs.flows.web.smb.home import Home
from MobileApps.libs.flows.web.smb.login import Login
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.smb.account import Account
from MobileApps.libs.flows.web.smb.users import Users
from MobileApps.libs.flows.web.smb.printers import Printers
from MobileApps.libs.flows.web.smb.settings import Settings
from MobileApps.libs.flows.web.smb.solutions import Solutions
from MobileApps.libs.flows.web.instant_ink.instsantink_smb import InstantInkSMB
from MobileApps.libs.flows.web.smb.sustainability import Sustainability
from MobileApps.libs.flows.web.smb.hpinstantink import HPInstantInk
from MobileApps.libs.flows.web.smb.helpcenter import HelpCenter
from MobileApps.libs.ma_misc import ma_misc

class CannotGoHomeException(Exception):
    pass

class FlowContainer(object):
    stack_url = {

        "dev": "https://smb.dev.portalshell.int.hp.com/us/en/",
        "pie": "https://smb.pie.portalshell.int.hp.com/us/en/",
        "stage": "https://smb.stage.portalshell.int.hp.com/us/en/",
        "production": "https://admin.hpsmart.com/"
        }

    def __init__(self, driver):
        self.driver = driver
        self.fd = {"login": Login(driver),
                   "hpid": HPID(driver),
                   "home": Home(driver),
                   "account": Account(driver),
                   "users": Users(driver),
                   "printers": Printers(driver),
                   "solutions": Solutions(driver),
                   "settings": Settings(driver),
                   "instantink_smb": InstantInkSMB(driver),
                   "sustainability": Sustainability(driver),
                   "hpinstantink": HPInstantInk(driver),
                    "helpcenter": HelpCenter(driver)}

    @property
    def flow(self):
        return self.fd      

    def navigate(self, stack,language):
        url = self.stack_url[stack].replace("/us/en/", "/" + language + "/")
        return self.driver.navigate(url)

    def login(self, email, pwd):
        self.fd["hpid"].verify_hp_id_sign_in()
        return self.fd["hpid"].login(email, pwd)
    
    def go_home(self, stack, email, pwd, tenantID, language, retry=3):
        for _ in range(retry):
            self.navigate(stack,language)
            if self.fd["home"].verify_home_menu_btn(timeout=10, raise_e=False) is False:
                self.login(email, pwd)
                self.fd["hpid"].handle_privacy_popup()
                self.fd["login"].select_an_organization_to_sign_in(tenantID)
            else:
                self.fd["login"].handle_intercept_survey_modal()
                return True

            if self.fd["home"].verify_home_menu_btn(timeout=10, raise_e=False) is not False:
                self.fd["login"].handle_intercept_survey_modal()
                return True
        raise CannotGoHomeException("After: " + str(retry) + " tries still cannot go home")
    
    def load_localization_files(self,language):
        #load Imagebank file path for the directory-smb
        root_path = ma_misc.web_localization_path_builder(self.driver, "web_localized_strings/smb/")

        #filter and load file paths based on the specified language from smb directory
        specific_language_file_list = self.fd["home"].filter_and_load_file_path_based_on_language(root_path,language)
        
        #to create single layer dictionary for the specified language
        spec_data = self.fd["home"].load_files_and_create_single_layer_dict(specific_language_file_list)
        # Load strings from json file 
        self.driver.load_app_strings("smb", spec_data)