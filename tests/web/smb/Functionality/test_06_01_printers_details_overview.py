import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_06_01_SMB_Printers_Details_Overview(object):

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
        self.solutions = self.fc.fd["solutions"]
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

    def test_01_verify_printer_details_overview_screen_network_summary_popup(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519738
        
        self.printers.click_printer_table_view_button()  
        # To verify summary link details
        self.printers.verify_and_click_connected_printer()
        printer_connectivity_status=self.printers.get_printer_details_screen_printer_connectivity_status()
        printer_network_ip_address =self.printers.get_printer_network_ip_address()
        printer_network_hostname =self.printers.get_printer_network_hostname()

        self.printers.click_printer_overview_network_summary_link()

        #verify network summary popup details
        self.printers.verify_network_summary_popup_title()
        
        # To verify Wired connection details
        assert "wired" == self.printers.get_network_summary_popup_wired_title()
        self.printers.verify_network_summary_popup_wired_connectivity_status_title()
        assert printer_connectivity_status == self.printers.get_network_summary_popup_wired_connectivity_status()

        assert  "Host Name" == self.printers.get_printer_network_summary_popup_host_name_title()
        assert printer_network_hostname == self.printers.get_printer_network_summary_popup_host_name()

        assert  "IP Address" == self.printers.get_printer_network_summary_popup_ip_address_title()
        assert  printer_network_ip_address == self.printers.get_printer_network_summary_popup_ip_address()

        assert  "Hardware (MAC) Address" == self.printers.get_printer_network_summary_popup_hardware_address_title()
        
        #To verify Wireless connection
        assert "wireless" == self.printers.get_printer_network_summary_popup_wireless_title()
        self.printers.verify_printer_network_summary_popup_wireless_status_title()
        
        #To verify WiFi connection
        self.printers.verify_printer_network_summary_popup_wifi_status_title()
        assert  "Wi-Fi Direct Name" == self.printers.get_printer_network_summary_popup_wifi_title()
        # assert  "Channel" == self.printers.get_printer_network_summary_popup_wifi_channel_title()
        
        #To verify Bluetooth connection
        self.printers.verify_printer_network_summary_popup_bluetooth_title()
        self.printers.verify_printer_network_summary_popup_bluetooth_status_title()
        self.printers.click_printer_network_summary_popup_close_button()

    # def test_02_verify_printer_overview_screen_manage_hyperlink(self):
    #     #https://hp-testrail.external.hp.com/index.php?/cases/view/30519739
        
    #     # To verify Manage link details 
    #     self.printers.verify_and_click_connected_printer()
    #     self.printers.click_printer_overview_manage_hyperlink()
    #     self.printers.verify_smart_security_setting_page()

    def test_03_verify_printer_overview_printer_information(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519740
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519741
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519742
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519743
        
        self.printers.click_printer_table_view_button()  
        self.printers.verify_and_click_connected_printer()
        #To verify Serial Number
        self.printers.verify_printer_overview_serial_number_title()
        
        #To verify Network section
        self.printers.verify_printer_details_screen_overview_network()
        # assert "IP Address:" == self.printers.get_printer_overview_ip_address_title()

         #To verify Firmware
        self.printers.verify_printer_details_screen_overview_firmware()
        
        # #To verify smart security section
        # self.printers.verify_printer_details_screen_overview_smart_security()
        # smart_secuirty_status = self.printers.get_printer_details_screen_printer_security_status()
        # assert smart_secuirty_status == self.printers.get_printer_overview_smart_security_status()

    def test_04_verify_printer_details_fax_setup_wizard_unsaved_changes_popup(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        if self.printers.verify_printer_settings_set_up_printer_fax_title_is_displayed() is True:
            self.printers.verify_printer_settings_set_up_printer_fax_title()
            fax_button_type = self.printers.get_printer_settings_fax_set_up_button_type()
            if fax_button_type == "Manage":
                self.printers.verify_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printers_fax_settings_open_fax_setup_wizard_button()
            else:
                self.printers.click_printer_settings_set_up_printer_fax_set_up_button()

            #Verify Fax settings page ui
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_name("test")
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_number("9106756566")
            
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_cancel_button()

            self.printers.verify_fax_setup_wizard_unsaved_changes_popup()
            # self.printers.verify_fax_setup_wizard_unsaved_changes_popup_desc()
            self.printers.verify_fax_setup_wizard_unsaved_changes_popup_cancel_button()
            self.printers.verify_fax_setup_wizard_unsaved_changes_popup_leave_button()
            self.printers.click_fax_setup_wizard_unsaved_changes_popup_cancel_button()

            self.printers.verify_printer_details_fax_setup_wizard_setup_summary_page_title()

    def test_05_verify_fax_setup_wizard_unsaved_changes_popup_leave_functionality(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        if self.printers.verify_printer_settings_set_up_printer_fax_title_is_displayed() is True:
            self.printers.verify_printer_settings_set_up_printer_fax_title()
            fax_button_type = self.printers.get_printer_settings_fax_set_up_button_type()
            if fax_button_type == "Manage":
                self.printers.verify_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printers_fax_settings_open_fax_setup_wizard_button()
            else:
                self.printers.click_printer_settings_set_up_printer_fax_set_up_button()

            #Verify Fax settings page ui
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_name("test")
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_number("9106756566")
            
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_cancel_button()
            self.printers.click_fax_setup_wizard_unsaved_changes_popup_leave_button()
            
            self.printers.verify_printer_details_screen_printer_name()
    
    def test_06_verify_printer_details_fax_setup_wizard_back_btn_functionality(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        if self.printers.verify_printer_settings_set_up_printer_fax_title_is_displayed() is True:
            self.printers.verify_printer_settings_set_up_printer_fax_title()
            fax_button_type = self.printers.get_printer_settings_fax_set_up_button_type()
            if fax_button_type == "Manage":
                self.printers.verify_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printers_fax_settings_open_fax_setup_wizard_button()
            else:
                self.printers.click_printer_settings_set_up_printer_fax_set_up_button()

            #Verify Fax settings page ui
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_name("test")
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_number("9106756566")
            
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            self.printers.verify_printer_details_fax_setup_wizard_setup_summary_page_title()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_back_button()

            self.printers.verify_printer_details_fax_setup_wizard_setup_configuration_page_title()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_back_button()

            self.printers.verify_printer_details_fax_setup_wizard_voice_and_internet_options_page_title()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_back_button()

            self.printers.verify_printer_details_fax_setup_wizard_fax_settings_page_title()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_back_button(displayed=False)       

    def test_07_verify_printer_details_fax_setup_wizard_fax_settings_page_search_functionality(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        if self.printers.verify_printer_settings_set_up_printer_fax_title_is_displayed() is True:
            self.printers.verify_printer_settings_set_up_printer_fax_title()
            fax_button_type = self.printers.get_printer_settings_fax_set_up_button_type()
            if fax_button_type == "Manage":
                self.printers.verify_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printer_settings_set_up_printer_fax_manage_button()
                self.printers.click_printers_fax_settings_open_fax_setup_wizard_button()
            else:
                self.printers.click_printer_settings_set_up_printer_fax_set_up_button()

            #Verify valid search functionality
            self.printers.click_fax_setup_wizard_fax_settings_page_select_country_dropdown()
            self.printers.enter_country_name_fax_setup_wizard_fax_settings_page_country_dropdown("India")
            self.printers.select_country_name_fax_setup_wizard_fax_settings_page_country_dropdown()

            #Verify invalid search functionality
            self.printers.click_fax_setup_wizard_fax_settings_page_select_country_dropdown()
            self.printers.enter_country_name_fax_setup_wizard_fax_settings_page_country_dropdown("test")
            assert "No results found" == self.printers.verify_fax_setup_wizard_fax_settings_page_country_dropdown_no_items_msg()
  
    def test_08_verify_overview_tab_print_anywhere_toggle_button_functionality(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #verify print anywhere toggle button status
        initial_status = self.printers.get_overview_enable_print_anywhere_toggle_button_status()

        #verify require private pickup being displayed 
        if initial_status == "true":
            self.printers.verify_overview_require_private_pickup_toggle_button()
        else:
            self.printers.verify_overview_require_private_pickup_toggle_button_is_displayed(displayed=False)
        
        #verify modified print anywhere toggle button status
        self.printers.click_overview_enable_print_anywhere_toggle_button()
        assert initial_status != self.printers.get_overview_enable_print_anywhere_toggle_button_status()

    def test_09_verify_print_anywhere_toggle_button_status_with_solutions_screen(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #verify print anywhere toggle button status
        initial_status = self.printers.get_overview_enable_print_anywhere_toggle_button_status()
        printer_name = self.printers.get_printer_details_screen_printer_name()
                
        #Verifying Solutions - Print anywhere screen print anywhere toggle button status
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.smart_security_search_printers(printer_name, timeout=20)

        assert initial_status == self.solutions.get_solutions_print_anywhere_toggle_button_status()

        #modify Printer details screen - print anywhere toggle button status
        self.home.click_printers_menu_btn()
        self.printers.click_printer_table_view_button()
        self.printers.search_printers(printer_name, timeout=20)
        self.printers.click_first_entry_link()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()
        
        self.printers.click_overview_enable_print_anywhere_toggle_button()
        modified_status = self.printers.get_overview_enable_print_anywhere_toggle_button_status()
                    
        #Verifying Solutions - Print anywhere screen print anywhere toggle button status
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.smart_security_search_printers(printer_name, timeout=20)
        
        assert modified_status == self.solutions.get_solutions_print_anywhere_toggle_button_status()
    
    def test_10_verify_private_pickup_toggle_button_status_with_solutions_screen(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #verify print anywhere toggle button status
        initial_print_anywhere_status = self.printers.get_overview_enable_print_anywhere_toggle_button_status()
        printer_name = self.printers.get_printer_details_screen_printer_name()

        #verify require private pickup being displayed 
        if initial_print_anywhere_status == "true":
            self.printers.verify_overview_require_private_pickup_toggle_button()
        else:
            self.printers.click_overview_enable_print_anywhere_toggle_button()
        
        initial_private_pickup_status = self.printers.get_overview_require_private_pickup_toggle_button_status()
                
        #Verifying Solutions - Print anywhere screen private pickup toggle button status
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.smart_security_search_printers(printer_name, timeout=20)

        assert initial_private_pickup_status == self.solutions.get_solutions_private_pickup_toggle_button_status()

        #modify Printer details screen - print anywhere toggle button status
        self.home.click_printers_menu_btn()
        self.printers.click_printer_table_view_button()
        self.printers.search_printers(printer_name, timeout=20)
        self.printers.click_first_entry_link()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()
        
        self.printers.click_overview_enable_print_anywhere_toggle_button()
        self.printers.verify_overview_require_private_pickup_toggle_button_is_displayed(displayed=False)
                    
        #Verifying Solutions - Print anywhere screen private pickup toggle button status
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.smart_security_search_printers(printer_name, timeout=20)
        
        #private pickup status remains same even when print anywhere is turned off
        assert initial_private_pickup_status == self.solutions.get_solutions_private_pickup_toggle_button_status()