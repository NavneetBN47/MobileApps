import pytest
import logging
from SAF.misc import saf_misc
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

class Test_02_SMB_Home(object):

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
        self.account = self.fc.fd["account"]
        self.users = self.fc.fd["users"]
        self.printers = self.fc.fd["printers"]
        self.solutions = self.fc.fd["solutions"]
        self.accounts = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.accounts["email"]
        self.hpid_password = self.accounts["password"]
        self.hpid_tenantID = self.accounts["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder()        
    
    def test_01_verify_side_menu(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30515978
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("home_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "_screenshhomeot/{}_home_localization.png".format(self.locale))

        self.home.verify_hpinstantink_menu_btn()
        self.home.verify_printers_menu_btn()
        self.home.verify_users_menu_btn()
        self.home.verify_solutions_menu_btn()
        self.home.verify_sustainability_menu_btn()
        self.home.verify_account_menu_btn()
        self.home.verify_help_center_menu()

    def test_02_verify_user_icon_design(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30515979
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.click_account_profile_tab()
        # self.account.verify_account_profile_screen_title()
        user_first_name=self.account.get_first_name()
        user_last_name=self.account.get_last_name()
        expected_user_icon_text = user_first_name[0]+user_last_name[0]
        actual_user_icon_text = self.home.get_user_icon_initial()
        assert actual_user_icon_text == expected_user_icon_text.upper()         

    def test_03_verify_status_widget_card_UI(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516020
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_status_widget_title()

        #verify printer status label text like total printers, connected, not connected
        self.home.verify_status_widget_printer_status_header()
        self.home.verify_status_widget_connected_printer()
        self.home.verify_status_widget_not_connected_printer()

        #verify users status label text like total users, active and pending
        self.home.verify_status_widget_users_status_header()
        self.home.verify_status_widget_active_users()
        self.home.verify_status_widget_pending_users()
        self.home.verify_status_widget_expired_users()

    def test_04_verify_notification_bell_icon(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519024
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_notification_bell_icon()

    def test_05_logout(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/41381082
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.logout()
        self.login.verify_smb_login_label()  

    def test_06_verify_hp_smart_pro_widget_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518979
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518981
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518982
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        if self.home.verify_smart_pro_widget() is False:
            logging.info("HP Smart Pro entitlenment is not active")
        else:
            self.home.verify_hp_smart_pro_widget_title()
            expected_desc="HP Smart Pro gives users access to additional features in the HP Smart App"
            sleep(3)
            assert expected_desc==self.home.get_smart_pro_widget_description()
            self.home.verify_smart_pro_discover_link()
    
    def test_07_verify_hp_plus_widget_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518987
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518992
        
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_hp_plus_widget_title()

        # ********Smart Security Section***********
        self.home.verify_smart_security_label()
        self.home.verify_hp_plus_smart_security_secured_text()
        self.home.verify_hp_plus_smart_security_needs_attention_text()
        self.home.verify_hp_plus_smart_security_unmonitored_text()
        self.home.verify_hp_plus_smart_security_needs_no_data_available_text()

        # ********Print Anywhere Section***********
        self.home.verify_print_anywhere_label()
        self.home.verify_hp_plus_print_anywhere_enabled_text()
        self.home.verify_hp_plus_print_anywhere_disabled_text()

        # ********Forest First***********
        self.home.verify_forest_first_label()
        expected_desc ="Every page you print is directly offset by a new tree being planted, as HP invests in forest restoration around the world. Your printing contributes to many acres of forests being restored around the world."
        assert expected_desc == self.home.get_forest_first_description()

    def test_08_verify_smart_security_printer_count(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518989
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)

        #get printer count from solutions page
        self.home.click_solutions_menu_btn()
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        sleep(3)
        solutions_smart_security_page_printer_count = self.solutions.get_printers_count()

        #get Hp+ widget smart security Printer count from home page
        self.home.click_home_menu_btn()
        self.home.verify_smart_security_label()
        sleep(3)
        smart_security_printer_total_count = self.home.get_hp_plus_printer_widget_smart_security_printer_total_count()
        assert smart_security_printer_total_count == solutions_smart_security_page_printer_count

    def test_09_verify_print_anywhere_printer_count(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518991
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)

        #get printer count from solutions page
        self.home.click_solutions_menu_btn()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.verify_print_anywhere_page_table_loads()
        solutions_print_anywhere_page_printer_count = self.solutions.get_printers_count()

        #get printer widget total count from home page
        self.home.click_home_menu_btn()
        print_anywhere_printer_total_count = self.home.get_hp_plus_printer_widget_print_anywhere_printer_total_count()
        assert print_anywhere_printer_total_count == solutions_print_anywhere_page_printer_count

    def test_10_verify_forest_first_learn_more_link(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518995
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_forest_first_label()
        self.home.click_on_learn_more_hyperlink()
        self.home.verify_learn_more_sustainability_label()

    def test_11_verify_welcome_text(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30515973
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        actual_welcome_text = self.home.get_welcome_text()
        self.home.click_account_menu_btn()
        self.home.click_account_profile_button()
        first_name = self.home.get_first_name_in_account_profile()
        expected_welcome_text = "Welcome, " + first_name +"!"
        assert expected_welcome_text == actual_welcome_text
         
    def test_12_verify_organization_name(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518883
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.home.click_account_profile_button()
        self.home.click_organization_tab()
        org_id = self.home.get_last_four_digit_of_uid()
        org_name = self.home.get_organization_name_in_account_profile()
        length = len(org_name)
        if length >11:
            actual_org_name = org_name[0:6]+"..."+org_name[length-5:]+" (..."+org_id+")"
        else:
            actual_org_name = org_name+" (..."+org_id+")"
        self.home.click_avatar_button()
        assert actual_org_name == self.home.get_organization_id()

    def test_13_verify_notification_bell_icon(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518885
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_notification_bell_icon()
        self.home.click_notification_bell_icon()
        self.home.verify_all_notification_text()

    def test_14_verify_printer_usage_widget_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521278
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521279
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_printer_usage_widget_label()
        self.home.verify_printer_usage_widget_help_icon()

        #verify usage widget - Printed usage status of printer
        self.home.verify_usage_widget_toggle_print_button()
        self.home.verify_printer_usage_widget_view_details_button()
        self.home.verify_printer_usage_widget_total_pages_printed_label()
        self.home.verify_printer_usage_widget_total_pages_printed_count()

        self.home.verify_printer_usage_data_select_previous_year_button()
        self.home.verify_printer_usage_data_select_next_year_button()
        self.home.verify_printer_usage_data_select_year_value()

        #Verifying y-axis of Print Usage Widget chart
        self.home.verify_printed_usage_data_highcharts_axis_printed_pages_title()

        #Verifying x-axis of Print Usage Widget chart
        self.home.verify_printed_usage_data_highcharts_black_and_white_button()
        self.home.verify_printed_usage_data_highcharts_color_button()
        self.home.verify_printed_usage_data_highcharts_average_use_button()
       
        expected_xaxis_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        assert expected_xaxis_labels == self.home.get_printed_usage_data_highcharts_xaxis_labels_options()

        #Verify Scan Usage toggle button 
        if self.home.verify_usage_widget_toggle_scan_button_is_displayed() is True:
            self.home.verify_usage_widget_toggle_scan_button()
            self.home.click_usage_widget_toggle_scan_button()

            #verify usage widget - Scanned usage status of printer
            self.home.verify_printer_usage_widget_total_pages_scanned_label()
            self.home.verify_printer_usage_widget_total_pages_scanned_count()

            self.home.verify_printer_usage_data_select_previous_year_button()
            self.home.verify_printer_usage_data_select_next_year_button()
            self.home.verify_printer_usage_data_select_year_value()

            #Verifying y-axis of Scan Usage Widget chart
            self.home.verify_scanned_usage_data_highcharts_axis_scanned_pages_title()

            #Verifying x-axis of Scan Usage Widget chart
            self.home.verify_scanned_usage_data_highcharts_scans_button()
            self.home.verify_scanned_usage_data_highcharts_average_use_button()
        
            expected_xaxis_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
            assert expected_xaxis_labels == self.home.get_scanned_usage_data_highcharts_xaxis_labels_options()

    def test_15_verify_notification_bell_icon(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518997
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519007

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_notification_bell_icon()
        self.home.verify_notification_popup()
        all_notifications_text = self.home.get_notification_popup_text() 
        if all_notifications_text == "All Notifications":
            self.home.verify_notification_popup_no_new_notification_text()
        else:
            assert self.home.get_notifications_count() == self.home.get_notifications_count_from_notification_list()

    def test_16_verify_notification_popup_ellipsis_dropdown_options(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518998
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30518999
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/30519005      

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_notification_bell_icon()
        all_notifications_text = self.home.get_notification_popup_text() 
        if all_notifications_text == "All Notifications":
            self.home.verify_notification_popup_no_new_notification_text()
        else:
            self.home.verify_notification_popup_ellipsis_button()
            self.home.click_notification_popup_ellipsis_button()
            expected_notification_popup_ellipsis_dropdown_options=["Mark all as read","Remove all"]
            actual_notification_popup_ellipsis_dropdown_options=self.home.get_notification_popup_ellipsis_dropdown_options()
            assert expected_notification_popup_ellipsis_dropdown_options==actual_notification_popup_ellipsis_dropdown_options

    def test_17_verify_bell_icon_notification_message(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/edit/30519000
        #https://hp-testrail.external.hp.com/index.php?/cases/edit/30519001
        #https://hp-testrail.external.hp.com/index.php?/cases/edit/30519003

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_notification_bell_icon()
        all_notifications_text = self.home.get_notification_popup_text()
        if all_notifications_text == "All Notifications":
            self.home.verify_notification_popup_no_new_notification_text()
        else:
            self.home.verify_bell_notification_message_icon()
            self.home.verify_new_notification_printer_detail_and_location()
            self.home.verify_new_notification_arrived_date_and_time()

    def test_18_verify_multiple_organization_count(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/31119143
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_avatar_button()
        self.home.verify_organization_count()
        self.home.change_organization_name()

    def test_19_verify_printer_details_in_smart_notification_widget(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518889
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518890
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        notification_count=self.home.get_smart_notification_widget_notification_count()
        #validate smart notification widget is empty or to validate the printer details
        if notification_count == 0:
                assert self.home.verify_smart_notification_widget_empty_text() == True
        else:
            self.home.verify_smart_notification_printer_detail_and_location()
            self.home.verify_smart_notification_generated_date_and_time()
        
    def test_20_dismiss_a_notification_in_smart_notification_widget(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518891
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        notification_count=self.home.get_smart_notification_widget_notification_count()
        #validate smart notification widget is empty or to dismiss the notification
        if notification_count == 0:
                assert self.home.verify_smart_notification_widget_empty_text() == True
        else:
            self.home.smart_notification_mouse_hover()
            self.home.click_smart_notification_action_button()
            self.home.click_smart_notification_dismiss_button()
            #Verify notification count got reduced after removing a notification
            assert (notification_count -1 ) == self.home.get_smart_notification_widget_notification_count()
        
    def test_21_verify_total_devices_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516023
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_status_total_printer_btn()
        self.home.click_status_total_printer_btn()
        self.printers.verify_printers_page_title()

    def test_22_verify_total_users_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516024
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_status_total_users_btn()
        self.home.click_status_total_users_btn()
        self.users.verify_users_page_title()

    def test_23_verify_read_status_for_single_notification(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)        
        self.home.click_home_menu_btn()
        self.home.click_notification_bell_icon()
        all_notifications_text = self.home.get_notification_popup_text() 
        #verifying the bell notification window has any notification or empty
        if all_notifications_text == "All Notifications":
            self.home.verify_notification_popup_no_new_notification_text()
        else:
            #verifying the bell notification window for new notification
            self.home.verify_notification_popup_ellipsis_button()
            self.home.click_notification_popup_ellipsis_button()

            #verify whether any unread/new notifications are present 
            read_status = self.home.get_mark_all_notification_read_option_status()
            self.home.click_notification_popup_ellipsis_button()
            
            #verify unread/new notification message
            if read_status == True: 
                         
                self.home.bell_notification_mouse_hover()
                self.home.click_single_notification_action_btn()
                #verify mark as read option enabled for first notification message
                if self.home.get_mark_read_option_status_for_single_message() == True:
                    #marking the unread notification as "read"
                    self.home.click_mark_read_option_for_single_notification()

                    #verify mark as read option disabled for first notification message
                    self.home.bell_notification_mouse_hover()
                    self.home.click_single_notification_action_btn()
                    assert self.home.get_mark_read_option_status_for_single_message() == False
                    
                # #remove first notification message 
                # self.home.bell_notification_mouse_hover()
                # self.home.click_single_notification_action_btn()
                # self.home.click_remove_option_for_single_notification()
            else: 
                logging.info("All notifications are read, no new notifications")
        
    def test_24_verify_remove_all_button_in_bell_notification(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        
        #verifying the bell notification window for new notification
        self.home.click_home_menu_btn()
        self.home.click_notification_bell_icon()
        all_notifications_text = self.home.get_notification_popup_text() 
        #verifying the bell notification window has any notification or empty
        if all_notifications_text == "All Notifications":
            self.home.verify_notification_popup_no_new_notification_text()
        else:
            #verifying the bell notification window for new notification
            self.home.verify_notification_popup_ellipsis_button()
            self.home.click_notification_popup_ellipsis_button()

            #verify whether any unread/new notifications are present 
            read_status = self.home.get_mark_all_notification_read_option_status()
            
            if read_status == True:          
                #marking all the unread notification as "read"
                self.home.click_mark_all_read_option_status()
            
                #verify mark all as read option disabled 
                self.home.click_notification_popup_ellipsis_button()
                self.home.verify_mark_all_read_option_status("disabled")

            #removing all the notification from window
            self.home.click_remove_all_notification_button()
            self.home.verify_notification_popup_no_new_notification_text()
    
    def test_25_verify_footer_component(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()
        self.home.verify_footer_copyright_information()
        self.home.verify_footer_component_hp_com()
        self.home.verify_footer_component_hp_support()
        self.home.verify_footer_component_hp_smart_admin_terms_of_use()
        self.home.verify_footer_component_hp_privacy()
        self.home.verify_footer_component_personal_data_rights_notice()

    def test_26_verify_footer_component_hp_com(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()

        self.home.click_footer_component_hp_com()
        self.home.verify_new_tab_opened()
        self.home.verify_hp_official_site_url()

    def test_27_verify_footer_component_hp_support(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()
        self.home.click_footer_component_hp_support()
        self.home.verify_new_tab_opened()
        self.home.verify_hp_official_support_url()

    def test_28_verify_footer_component_hp_smart_admin_terms_of_use(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()
        self.home.click_footer_component_hp_smart_admin_terms_of_use()
        self.home.verify_new_tab_opened()
        self.home.verify_hp_smart_admin_terms_of_use_url()

    def test_29_verify_footer_component_hp_privacy(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()
        self.home.click_footer_component_hp_privacy()
        self.home.verify_new_tab_opened()
        self.home.verify_hp_privacy_central_url()

    def test_30_verify_footer_component_personal_data_rights_notice(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()
        self.home.click_footer_component_personal_data_rights_notice()
        self.home.verify_new_tab_opened()
        self.home.verify_personal_data_rights_notice_url()