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
        self.printers = self.fc.fd["printers"]
        self.users = self.fc.fd["users"]
        self.account = self.fc.fd["account"]
        self.accounts = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.accounts["email"]
        self.hpid_password = self.accounts["password"]
        self.hpid_tenantID = self.accounts["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder() 

    def test_01_verify_emailid_on_user_icon(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519021
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("home_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "_screenshhomeot/{}_home_localization.png".format(self.locale))

        self.home.verify_home_dashboard_welcome_text()
        self.home.verify_user_icon_top_right_profile()
        self.home.click_user_icon_top_right()
        self.home.verify_emailid_user_icon()
        email_id=self.home.get_emailid_user_icon()
        assert email_id == self.hpid_username
      
    def test_02_verify_status_widget_printer_information(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516021
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516022
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_status_widget_title()  
        
        #get printer count from status widget 
        status_widget_total_printers_count = self.home.get_status_widget_total_printer_count()
        status_widget_connected_printers_count = self.home.get_status_widget_connected_printer_count()
        status_widget_not_connected_printers_count = self.home.get_status_widget_not_connected_printer_count()

        #get printer count from printers page
        self.home.click_status_total_printer_btn()
        self.printers.click_printer_table_view_button()
        printer_page_printer_count = self.printers.get_printers()

        #verify status widget printer count 
        assert status_widget_total_printers_count == printer_page_printer_count["total_count"]
        assert status_widget_connected_printers_count == printer_page_printer_count["connected"]
        assert status_widget_not_connected_printers_count == printer_page_printer_count["notconnected"]

    def test_03_verify_status_widget_users_information(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516021
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516022
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_home_menu_btn()
        self.home.verify_status_widget_title()  

        #get users count from status widget
        status_widget_total_users_count = self.home.get_status_widget_total_user_count()
        status_widget_active_users_count = self.home.get_status_widget_active_user_count()
        status_widget_pending_users_count = self.home.get_status_widget_pending_user_count()
        status_widget_expired_users_count = self.home.get_status_widget_expired_user_count()

        #get users count from users page
        self.home.click_status_total_users_btn()
        sleep(10)
        users_page_user_count = self.users.get_users()

        #verify status widget users count
        assert status_widget_total_users_count == users_page_user_count["total_count"]
        assert status_widget_active_users_count == users_page_user_count["active"]
        assert status_widget_pending_users_count == users_page_user_count["pending"]
        assert status_widget_expired_users_count == users_page_user_count["expired"] 

    # # Need to modify testcase as per new design change 
    # def test_04_verify_printer_usage_widget_dropdown_functionalities(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521280
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521281
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521282
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521283
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521284
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521285
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521286
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521287
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/32151684
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/32151681
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        
    #     # Scan Dropdown screen UI
    #     self.home.click_printer_usage_select_dropdown()
    #     self.home.usage_select_dropdown_option("scan")
    #     self.home.verify_printer_usage_pages_scanned_text()
    #     self.home.verify_printer_usage_scanned_pages_text()

    #     # Fax Dropdown screen UI
    #     self.home.click_printer_usage_select_dropdown()
    #     self.home.usage_select_dropdown_option("fax")
    #     self.home.verify_printer_usage_fax_pages_text()
    #     self.home.verify_printer_usage_fax_pages_sent_text()
    #     self.home.verify_printer_usage_fax_pages_received_text()

    #     # Print Dropdown screen UI
    #     self.home.click_printer_usage_select_dropdown()
    #     self.home.usage_select_dropdown_option("print")
    #     # self.home.verify_printer_usage_description()
    #     printer_usage_color_label = "Color"
    #     assert printer_usage_color_label == self.home.get_printer_usage_widget_color_label()
    #     self.home.get_printer_usage_widget_black_white_label()
    #     self.home.verify_printer_usage_widget_toggle_color_button_default()
    #     self.home.verify_printer_usage_widget_total_print_count()
    #     self.home.verify_printer_usage_widget_printed_pages_text()
    #     self.home.click_printer_usage_print_sides_button()
    #     self.home.get_printer_usage_widget_single_sided_label()
    #     self.home.get_printer_usage_widget_double_sided_label()
    #     self.home.verify_printer_usage_widget_total_printed_pages_count()

    def test_05_verify_printer_widget_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516009
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516012
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516013
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516014
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519052
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518899
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516006

        #This test cases verify Printer details on widget
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_printer_widget_section()
        self.home.verify_printer_widget_title()

        if self.home.verify_printer_widget_printer_is_displayed() is False:
            expected_value = "No printers available"
            assert expected_value ==  self.home.get_printer_widget_empty_text() 
        else:
            self.home.click_printer_widget_view_all_link()
            self.printers.verify_printers_page_title()               

    def test_06_verify_printer_widget_total_count(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516010
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516004
        
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)

        #get printer count from printers page
        self.home.click_printers_menu_btn()
        self.printers.click_printer_table_view_button()
        printer_page_printer_count = self.printers.get_printers_count()

        #get printer widget total count from home page
        self.home.click_home_menu_btn()
        self.home.verify_printer_widget_section()
        list_of_printers_in_printer_widget=self.home.get_printer_widget_no_of_printers_count()
        assert printer_page_printer_count == list_of_printers_in_printer_widget  

    def test_07_verify_smart_notification_widget_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30515992
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30515993
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30515998
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_smart_notification_widget_title()
        expected_title="Smart Notifications"
        assert expected_title == self.home.get_smart_notification_widget_title()
        notification_count=self.home.get_smart_notification_widget_notification_count()

        #validate smart notification widget is empty or to validate the notifications
        if notification_count == 0:
                assert self.home.verify_smart_notification_widget_empty_text() == True
        else:
            list_of_notification_in_notification_widget=self.home.get_smart_notification_widget_list_of_notifications()
            assert notification_count == list_of_notification_in_notification_widget
    
    def test_08_verify_hp_smart_pro_widget_status_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30518984
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        if self.home.verify_smart_pro_widget() is False:
            logging.info("HP Smart Pro entitlenment is not active")
        else:
            self.home.verify_smart_pro_widget()
            self.home.click_smart_pro_discover_link()
            self.home.verify_hp_smart_pro_page_title()

    # #Need to modify testcase as per new design change 
    # def test_09_validate_printer_usage_widget_print_color_toggle_color_pages_count_with_total_count(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521280
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521281
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521282
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
    #     sleep(20)
    #     total_pages_of_color_and_black = self.home.add_both_color_black_and_white()
    #     total_pages_of_usage_print_count = self.home.get_total_pages_in_usage_print_color_toggle()
    #     assert total_pages_of_color_and_black == total_pages_of_usage_print_count

    # def test_10_validate_printer_usage_widget_print_sides_toggle_printed_sides_count_with_total_count(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521285
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521286
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30521287
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
    #     self.home.click_printer_usage_print_sides_button()
    #     total_pages_of_single_sided_count = self.home.add_both_single_and_double_sided_pages()
    #     total_pages_of_double_sided_count = self.home.get_total_pages_in_usage_print_sides_toggle()
    #     assert total_pages_of_single_sided_count == total_pages_of_double_sided_count