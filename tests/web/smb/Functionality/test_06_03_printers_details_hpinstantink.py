import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"
import logging

class Test_06_03_SMB_Printers_Details_HPInstantInk(object):

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

    def test_01_verify_printer_details_hpinstantink_tab_learnmore_button(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) == True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.verify_printer_details_hpinstantink_tab_learnmore_button()
                self.printers.click_printer_details_hpinstantink_tab_learnmore_button()
                self.printers.verify_new_tab_opened()
                self.printers.verify_hpinstantink_learnmore_newtab_url()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer")                

    def test_02_verify_printer_details_hpinstantink_tab_enrollnow_button(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) == True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.verify_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.click_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_title()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer") 

    def test_03_verify_printers_details_enrollnow_page_back_button_functionality(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) == True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.click_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_title()
                self.printers.click_hpinstantink_enrollnow_page_backtodashboard_button()
                self.home.verify_home_menu_btn()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer") 
    
    def test_04_verify_printers_details_enrollnow_page_continue_button_functionality(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) == True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.click_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_title()
                self.printers.click_hpinstantink_enrollnow_page_continue_button()
                self.printers.verify_hpinstantink_tab_enrollnow_details_page_title()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer") 

    def test_05_verify_printers_details_enrollnow_details_page_back_button_functionality(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) == True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.click_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_title()
                self.printers.click_hpinstantink_enrollnow_page_continue_button()
                self.printers.verify_hpinstantink_tab_enrollnow_details_page_plan_widget()
                self.printers.click_hpinstantink_tab_enroll_enrollnow_page_backtodashboard_button()
                self.home.verify_home_menu_btn()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer") 