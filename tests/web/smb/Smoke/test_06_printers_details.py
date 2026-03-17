import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

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
        self.home.click_printers_menu_btn()
        return self.printers.verify_printers_page(table_load=False)

    def test_01_verify_printer_detail_screen_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516088
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519691
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519694
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519695
        
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_table_refresh_button()
        self.printers.verify_printer_details_last_updated_date_time()
        self.printers.verify_printer_details_screen_estimated_supply_chart()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.verify_printer_details_screen_printer_model()
        self.printers.verify_printer_details_screen_printer_location()
        self.printers.verify_printer_details_screen_printer_connectivity()
        self.printers.verify_printer_details_screen_printer_device_status()
        # self.printers.verify_printer_details_screen_printer_security_status()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_additional_settings_title()
        self.printers.verify_printer_details_screen_printer_info_title()

    def test_02_verify_printer_detail_screen_overview_tab_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519737

        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #printer info validation
        self.printers.verify_printer_overview_serial_number_title()
        self.printers.verify_printer_overview_serial_number()
        self.printers.verify_printer_details_screen_overview_network()
        self.printers.verify_printer_details_screen_overview_network_ip_address()
        self.printers.verify_printer_details_screen_overview_network_host_name()
        self.printers.verify_printer_details_screen_overview_network_summary_link()
        self.printers.verify_printer_details_screen_overview_firmware_title()
        self.printers.verify_printer_details_screen_overview_firmware()
        # self.printers.verify_printer_details_screen_overview_smart_security()
        # self.printers.verify_printer_details_screen_overview_smart_security_manage_link()

        #Overview: Scan Destinations field validation
        if self.printers.verify_printers_details_scan_destinations_settings_is_displayed(displayed=False) is True:
            logging.info("Scan destinations is not active for this connected printer")
        else: 
            self.printers.verify_printer_details_screen_overview_settings_scan_title()
            expected_scan_email_title="Scan to Email"
            assert expected_scan_email_title == self.printers.verify_printer_settings_scan_to_email()
            self.printers.verify_printer_settings_scan_to_email_desc()
            self.printers.verify_printer_settings_scan_to_email_setup_button()
            expected_scan_cloud_title="Scan to Cloud"
            assert expected_scan_cloud_title == self.printers.verify_printer_settings_scan_to_cloud()
            self.printers.verify_printer_settings_scan_to_cloud_desc()
            self.printers.verify_printer_settings_scan_to_cloud_setup_button()
            if self.printers.verify_printer_settings_set_up_printer_fax_title_is_displayed() is True:
                self.printers.verify_printer_settings_set_up_printer_fax_title()
                self.printers.verify_printer_settings_set_up_printer_fax_set_up_button()

    def test_03_verify_printer_details_solutions_tab_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519776

        # To verify solution tab ui 
        
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_solutions_title()
        self.printers.click_printer_solutions_tab()

        #To verify smart security 
        if self.printers.verify_printer_details_solutions_smart_security_title_is_displayed() is True:
            self.printers.verify_printer_solutions_smart_security_title()
            self.printers.verify_printer_solutions_smart_security_description()
            self.printers.verify_printer_solutions_smart_security_manage_link()

        #To verify print anywhere 
        if self.printers.verify_printer_solutions_print_anywhere_manage_link_is_displayed() is True:
            self.printers.verify_printer_solutions_print_anywhere_title()
            self.printers.verify_printer_solutions_print_anywhere_description()
            self.printers.verify_printer_solutions_print_anywhere_manage_link()

        #To verify sustainability 
        if self.printers.verify_printer_solutions_sustainability_learn_more_link_is_displayed() is True:
            self.printers.verify_printer_solutions_sustainability_title()
            self.printers.verify_printer_solutions_sustainability_description()
            self.printers.verify_printer_solutions_sustainability_learn_more_link()

    def test_04_verify_printer_detail_screen_overview_tab_print_test_page_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/edit/33349610

        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.click_printer_details_screen_overview_print_test_page_button()
        self.printers.verify_printer_details_screen_overview_print_test_page_title()
        self.printers.verify_printer_details_screen_overview_print_test_page_desc()
        self.printers.verify_printer_details_screen_overview_print_test_page_drivers_required_title()
        self.printers.verify_printer_details_screen_overview_print_test_page_drivers_required_desc()
        self.printers.verify_printer_details_screen_overview_print_test_page_install_hp_software_hyperlink()
        self.printers.verify_printer_details_screen_overview_print_test_page_cancel_button()
        self.printers.verify_printer_details_screen_overview_print_test_page_print_button()    
    
    def test_05_verify_printer_detail_screen_hpinstantink_tab_ui(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) is True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            self.printers.verify_printers_details_screen_hpinstantink_tab_header()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.verify_printer_details_hpinstantink_tab_instantink_label()
                self.printers.verify_printer_details_hpinstantink_tab_description()
                self.printers.verify_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.verify_printer_details_hpinstantink_tab_learnmore_button()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer")

    def test_06_verify_printers_details_enrollnow_page_ui(self):
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        if self.printers.verify_printer_details_screen_hpinstantink_is_displayed(displayed=False) is True:
            logging.info("HP Instant Ink tab is not displaying")
        else:
            self.printers.click_printer_details_screen_hpinstantink_tab()
            if self.printers.verify_printer_details_hpinstantink_tab_status() == "Eligible":
                self.printers.click_printer_details_hpinstantink_tab_enrollnow_button()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_title()
                # self.printers.verify_printer_details_hpinstantink_enrollnow_page_desc()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_learnmore_link()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_continue_button()
                self.printers.verify_printer_details_hpinstantink_enrollnow_page_backtodashboard_button()
            else:
                self.printers.verify_printer_details_hpinstantink_tab_data_unavailable_msg()
                logging.info("HP Instant Ink tab is not supported by printer")

    def test_07_verify_printer_details_additional_settings_tab_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        self.printers.click_printer_details_screen_additional_settings_tab()
        
        #verify additional settings tab 
        self.printers.verify_tools_widget_printer_information_button()
        self.printers.verify_tools_widget_asset_tracking_button()
        self.printers.verify_tools_widget_restart_printer_button()
        self.printers.verify_settings_widget_date_and_time_button()
        self.printers.verify_settings_widget_international_button()

    def test_08_verify_additional_settings_printer_information_screen_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_printer_information_button()

        ############# verify column headers #############
        self.printers.verify_additional_settings_printer_info_title()
        self.printers.verify_additional_settings_printer_info_table_product_name_title()
        self.printers.verify_additional_settings_printer_info_table_product_number_title()
        self.printers.verify_additional_settings_printer_info_table_product_serial_number_title()
        self.printers.verify_additional_settings_printer_info_table_service_id_title()
        self.printers.verify_additional_settings_printer_info_table_device_name_title()
        self.printers.verify_additional_settings_printer_info_table_asset_number_title()
        self.printers.verify_additional_settings_printer_info_table_firmware_version_title()
        self.printers.verify_additional_settings_printer_info_table_country_region_title()
        self.printers.verify_additional_settings_printer_info_popup_close_button()
        self.printers.click_additional_settings_printer_info_popup_close_button()

    def test_09_verify_printer_information_popup_details(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        expected_serial_value = self.printers.get_printer_details_overview_serial_number()
        expected_device_name = self.printers.get_printer_details_overview_device_name()
        expected_firmware_version = self.printers.get_printer_details_overview_firmware_version()
        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_printer_information_button()
        # assert expected_serial_value == self.printers.get_printer_info_serial_number()
        assert expected_device_name == self.printers.get_printer_info_popup_device_name()
        assert expected_firmware_version == self.printers.get_printer_info_popup_firmware_version()
        actual_product_name = self.printers.get_printer_info_popup_product_header()
        assert actual_product_name == self.printers.get_printer_info_product_name()
        self.printers.click_additional_settings_printer_info_popup_close_button()

    def test_10_verify_printer_additional_settings_asset_tracking_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_asset_tracking_button()

        #verify asset tracking window
        self.printers.verify_additional_settings_asset_tracking_tab_title()
        self.printers.verify_additional_settings_asset_tracking_tab_desc()
        self.printers.verify_additional_settings_asset_tracking_devicename_label()
        self.printers.verify_additional_settings_asset_tracking_asset_number_label()
        self.printers.verify_additional_settings_asset_tracking_company_name_label()
        self.printers.verify_additional_settings_asset_tracking_contact_person_label()
        self.printers.verify_additional_settings_asset_tracking_cancel_button()
        self.printers.verify_additional_settings_asset_tracking_save_button()

    def test_11_verify_printer_additional_settings_asset_tracking_tab_info(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        expected_device_name = self.printers.get_printer_details_screen_printer_name()
        # expected_device_location = self.printers.get_printer_details_screens_printer_location()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_asset_tracking_button()
        self.printers.verify_additional_settings_asset_tracking_tab_title()
        assert expected_device_name == self.printers.get_additional_settings_asset_tracking_tab_device_name()
        # assert expected_device_location == self.printers.get_additional_settings_asset_tracking_tab_location_name()

    def test_12_verify_printer_additional_settings_asset_tracking_save_button(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_asset_tracking_button()
        self.printers.verify_additional_settings_asset_tracking_tab_title()
        self.printers.verify_additional_settings_asset_tracking_save_button_status("disabled")
        self.printers.clear_additional_settings_asset_tracking_device_name()
        self.printers.verify_additional_settings_asset_tracking_save_button_status("enabled")
        self.printers.click_additional_settings_asset_tracking_cancel_button()

    def test_13_verify_printer_additional_settings_restart_printer_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_restart_printer_button()

        #verify restart printer window
        self.printers.verify_additional_settings_restart_printer_title()
        self.printers.verify_additional_settings_restart_printer_desc()
        self.printers.verify_additional_settings_restart_printer_warning_icon()
        self.printers.verify_additional_settings_restart_printer_notification_text()
        self.printers.verify_additional_settings_restart_printer_cancel_button()
        self.printers.verify_additional_settings_restart_printer_restart_button()
        self.printers.click_additional_settings_restart_printer_cancel_button()
        #verify printer details screen
        self.printers.verify_printer_details_screen_printer_name()

    def test_14_verify_printer_additional_settings_date_and_time_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_date_and_time_button()

        #verify date and time window
        self.printers.verify_additional_settings_date_and_time_title()
        # self.printers.verify_additional_settings_current_printer_date_label()
        self.printers.verify_additional_settings_current_printer_date_value()
        # self.printers.verify_additional_settings_current_printer_time_label()
        self.printers.verify_additional_settings_current_printer_time_value()
        self.printers.verify_additional_settings_current_printer_time_zone_label()
        self.printers.verify_additional_settings_current_printer_time_zone_value()
        self.printers.verify_additional_settings_date_and_time_note_label()
        self.printers.verify_additional_settings_date_and_time_note_text1()
        self.printers.verify_additional_settings_date_and_time_note_text2()
        self.printers.verify_additional_settings_change_date_and_time_button()
        self.printers.verify_additional_settings_change_date_and_time_close_button()
        #verify printer details screen
        self.printers.verify_printer_details_screen_printer_name()

    def test_15_verify_printer_change_date_and_time_select_method_wizard_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_date_and_time_button()
        self.printers.click_additional_settings_change_date_and_time_button()

        #verify change date and time - Step 1: Select your method window ui
        self.printers.verify_change_date_and_time_wizard_title()
        self.printers.verify_change_date_and_time_wizard_methods()

        self.printers.verify_change_date_and_time_wizard_select_method_title()
        self.printers.verify_change_date_and_time_wizard_select_method_description()

        self.printers.verify_change_date_and_time_wizard_configure_sync_with_computer_method()
        self.printers.verify_change_date_and_time_wizard_configure_manually_adjust_time_method()

        self.printers.click_change_date_and_time_wizard_configure_manually_adjust_time_method()
        self.printers.click_change_date_and_time_wizard_configure_sync_with_computer_method()

        self.printers.verify_change_date_and_time_wizard_cancel_button()
        self.printers.verify_change_date_and_time_wizard_next_button()

    def test_16_verify_printer_change_date_and_time_configure_settings_wizard_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        self.printers.click_printer_details_screen_additional_settings_tab()
        self.printers.click_additional_settings_date_and_time_button()
        self.printers.click_additional_settings_change_date_and_time_button()
        self.printers.click_change_date_and_time_wizard_configure_sync_with_computer_method()
        self.printers.click_change_date_and_time_wizard_next_button()

        #verify change date and time - Step 2: Configure settings window ui
        self.printers.verify_change_date_and_time_wizard_configure_settings_title()
        self.printers.verify_configure_date_and_time_wizard_select_date_format_title()
        self.printers.verify_configure_date_and_time_wizard_select_time_format_title()

        # self.printers.verify_configure_date_and_time_wizard_date_picker_dropdown()
        self.printers.verify_configure_date_and_time_wizard_time_zone_title()
        self.printers.verify_configure_date_and_time_wizard_time_zone_description()
        self.printers.verify_configure_date_and_time_wizard_time_zone_dropdown()

        self.printers.verify_configure_date_and_time_wizard_daylight_saving_time_settings_title()
        self.printers.verify_configure_date_and_time_wizard_daylight_saving_time_settings_description()
        self.printers.verify_configure_date_and_time_wizard_daylight_saving_time_settings_toggle()
        self.printers.verify_configure_date_and_time_wizard_daylight_saving_time_settings_toggle_name()
        self.printers.verify_configure_date_and_time_wizard_back_button()

        self.printers.click_configure_date_and_time_wizard_back_button()
        self.printers.verify_change_date_and_time_wizard_select_method_title()
    
    def test_17_verify_printer_detail_screen_usage_tab_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        
        #verify Printer details - Usage tab
        self.printers.click_printer_details_screen_usage_tab()
        self.printers.verify_printers_usage_data_last_updated_time()
        self.printers.verify_printers_usage_data_last_updated_time_close_button()
        self.printers.verify_printers_usage_data_select_usage_view_dropdown()
        self.printers.verify_printers_usage_data_select_usage_view_year_dropdown()
        self.printers.verify_printers_usage_data_print_pages_usage_card()

        if self.printers.verify_printers_usage_data_scan_usage_card_is_displayed() is True:
            self.printers.verify_printers_usage_data_scan_usage_card()

        self.printers.click_printers_usage_data_last_updated_time_close_button()
        self.printers.verify_printers_usage_data_last_updated_time_is_displayed(displayed=False)
    
    def test_18_verify_printer_detail_screen_overview_tab_print_anywhere_card_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519737

        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #Verify print anywhere card UI
        self.printers.verify_printer_details_screen_overview_print_card_title()
        self.printers.verify_printer_details_screen_overview_print_test_page_button()

        self.printers.verify_overview_enable_print_anywhere_toggle_button()
        self.printers.verify_overview_enable_print_anywhere_toggle_button_label()
        self.printers.verify_overview_enable_print_anywhere_toggle_button_description()

        #verify print anywhere toggle button status
        initial_status = self.printers.get_overview_enable_print_anywhere_toggle_button_status()

        #verify require private pickup being displayed 
        if initial_status == "true":
            self.printers.verify_overview_require_private_pickup_toggle_button()
            self.printers.verify_overview_require_private_pickup_toggle_button_label()
            self.printers.verify_overview_require_private_pickup_toggle_button_description()
        else:
            self.printers.verify_overview_require_private_pickup_toggle_button_is_displayed(displayed=False)

    def test_19_verify_printer_detail_screen_order_supplies(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        #verify estimated supply levels container 
        self.printers.verify_printer_details_screen_supplies_level_container()
        self.printers.verify_printer_details_screen_supplies_level_container_label()
        self.printers.verify_printer_details_screen_order_supplies_button()

        #verify printer supplies cartridges
        self.printers.verify_printer_details_screen_printer_supplies_cartridge_K()
        self.printers.verify_printer_details_screen_printer_supplies_cartridge_C()
        self.printers.verify_printer_details_screen_printer_supplies_cartridge_M()
        self.printers.verify_printer_details_screen_printer_supplies_cartridge_Y()

        self.printers.click_printer_details_screen_order_supplies_button()
        self.printers.verify_new_tab_opened()
        self.printers.verify_printer_order_supplies_url()
    
    def test_20_verify_printer_detail_screen_install_hp_software_popup_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()

        #verify install hp software ui
        self.printers.verify_install_hp_software_popup()
        self.printers.verify_install_hp_software_popup_title()
        self.printers.verify_install_hp_software_popup_driver_download_hyperlink()
        self.printers.verify_install_hp_software_popup_cancel_button()
        self.printers.verify_install_hp_software_popup_install_button()

        #verify install hp software cancel button
        self.printers.click_install_hp_software_popup_cancel_button()
        self.printers.verify_printer_details_screen_printer_name()

    def test_21_verify_printer_detail_screen_scan_to_email_setup_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #Overview: Scan Destinations field validation
        if self.printers.verify_printers_details_scan_destinations_settings_is_displayed(displayed=False) is True:
            logging.info("Scan destinations is not active for this connected printer")
        else: 
            self.printers.verify_printer_details_screen_overview_settings_scan_title()
            expected_scan_email_title="Scan to Email"
            assert expected_scan_email_title == self.printers.verify_printer_settings_scan_to_email()
            self.printers.verify_printer_settings_scan_to_email_setup_button()
            scan_to_email_btn_status = self.printers.get_printer_settings_scan_to_email_setup_button_status()

            if scan_to_email_btn_status == "Set Up":
                self.printers.click_printer_settings_scan_to_email_setup_button()
                self.printers.verify_printer_settings_scan_to_email_setup_screen()
                self.printers.verify_printer_scan_to_email_setup_page_title()
                self.printers.verify_printer_scan_to_email_setup_page_cancel_button()
                self.printers.verify_printer_scan_to_email_setup_page_save_button(displayed=False)                
                self.printers.verify_printer_scan_to_email_setup_scan_destination_name_field_title()
                self.printers.verify_printer_scan_to_email_setup_scan_destination_name_field()
                self.printers.verify_printer_scan_to_email_setup_scan_destination_name_field_default_text()

                self.printers.verify_printer_scan_to_email_setup_email_information_field_title()
                self.printers.verify_printer_scan_to_email_setup_email_information_field_desc()
                self.printers.verify_printer_scan_to_email_setup_email_information_field()
                self.printers.verify_printer_scan_to_email_setup_email_information_field_default_text()

                self.printers.verify_printer_scan_to_email_setup_subject_field()
                self.printers.verify_printer_scan_to_email_setup_subject_field_default_text()

                self.printers.verify_printer_scan_to_email_setup_message_body_field()
                self.printers.verify_printer_scan_to_email_setup_message_body_field_default_text()

                self.printers.verify_printer_scan_to_email_setup_settings_field()
                self.printers.verify_printer_scan_to_email_setup_settings_field_title()

                self.printers.verify_printer_scan_to_email_setup_file_type_dropdown()
                self.printers.verify_printer_scan_to_email_setupfile_type_dropdown_title()

                self.printers.verify_printer_scan_to_email_setup_security_pin_title()
                self.printers.verify_printer_scan_to_email_setup_security_pin_toggle_btn()
                self.printers.verify_printer_scan_to_email_setup_security_pin_toggle_btn_label()
                self.printers.verify_printer_scan_to_email_setup_security_pin_toggle_btn_descripton()
                # self.printers.verify_printer_scan_to_email_setup_security_pin_field()
                # self.printers.verify_printer_scan_to_email_setup_enter_security_pin_field()
                # self.printers.verify_printer_scan_to_email_setup_confirm_security_pin_field()

                self.printers.click_printer_scan_to_email_setup_page_cancel_button()

                self.printers.verify_unsaved_changes_popup()
                self.printers.verify_unsaved_changes_popup_desc()
                self.printers.verify_unsaved_changes_popup_cancel_button()
                self.printers.verify_unsaved_changes_popup_leave_button()

                self.printers.click_unsaved_changes_popup_cancel_button()
                self.printers.verify_printer_scan_to_email_setup_page_title()
                
                self.printers.click_printer_scan_to_email_setup_page_cancel_button()
                self.printers.click_unsaved_changes_popup_leave_button()
                self.printers.verify_printer_scan_destination_screen()
    
    def test_22_verify_printer_detail_scan_destination_screen_ui(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_overview_title()
        self.printers.verify_printer_details_screen_printer_info_title()

        #Overview: Scan Destinations field validation
        if self.printers.verify_printers_details_scan_destinations_settings_is_displayed(displayed=False) is True:
            logging.info("Scan destinations is not active for this connected printer")
        else: 
            self.printers.verify_printer_details_screen_overview_settings_scan_title()
            expected_scan_email_title="Scan to Email"
            assert expected_scan_email_title == self.printers.verify_printer_settings_scan_to_email()
            self.printers.verify_printer_settings_scan_to_email_setup_button()
            scan_to_email_btn_status = self.printers.get_printer_settings_scan_to_email_setup_button_status()

            if scan_to_email_btn_status == "Manage":
                self.printers.click_printer_settings_scan_to_email_setup_button()
                self.printers.verify_printer_scan_destination_screen()
                self.printers.verify_printer_scan_destination_screen_breadcrumb()
                self.printers.verify_printer_scan_destination_screen_refresh_button()
                self.printers.verify_printer_scan_destination_screen_last_updated_date_time()
                
                self.printers.verify_printer_scan_destination_screen_printer_widget_container()
                self.printers.verify_printer_scan_destination_screen_printer_details_container()
                self.printers.verify_printer_scan_destination_screen_printer_name()
                self.printers.verify_printer_scan_destination_screen_printer_model_name()
                self.printers.verify_printer_scan_destination_screen_printer_status()
                self.printers.verify_printer_scan_destination_screen_printer_status_icon()
                self.printers.verify_printer_scan_destination_screen_printer_details_link()

                self.printers.verify_printer_scan_destination_screen_scan_data_container()
                self.printers.verify_printer_scan_destination_screen_scan_data_email_title()
                self.printers.verify_printer_scan_destination_screen_scan_data_email_icon()
                self.printers.verify_printer_scan_destination_screen_scan_data_email_count()
                self.printers.verify_printer_scan_destination_screen_scan_data_cloud_title()
                self.printers.verify_printer_scan_destination_screen_scan_data_email_icon()
                self.printers.verify_printer_scan_destination_screen_scan_data_cloud_count()

                self.printers.verify_printer_scan_destination_screen_scan_tabs_container()
                self.printers.verify_printer_scan_destination_screen_scan_email_tab()
                self.printers.verify_printer_scan_destination_screen_scan_cloud_tab()

                self.printers.verify_printer_scan_destination_screen_search_field()
                self.printers.verify_printer_scan_destination_screen_scan_to_email_table()

                self.printers.click_printer_scan_destination_screen_scan_cloud_tab()
                self.printers.verify_printer_scan_destination_screen_scan_to_cloud_table()

    def test_23_verify_printer_details_screen_overview_tab_fax_setup_wizard(self):
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

            #Verify Fax setup wizard ui
            self.printers.verify_printer_details_screen_overview_tab_fax_setup_wizard_title()
            self.printers.verify_printer_details_fax_setup_wizard_fax_settings_page_title()

            #verify fax setup wizard steps label
            self.printers.verify_printer_details_fax_setup_wizard_fax_settings_label()
            self.printers.verify_printer_details_fax_setup_wizard_voice_and_internet_options_label()
            self.printers.verify_printer_details_fax_setup_wizard_setup_configuration_label()
            self.printers.verify_printer_details_fax_setup_wizard_summary_label()

            #verify footer component
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_cancel_button()

            if fax_button_type == "Manage":
                self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_next_button()            
            else:
                self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_next_button_is_not_displayed()
       
    def test_24_verify_printer_details_fax_setup_wizard_fax_settings_page(self):
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
            self.printers.verify_fax_setup_wizard_fax_settings_page_edit_info_title()
            self.printers.verify_fax_setup_wizard_fax_settings_page_edit_info_description()
            self.printers.verify_fax_setup_wizard_fax_settings_page_select_country_dropdown()
            self.printers.verify_fax_setup_wizard_fax_settings_page_name_field()
            self.printers.verify_fax_setup_wizard_fax_settings_page_fax_number_field()
            self.printers.verify_fax_setup_wizard_fax_settings_page_voice_calls_message()
            self.printers.verify_fax_setup_wizard_fax_settings_page_fax_ring_calls_message()

            #voice calls options
            self.printers.verify_fax_setup_wizard_fax_settings_page_voice_calls_message_yes_option()
            self.printers.verify_fax_setup_wizard_fax_settings_page_voice_calls_message_no_option()

            #distinctive ring for fax calls
            self.printers.verify_fax_setup_wizard_fax_settings_page_fax_ring_calls_message_yes_option()
            self.printers.verify_fax_setup_wizard_fax_settings_page_fax_ring_calls_message_no_option()
     
    def test_25_verify_printer_details_fax_setup_wizard_voice_and_internet_options(self):
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
            self.printers.verify_printer_details_screen_overview_tab_fax_setup_wizard_title()
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_name("test")
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_number("9106756566")
            
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            #Verify voice and internet options ui
            self.printers.verify_printer_details_fax_setup_wizard_voice_and_internet_options_page_title()
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_internet_service_option_text()
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_computer_modem_option_text()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_back_button()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_cancel_button()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_next_button()

            #Verify DSL Internet service options
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_internet_service_yes_option()
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_internet_service_no_option()

            #Verify Computer Modem service options
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_computer_modem_no_option()
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_internet_service_dsl_modem_option()
            self.printers.verify_fax_setup_wizard_voice_and_internet_page_internet_service_dial_up_modem_option()

    def test_26_verify_printer_details_fax_setup_wizard_setup_configuration_page(self):
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
            self.printers.verify_printer_details_screen_overview_tab_fax_setup_wizard_title()
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_name("test")
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_number("9106756566")
            
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            #Verify setup configuration ui
            self.printers.verify_printer_details_fax_setup_wizard_setup_configuration_page_title()
            self.printers.verify_fax_setup_wizard_setup_configuration_page_description_note()

            #verify setup configuration page options
            self.printers.verify_fax_setup_wizard_setup_configuration_page_voice_line_fax_option()
            self.printers.verify_fax_setup_wizard_setup_configuration_page_answering_machine_option()
            self.printers.verify_fax_setup_wizard_setup_configuration_page_dsl_adsl_service_option()
            self.printers.verify_fax_setup_wizard_setup_configuration_page_dsl_adsl_modem_option()
            self.printers.verify_fax_setup_wizard_setup_configuration_page_dial_up_modem_option()

            self.printers.verify_fax_setup_wizard_setup_configuration_page_phone_card_warning_msg()

            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_back_button()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_cancel_button()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_next_button()

    def test_27_verify_printer_details_fax_setup_wizard_setup_summary_page(self):
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
            self.printers.verify_printer_details_screen_overview_tab_fax_setup_wizard_title()
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_name("test")
            self.printers.enter_fax_setup_wizard_fax_settings_page_fax_number("9106756566")
            
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()
            self.printers.click_printer_details_fax_setup_wizard_contextual_footer_next_button()

            #Verify setup summary ui
            self.printers.verify_printer_details_fax_setup_wizard_setup_summary_page_title()
            self.printers.verify_fax_setup_wizard_setup_summary_page_description()

            #verify setup summary page options
            self.printers.verify_fax_setup_wizard_setup_summary_page_company_name_label()
            self.printers.verify_fax_setup_wizard_setup_summary_page_fax_number_label()
            self.printers.verify_fax_setup_wizard_setup_summary_page_auto_answer_label()
            self.printers.verify_fax_setup_wizard_setup_summary_page_distinctive_ring_label()

            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_back_button()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_cancel_button()
            self.printers.verify_printer_details_fax_setup_wizard_contextual_footer_save_button()

            #verify setup summary page options
            actual_company_name = self.printers.verify_fax_setup_wizard_setup_summary_page_company_name_text()
            assert actual_company_name == "test"
            # self.printers.verify_fax_setup_wizard_setup_summary_page_fax_number()