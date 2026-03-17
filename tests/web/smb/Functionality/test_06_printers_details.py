import pytest
import random
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

update = "t_"+str(random.randint(00,99))

class Test_06_SMB_Printers_Details(object):

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

    def test_01_verify_printer_details_screen_printer_action_dropdown(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519692
        
        self.printers.click_printer_table_view_button() 
        # To verify action dropdown in printer detail screen 
        expected_action_dropdown = ["Install HP software", "Edit name and location", "Remove Printer"]
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.click_printer_action_dropdown()
        assert expected_action_dropdown == self.printers.get_printer_action_dropdown_options()

    def test_02_verify_printer_details_edit_printer_name_popup_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/31296122
        
        self.printers.click_printer_table_view_button() 
        # To verify action dropdown edit printer name cancel functionality
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.click_printer_action_dropdown()
        self.printers.select_edit_printer_name_and_location_option()
        
        #edit printer name popup
        self.printers.verify_edit_printer_name_and_location_popup()
        printer_name = self.printers.edit_printer_name_popup_get_printer_name()
        update_printer_name = printer_name + update
        self.printers.enter_printer_name(update_printer_name)
        
        #cancel the edit printer name
        self.printers.click_edit_printer_name_and_location_popup_cancel_button()
        actual_printer_name =self.printers.get_printer_details_screen_printer_name()
        assert actual_printer_name == printer_name

    def test_03_verify_printer_details_edit_printer_name(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519696
        
        self.printers.click_printer_table_view_button() 
        # To verify action dropdown edit printer name save functionality
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.click_printer_action_dropdown()
        self.printers.select_edit_printer_name_and_location_option()
        
        #edit printer name
        self.printers.verify_edit_printer_name_and_location_popup()
        printer_name = self.printers.edit_printer_name_popup_get_printer_name()
        update_printer_name = "QA_Automation" + update
        self.printers.enter_printer_name(update_printer_name)
        # new_printer_name =self.printers.edit_printer_name_popup_get_printer_name()
        
        #save the edit printer name
        self.printers.click_edit_printer_name_and_location_popup_save_button()

        #verify printer name change request in printer details screen
        assert "Request to change the printer name is pending. Check back shortly." == self.printers.get_printer_name_change_request_message()

        #verify printer name change request in edit printer name popup
        self.printers.click_printer_action_dropdown()
        self.printers.select_edit_printer_name_and_location_option()
        assert printer_name == self.printers.edit_printer_name_popup_get_printer_name()
        self.printers.verify_edit_printer_name_popup_name_change_request_msg()
        assert update_printer_name == self.printers.get_edit_printer_name_popup_request_printer_name()        

    def test_04_verify_printer_details_edit_printer_location_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/31296124
        
        self.printers.click_printer_table_view_button() 
        # To verify action dropdown edit printer location cancel functionality
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.click_printer_action_dropdown()
        self.printers.select_edit_printer_name_and_location_option()
       
        #edit location name popup
        self.printers.verify_edit_printer_name_and_location_popup()
        location_name = self.printers.edit_printer_name_popup_get_printer_location()
        update_location_name = location_name + update
        self.printers.enter_location_name(update_location_name)
        
        #cancel the edit location name
        self.printers.click_edit_printer_name_and_location_popup_cancel_button()
        actual_printer_location =self.printers.get_printer_details_screen_printer_location()
        assert actual_printer_location == location_name

    def test_05_verify_printer_details_edit_printer_location_save(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519697
        
        self.printers.click_printer_table_view_button() 
        # To verify action dropdown edit location save functionality 
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.click_printer_action_dropdown()
        self.printers.select_edit_printer_name_and_location_option()
        
        #edit location name
        self.printers.verify_edit_printer_name_and_location_popup()
        location_name = self.printers.edit_printer_name_popup_get_printer_location()
        update_location_name = "Auto_Location" + update
        self.printers.enter_location_name(update_location_name)
        
        #save the edit location name
        self.printers.click_edit_printer_name_and_location_popup_save_button()
    
        #verify printer name change request in printer details screen
        assert "Request to change the printer location is pending. Check back shortly." == self.printers.get_printer_name_change_request_message()

        #verify printer name change request in edit printer name popup
        self.printers.click_printer_action_dropdown()
        self.printers.select_edit_printer_name_and_location_option()
        assert location_name == self.printers.edit_printer_name_popup_get_printer_location()
        self.printers.verify_edit_printer_name_popup_name_change_request_msg()
        assert update_location_name == self.printers.get_edit_printer_location_popup_request_printer_location()