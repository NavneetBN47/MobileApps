import pytest
from datetime import datetime as Datetime
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_01_E2e_Functionality(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.account = cls.fc.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpid = cls.fc.fd[FLOW_NAMES.HPID]
        cls.camera_scan = cls.fc.fd[FLOW_NAMES.CAMERA_SCAN] 
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_the_shortcuts_feature_when_the_user_is_not_signed_in_created_the_account(self):
        """
        Description: C52648707  
            Install and launch the app.
            Add the target device to the root view.
            Navigate to device details screen.
            Click on the Shortcuts tile.
            Verify the behavior.
        Expected Result:
            User should not be able to access the shortcuts tile.
            Notification screen should be displayed as below screen.      
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.account.verify_tiles_not_signed_in_page()

    def test_02_verify_the_shortcuts_feature_after_user_creating_an_account(self):
        """
        Description: C52649187
            Click on the Shortcuts tile.
            Create an account.
            Click on Add new shortcuts.
            Click on the Create your own Shortcut.
            Enable the Destinations (Print, Email, and Save) toggle bar.
            Click on the Continue button.
            Navigate to 'Add print' screen and select any print settings for this shortcut.
            Then click on the continue button.
            Navigate to the "Add Email" screen, enter the required details, and click the "Continue" button.
            Navigate to the "Add Save" screen and select the account (sign in if necessary).
            Navigate to cloud destination.
            Save the folder and click on Add to shortcut button in 'Add save' screen.
            Observe the behavior.
            Then click on the 'Save' shortcut button and observe the behavior.
            Then click on the 'Done' button.
            Observe the behavior.
        Expected Result:
            The user should be navigated to the 'Shortcut setting' screen and the shortcut name should be automatically set to 'Print, Email, and Save'.
            After step 14: The shortcut should be created and saved successfully as shown in the below screen.
            After step 16: User should be navigated to the 'Shortcuts' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.account.click_create_account_btn()  
        self.hpid.create_account()
        self.shortcuts.verify_shortcuts_screen()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()    
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)   
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_done_btn()
        assert self.hpx_shortcuts.verify_shortcut_present_in_list(shortcut_name), f"The created shortcut '{shortcut_name}' should be present in the shortcuts list"

    def test_03_verify_the_shortcuts_feature_with_an_existing_account(self):
        """
        Description: C52689192
            Click on the Shortcuts tile.
            Click on Add new shortcut.
            Click on the Create your own Shortcut.
            Enable the Destinations (Print, Email, and Save) toggle bar.
            Navigate to 'Add print' screen and select any print settings for this shortcut.
            Click on 'Add to Shortcut' button.
            Navigate to the "Add Email" screen, enter the required details, and click the 'Add to Shortcut' button.
            Navigate to the 'Add Save' screen and select the account (sign in if necessary).
            Navigate to cloud destination.
            Save the folder and observe the screen.
            In 'Shortcut settings' screen enter the required details and select any settings then click on the 'Save' shortcut button.
            Then click on 'Run this shortcut' button.
            Select the source from camera/printer scan/Files and photos.
            Select the created shortcut and click on the 'Print' button.
            Observe the behavior.           
        Expected Result:
            After step 10: The user should be navigated to the 'Shortcut settings' screen.
            After step 11: The 'Print, Email and Save' shortcuts should be created and saved successfully as shown in the below screen.
            After step 15: The selected file should be printed successfully through the created shortcut, sent to the specified email recipient, and saved to the designated destination as set in the shortcut.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn() 
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.account.click_sign_in_btn()
        self.hpid.login()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()    
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)   
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        assert self.camera_scan.verify_select_scan_source_screen(), "scan source screen should be displayed after clicking 'Run this Shortcut' button"
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"

    def test_04_verify_the_shortcuts_feature_when_a_user_creates_a_shortcut_with_the_print_destination_only(self):
        """
        Description: C52692759
            Click on the Shortcuts tile.
            Click on the Add new Shortcut in Shortcuts screen.
            Then Click on the Create your own shortcut.v
            In Add Shortcut screen enable only the 'Print' destination and observe the screen.
            In the Add Print screen, choose any settings, then click the 'Add to Shortcut' button. After that, click the 'Continue' button and observe the screen.
            In shortcut settings screen select any settings and click on the Save shortcut button.
            Then click on the 'Run this shortcut' button.
            Select any source from camera Scan/ printer scan/ Files and photos.
            Select the shortcut you created in Preview screen.
            Click on the 'Print' icon beside the image.
            Observe the behavior.
            Click on the 'Done' button and observe the behavior.
        Expected Result:
            After step 4: The user should be navigated to the 'Add print' screen.
            After step 5: The user should be navigated to the 'Shortcut setting' screen.
            Note: If the user selects 'Print' destination the 'File type' should not be displayed in the shortcut settings screen.
            After step 6: The shortcut should be saved successfully.
            After step 11: The user should be able to print successfully with the specified settings and 'Your shortcut is running' pop-up window should be displayed as below screen.
            After step 12: The user should be navigated to root view.  
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn() 
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.verify_shortcut_settings_screen_title() 
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"
  
    def test_05_verify_the_shortcuts_feature_when_a_user_creates_a_shortcut_with_the_email_destination_only(self):
        """
        Description: C52694852
            Click on the Shortcuts tile.
            Click on the Add new Shortcut.
            Then Click on the Create your own shortcut.
            In Add Shortcut screen enable only the 'Email' destination and observe the screen.
            In Add email screen enter the required details and click on the 'Add to shortcuts' button then click on the continue button.
            In shortcut settings screen select any settings and click on save shortcut button.
            Then click on the Run this Shortcut button.
            Select the source from camera/printer scan/Files and photos.
            Select the shortcut you created in Preview screen.
            Observe the screen.
            Click on the 'Done' button.
            Then navigate to 'Your shortcut is running' screen.
            Click on the 'View status' button and observe the screen.
            Make sure that the user is in 'Your shortcut is running' screen.
            Then click on the 'Shortcuts' button.
        Expected Result:
            After step 4: The user should be navigated to the 'Add Email' screen.
            After step 5: The user should be navigated to the 'Shortcut settings' screen. (Note: The file type option should be displayed for email shortcut)
            After step 6: The Email shortcut should be saved successfully as shown in the below screen
        """ 
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn() 
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.verify_shortcut_settings_screen_title() 
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.hpx_shortcuts.verify_your_shortcut_is_running_title()
        self.hpx_shortcuts.click_view_status_btn()
        self.driver.back()
        self.hpx_shortcuts.click_shortcuts_btn()

    def test_06_verify_the_shortcuts_feature_when_a_user_creates_a_shortcut_with_the_save_destination_only(self):
        """
        Description: C52697934
            Click on the Shortcuts tile.
            Click on the Add new Shortcut in Shortcuts screen.
            Then Click on the Create your own shortcut.
            In Add Shortcut screen enable only the 'Save' destination and observe the screen.
            Navigate to the Add save screen and select the any account (Sign in if we needed).
            Navigate to cloud destination screen.
            Click on save to this folder and click on the 'Add to shortcuts' button.
            Click the 'Continue' button and observe the screen.
            In shortcut settings screen select any settings and click on the Save shortcut button.
            Then click on the 'Run this Shortcut' button.
            Select the source from camera/printer scan/Files and photos.
            Select the shortcut you created in Preview screen.
            Observe the screen.
            Click on the 'Done' button.
            Then navigate to 'Your shortcut is running' screen.
            Click on the 'View status' button and observe the screen.
            Make sure that the user is in 'Your shortcut is running' screen.
            Then click on the 'Shortcuts' button.
        Expected Result:
            After step 4: The user should be navigated to the 'Add Save' screen.
            After step 8: The user should be navigated to the 'Shortcut settings' screen. (Note: The file type option should be displayed for Save shortcut)
            After step 9: The file should be saved successfully as shown in the below screen, in the specified destination and folder as set in the shortcut.
            After step 13: 'Your shortcut is running' pop-up window should be displayed as below screen, and the file should be successfully saved in the destination and folder as specified in the shortcut.
            After step 14: User should be navigated to the root view.
            After step 16: The user should receive a notification after clicking the 'View status' button.
            After step 18: The user should be redirected to the root view.
       """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.verify_shortcut_settings_screen_title() 
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.hpx_shortcuts.verify_your_shortcut_is_running_title()
        self.hpx_shortcuts.click_view_status_btn()
        self.driver.back()
        self.hpx_shortcuts.click_shortcuts_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"

    def test_07_verify_the_shortcuts_feature_when_a_user_deletes_the_existing_shortcuts_for_print_email_and_save_destinations(self):
        """
        Description: C52702044
            Click on the Shortcuts tile.
            Navigate to the Shortcuts screen and observe the screen.
            Click on the 'Edit' link on the shortcuts screen.
            Then click on the 'Delete' icon in 'Print, Email and Save' shortcuts.
            Observe the screen.
            Click on the 'Cancel' button and observe the screen.
            Repeat step 2,3 and 4.
            Click on 'Delete' button in the dialog.
            Observe the screen.
        Expected Result:
            After step 2: The Existing shortcuts for the 'Print, Email and Save' should be displayed on the shortcuts screen.
            After step 5: The 'Delete Shortcut' pop up window should be displayed as below screen.
            After step 6: User should be redirected to the 'Add shortcuts' screen.
            After step 9: User should be redirected to the 'Shortcuts' screen.
       """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to delete the shortcut since element is not available in the page source
        self.hpx_shortcuts.click_delete_shortcut_btn_delete_btn()
        self.hpx_shortcuts.verify_delete_shortcut_confirmation_msg_title()
        self.hpx_shortcuts.verify_shortcuts_screen_title()

    def test_08_verify_the_shortcuts_feature_when_a_user_cancels_the_creation_of_the_shortcuts(self):
        """
        Description: C52706692
            Click on the Shortcuts tile.
            Click on the Add new Shortcut in Shortcuts screen.
            Then Click on the Create your own shortcut.
            Enable the Destinations (Print, Email, and Save) toggle bar.
            Navigate to 'Add print' screen and select any print settings for this shortcut and click on the Add to shortcuts button.
            Navigate to the "Add Email" screen, enter the required details, and click the Add to shortcuts button.
            Navigate to the "Add Save" screen and select the account (sign in if necessary).
            Navigate to cloud destination and click on this folder.
            Click on Add to shortcuts button.
            Then click on the '<-' previous page button in 'Add shortcuts' screen and observe the screen.
            Click on the 'Go back' button and observe the screen.
            Click on the 'Yes, cancel' button and observe the screen.
        Expected Result:
            After step 10: User should be navigated to the 'Cancel this shortcut?' pop up window as shown in below screen.
            After step 11: The user should be redirected to the 'Add Shortcut' screen and the created shortcuts should not be canceled.
            After step 12: The user should be redirected to the 'Shortcuts' screen and the created shortcuts should be canceled.
       """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        self.hpx_shortcuts.verify_shortcuts_screen_title()

    def test_09_verify_the_shortcuts_feature_when_the_user_performs_add_destination_remove_edit_name_actions(self):
        """
        Description: C52773445
            Click on the Shortcuts tile.
            Navigate to Add shortcut screen.
            Add Print, Email shortcuts.
            In Add save destination sign in for any of the account (e.g., Google Drive, One Drive etc.)
            Observe the 'Add Save' screen.
            Click on the 3 dots icon and observe the screen.
            Select 'Add destination' option from the pop-up window.
            Observe the screen.
            Then click on the back button/previous page and observe the screen.
            Click on the 3 dots icon and select 'Edit name' option.
            Observe the dialog.
            Edit the account name and click on the 'Cancel' button.
            Observe the account name in add save screen under 'Accounts' section.
            Repeat step 10, edit the account name and click on the 'Save' button.
            Observe the screen.
            Click on 3 dots icon and select 'Remove' option and observe the screen.
            Click on the 'OK' button and observe the behavior.
        Expected Result:
            After step 5: The 'Google Drive' account should be added under 'Accounts' section as displayed on the below screen.
            After step 13: The 'Account name' should remain unchanged, previously created account name should be displayed.
            After step 15: The 'Account name' should be updated and reflected in the respective account after the change is made.
            After step 16: "Remove HP access" pop up window should be displayed as shown in the below screen.
            After step 17: "Remove HP access" pop up window should be dismissed, and user should not have the access for the removed account.
       """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_three_dot_in_account()
        self.hpx_shortcuts.click_remove_btn_in_account()
        assert self.hpx_shortcuts.verify_remove_hp_access_confirmation_msg() == "Remove HP access", "Expected text 'Remove HP access' not found"

    def test_10_verify_the_shortcuts_feature_when_the_user_adds_all_three_destinations_print_email_and_save_and_performs_shortcut_settings_actions(self):
        """
        Description: C52777057
            Click on the Shortcuts tile.
            Navigate to Add shortcuts screen.
            Add all three destinations 'Print, Email, and Save' shortcuts then click on the continue button.
            Observe the screen.
            In Shortcut settings screen enter the required details and select the desired settings then click on the 'Save shortcut' button.
            Then click on 'Run this shortcut' button.
            Select the source from camera/printer scan/Files and photos.
            Select the created shortcut and click on the 'Print' icon beside the image.
            Observe the behavior.
        Expected Result:
            After step 4: The 'shortcut setting' screen should be displayed as shown in the below screen.
            Note: The 'File type' option should be displayed on the 'Shortcut setting' screen when the user enables 'Email/Save' destination,
            After step 9: The user should be able to print successfully using the specified settings.
       """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()    
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)   
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        assert self.camera_scan.verify_select_scan_source_screen(), "scan source screen should be displayed after clicking 'Run this Shortcut' button"
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"

    def test_11_verify_the_shortcuts_feature_when_the_user_adds_only_Print_destination_and_performs_shortcut_settings_action(self):
        """
        Description: C52777612
            Click on the Shortcuts tile.
            Navigate to Add shortcuts screen.
            Add only the 'Print' shortcut and click on the continue button.
            Observe the screen.
            In Shortcut settings screen enter the required details and select settings then click on the Save shortcut button and observe the screen.
            Then click on 'Run this shortcut' button.
            Select the source from camera/printer scan/Files and photos.
            Select the created shortcut and click on the 'Print' button.
            Observe the behavior.
        Expected Result:
            After step 4: The 'shortcut setting' screen should be displayed as shown in the below screen.
            Note: The 'File type' option should not be displayed in the 'Shortcut settings' screen if user selects only 'Print' destination.
            After step 5: The shortcut should be saved successfully and 'Shortcut saved' pop-up window should be displayed as below screen.
            After step 9: The user should be able to print successfully without any error.
       """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn() 
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.verify_shortcut_settings_screen_title() 
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"







    