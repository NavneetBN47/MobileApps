import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_07_01_SMB_Smart_Security(object):

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
        self.account = self.fc.fd["account"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
        
    def test_01_verify_smart_security_printer_details_hyperlink(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30521021
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen
        self.solutions.verify_and_click_connected_printer()
        #verify printer details in smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.click_smart_security_detail_screen_printer_detail_link()
        #verify printer details in printer screen
        self.printers.verify_printer_details_screen_printer_name()

    def test_02_verify_smart_security_details_tool_tip_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519729
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519829
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519734
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519871
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519735
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519881
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519736
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30528217     
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        
        #verify admin password tool tip
        self.solutions.verify_admin_password_tool_tip()
        self.solutions.click_admin_password_tool_tip()
        self.solutions.verify_admin_password_pop_up_title()
        self.solutions.verify_admin_password_pop_up_desc()
        self.solutions.verify_admin_password_pop_up_close_button()
        self.solutions.click_admin_password_pop_up_close_button()
        
        # #verify automatic firmware update tool tip
        # self.solutions.verify_automatic_firmware_update_tool_tip()
        # self.solutions.click_automatic_firmware_update_tool_tip()
        # self.solutions.verify_automatic_firmware_update_pop_up_title()
        # self.solutions.verify_automatic_firmware_update_pop_up_desc()
        # self.solutions.verify_automatic_firmware_update_pop_up_close_button()
        # self.solutions.click_automatic_firmware_update_pop_up_close_button()
        
        #verify snmp V1/V2 write tool tip
        self.solutions.verify_snmp_tool_tip()
        self.solutions.click_snmp_tool_tip()
        self.solutions.verify_snmp_pop_up_desc()
        self.solutions.verify_snmp_pop_up_close_button()
        self.solutions.click_snmp_pop_up_close_button()
        self.solutions.verify_snmp_expand_button()
        
        #verify snmp V3 tool tip
        self.solutions.verify_snmp_v3_tool_tip()
        self.solutions.click_snmp_v3_tool_tip()
        self.solutions.verify_snmp_v3_pop_up_desc()
        self.solutions.verify_snmp_v3_pop_up_close_button()
        self.solutions.click_snmp_v3_pop_up_close_button()
        self.solutions.verify_snmp_v3_expand_button()

    def test_03_verify_smart_security_details_expand_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/edit/30519795

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()
        
        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()
        
        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        
        #verify admin password expand button
        self.solutions.click_admin_password_expand_button()
        self.solutions.verify_admin_password_status_desc()
        self.solutions.click_admin_password_expand_button()
        # self.solutions.click_automatic_firmware_update_expand_button()
        # # self.solutions.verify_automatic_firmware_update_status_desc()
        # self.solutions.click_automatic_firmware_update_expand_button()
        self.solutions.click_snmp_expand_button()
        self.solutions.verify_snmp_toggle_button()
        self.solutions.verify_snmp_status_desc()
        self.solutions.click_snmp_expand_button()

    # def test_04_verify_smart_security_printer_details(self):
    #     #
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
    #     #navigate to solution screen
    #     self.home.click_solutions_menu_btn()
    #     self.solutions.verify_solutions_title()
    #     #navigate to smart security screen
    #     self.solutions.click_solutions_smart_security_button()
    #     self.solutions.verify_smart_security_title()
    #     self.solutions.smart_security_search_printers("Marconi", timeout=30)  
    #     #get printer info from table
    #     printer_info_from_table=self.solutions.get_printer_info_in_smart_scurity_table_view()
    #     #navigate to smart security detail screen
    #     self.solutions.click_printer_first_entry_link()
    #     #verify smart security detail screen
    #     assert printer_info_from_table == self.solutions.get_printer_info_in_smart_scurity_detail_screen()

    def test_05_verify_smart_security_printer_details_with_printer_screen_details(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30521021
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()
        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        #get printer info from smart security detail screen
        smart_security_printer_info=self.solutions.get_printer_info_in_smart_scurity_detail_screen()
        #naviagte to printer detail screen
        self.solutions.click_smart_security_detail_screen_printer_detail_link()
        #validate  printer info from printer detail screen with smart security
        assert smart_security_printer_info == self.printers.get_printer_details_in_printer_screen_from_smart_security()
        
    def test_06_verify_smart_security_monitoring_ui_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519309
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519411
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()
        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        toggle_status_message=self.solutions.get_security_monitoring_toggle_status_message()
        if toggle_status=="true":
            expected_status=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status==toggle_status_message
            expected_status_desc="This printer’s protection services are enabled and up to date. No action is required."
            # assert expected_status_desc ==self.solutions.get_security_monitoring_desc()
        else:
            self.solutions.click_security_monitoring_toggle_button()
            expected_status=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status==toggle_status_message
            expected_status_desc="Turn on security monitoring to help protect this printer."      
            # assert expected_status_desc ==self.solutions.get_security_monitoring_desc()
            #reverting back to original state
            self.solutions.click_security_monitoring_toggle_button()

    def test_07_verify_smart_security_mointoring_toggle_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521026
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521027
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()
        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        toggle_status_message=self.solutions.get_security_monitoring_toggle_status_message()
        if toggle_status=="true":
            self.solutions.click_security_monitoring_toggle_button()
            self.solutions.click_security_monitoring_popup_turnoff_button()
            expected_status=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status!=toggle_status_message
            #reverting back to original state
            self.solutions.click_security_monitoring_toggle_button()
            expected_status_message=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status_message==toggle_status_message
        else:
            self.solutions.click_security_monitoring_toggle_button()
            expected_status=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status!=toggle_status_message
            #reverting back to original state
            self.solutions.click_security_monitoring_toggle_button()
            expected_status_message=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status_message==toggle_status_message
  
    def test_08_verify_smart_security_mointoring_toggle_button_cancel_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30521039
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()
        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        toggle_status_message=self.solutions.get_security_monitoring_toggle_status_message()
        if toggle_status=="true":
            self.solutions.click_security_monitoring_toggle_button()
            self.solutions.click_security_monitoring_popup_cancel_button()
            expected_status=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status==toggle_status_message
        else:
            self.solutions.verify_security_monitoring_title()
            expected_status=self.solutions.get_security_monitoring_toggle_status_message()
            assert expected_status==toggle_status_message

    def test_09_verify_snmp_v1_v2_toggle_button(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519877
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519878
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()
        
        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v1_v2_label()
        self.solutions.click_snmp_v1_v2_expand_button()
        snmp_v1_v2_toggle_status = self.solutions.get_snmp_v1_v2_toggle_status()
        if snmp_v1_v2_toggle_status=="true":
            self.solutions.verify_snmp_v1_v2_toggle_turned_on_warning_label()
            self.solutions.verify_snmp_v1_v2_toggle_turned_on_warning_desc()
            self.solutions.click_snmp_v1_v2_expand_button()
        else:
            self.solutions.click_snmp_v1_v2_toggle_button()
            self.solutions.verify_snmp_v1_v2_toggle_turned_on_warning_label()
            self.solutions.verify_snmp_v1_v2_toggle_turned_on_warning_desc()
            # Reverting back to original state
            self.solutions.click_snmp_v1_v2_toggle_button()
            self.solutions.click_snmp_v1_v2_expand_button()

    def test_10_verify_snmp_v3_toggle_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519930
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519928
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v3_label()
        self.solutions.click_snmp_v3_expand_button()
        snmp_v3_toggle_status = self.solutions.get_snmp_v3_toggle_status()
        if snmp_v3_toggle_status=="true":
            self.solutions.verify_snmp_v3_toggle_turned_on_warning_label()
            self.solutions.verify_snmp_v3_toggle_turned_on_warning_desc()
            self.solutions.verify_snmp_v3_user_name_label()
            self.solutions.verify_snmp_v3_user_name_text_box()
            self.solutions.verify_snmp_v3_authentication_passphrase_label()
            self.solutions.verify_snmp_v3_authentication_passphrase_set_passphrase_text_box()
            self.solutions.verify_snmp_v3_authentication_passphrase_confirm_passphrase_text_box()
            self.solutions.verify_snmp_v3_privacy_passphrase_label()
            self.solutions.verify_snmp_v3_privacy_passphrase_set_passphrase_text_box()
            self.solutions.verify_snmp_v3_privacy_passphrase_confirm_passphrase_text_box()
            self.solutions.verify_snmp_v3_save_button_status("disabled")
            self.solutions.click_snmp_v3_expand_button()
        else:
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_toggle_turned_on_warning_desc()
            self.solutions.verify_snmp_v3_user_name_label()
            self.solutions.verify_snmp_v3_user_name_text_box()
            self.solutions.verify_snmp_v3_authentication_passphrase_label()
            self.solutions.verify_snmp_v3_authentication_passphrase_set_passphrase_text_box()
            self.solutions.verify_snmp_v3_authentication_passphrase_confirm_passphrase_text_box()
            self.solutions.verify_snmp_v3_privacy_passphrase_label()
            self.solutions.verify_snmp_v3_privacy_passphrase_set_passphrase_text_box()
            self.solutions.verify_snmp_v3_privacy_passphrase_confirm_passphrase_text_box()
            self.solutions.verify_snmp_v3_save_button_status("disabled")
            # Reverting back to original state
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.click_snmp_v3_expand_button()

    def test_11_validate_snmp_v3_user_name_field(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/30519931
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v3_label()
        self.solutions.click_snmp_v3_expand_button()
        snmp_v3_toggle_status = self.solutions.get_snmp_v3_toggle_status()
        if snmp_v3_toggle_status=="true":
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_single_text("a")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_valid_text("testing_user")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message_status(displayed=False)
        else:
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_single_text("a")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_valid_text("testing_user")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message_status(displayed=False)
            # Reverting back to original state
            self.solutions.click_snmp_v3_toggle_button()

    def test_12_validate_authentication_passphrase_field(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/30519932
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v3_label()
        self.solutions.click_snmp_v3_expand_button()
        snmp_v3_toggle_status = self.solutions.get_snmp_v3_toggle_status()
        if snmp_v3_toggle_status=="true":
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_single_text("123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text("e")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message_status(displayed=False)
        else:
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_single_text("123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text("e")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message_status(displayed=False)
            # Reverting back to original state
            self.solutions.click_snmp_v3_toggle_button()

    def test_13_validate_snmp_v3_privacy_passphrase_field(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30520979
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v3_label()
        self.solutions.click_snmp_v3_expand_button()
        snmp_v3_toggle_status = self.solutions.get_snmp_v3_toggle_status()
        if snmp_v3_toggle_status=="true":
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_single_text("text")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text("o")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message_status(displayed=False)
        else:
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_single_text("text")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text("o")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message_status(displayed=False)
            # Reverting back to original state
            self.solutions.click_snmp_v3_toggle_button()

    def test_14_validate_snmp_v3_save_button(self):
        # Functionality/test_08_01_smart_security.py::test_14_validate_snmp_v3_save_button  
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v3_label()
        self.solutions.click_snmp_v3_expand_button()
        snmp_v3_toggle_status = self.solutions.get_snmp_v3_toggle_status()
        if snmp_v3_toggle_status=="true":
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_single_text("a")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_single_text("123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text("e")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_single_text("text")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text("o")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message()
            self.solutions.click_snmp_v3_toggle_button()

            # verifying the textboxes with valid text
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_valid_text("testing_user")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message_status(displayed=False)  
            self.solutions.verify_snmp_v3_save_button_status("enabled")
        else:
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_single_text("a")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_single_text("123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text("e")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_single_text("text")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message()
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text("o")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message()
            self.solutions.click_snmp_v3_toggle_button()
            
            # verifying the textboxes with valid text
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_valid_text("testing_user")
            self.solutions.verify_snmp_v3_user_name_text_box_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_passing_valid_text("Test@123")
            self.solutions.verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message_status(displayed=False)
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_passing_valid_text("Test@1234")
            self.solutions.verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message_status(displayed=False)  
            self.solutions.verify_snmp_v3_save_button_status("enabled")
            # Reverting back to original state
            self.solutions.click_snmp_v3_toggle_button()
    
    def test_15_verify_smart_security_printer_details_screen_unsaved_changes_popup_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30521035
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/30521036
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/30521037
        
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen

        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify smart security detail screen
        self.solutions.verify_smart_security_detail_screen_printer_name()
        self.solutions.verify_snmp_v3_label()
        self.solutions.click_snmp_v3_expand_button()
        snmp_v3_toggle_status = self.solutions.get_snmp_v3_toggle_status()
        if snmp_v3_toggle_status=="true":
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_single_text("a")
            self.home.click_printers_menu_btn()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_popup_label()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_popup_description()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_popup_cancel_button()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_leave_button()
            self.solutions.click_smart_security_printer_details_screen_unsaved_changes_leave_button()
        else:
            self.solutions.click_snmp_v3_toggle_button()
            self.solutions.verify_snmp_v3_user_name_text_box_with_passing_single_text("a")
            self.home.click_printers_menu_btn()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_popup_label()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_popup_description()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_popup_cancel_button()
            self.solutions.verify_smart_security_printer_details_screen_unsaved_changes_leave_button()
            self.solutions.click_smart_security_printer_details_screen_unsaved_changes_leave_button()            