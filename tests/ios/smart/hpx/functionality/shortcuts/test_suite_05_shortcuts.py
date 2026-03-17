import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
pytest.app_info = "SMART"

class Test_Suite_05_Shortcuts(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        """Class-level setup for Shortcuts test suite 05."""
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.hpxshortcuts = cls.fc.fd["hpx_shortcuts"]

    def test_01_verify_save_destination_in_add_shortcut_screen(self):
        """C51953686
        Verify the screen when the user enables only the 'Save' destination in the 'Add Shortcut' screen.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable only the 'Save' destination toggle bar in 'Add Shortcut' screen.
        7. Then click on the Continue button.
        8. Verify the screen.
        Expected: User should be navigated to the 'Add Save' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Then click on the Create your own shortcut arrow button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable only the 'Save' destination toggle bar
        self.hpxshortcuts.click_save_destination_toggle()
        # Step 7: Then click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Step 8: Verify the user is navigated to the 'Add Save' screen
        self.hpxshortcuts.verify_add_save_screen_displayed()

    def test_02_verify_back_button_in_add_save_screen(self):
        """C51953687
        Verify the screen when user clicks on 'back' button in 'Add save' screen.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Navigate 'Add save' screen.
        7. Click on the back button.
        8. Verify the screen.
        Expected: User should be navigated to the 'Add Shortcut' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Then click on the Create your own shortcut arrow button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Navigate 'Add save' screen
        self.hpxshortcuts.click_save_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 7: Click on the back button
        self.hpxshortcuts.click_back_btn()
        # Step 8: Verify user is navigated to the 'Add Shortcut' screen
        self.hpxshortcuts.verify_add_shortcut_screen_displayed()

    def test_03_verify_sign_in_link_for_cloud_accounts_in_add_save_screen(self):
        """C51953688
        Verify the screen when user clicks on 'Sign In' link of any cloud accounts under Add accounts in 'Add save' screen.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Navigate 'Add save' screen.
        7. Click on the 'Sign In' link of any cloud accounts in Add save screen.
        8. Verify the behavior.
        Expected: User should be able to signed in with the desired cloud accounts.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Then click on the Create your own shortcut arrow button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Navigate 'Add save' screen
        self.hpxshortcuts.click_save_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 7: Click on the 'Sign In' link of any cloud accounts
        self.hpxshortcuts.scroll("google_drive_sign_in", click_obj=True)

    def test_04_verify_screen_when_user_signed_in_with_cloud_destination(self):
        """C51953689
        Verify the screen when user signed in with 'Cloud' destination.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Navigate 'Add save' screen.
        7. Click on 'sign in' under add accounts.
        8. Verify the cloud destinations under Accounts screen.
        Expected: Cloud accounts should be displayed as signed in if the user is already signed in to any of these accounts on the device. (Ex: Google Drive, Dropbox, OneDrive)
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Then click on the Create your own shortcut arrow button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Navigate 'Add save' screen
        self.hpxshortcuts.click_save_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 7: Click on 'sign in' under add accounts
        self.hpxshortcuts.scroll("google_drive_sign_in", click_obj=True)

    def test_05_verify_existing_cloud_destination_in_add_save_screen_under_accounts_section(self):
        """C51953699
        Verify the existing 'Cloud' destination in 'Add save' screen under Accounts section.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Navigate 'Add save' screen.
        7. Verify the account section.
        Expected: The existing cloud accounts should be displayed under accounts section.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Then click on the Create your own shortcut arrow button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Navigate 'Add save' screen
        self.hpxshortcuts.click_save_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 7: Verify the account section
        self.hpxshortcuts.verify_accounts_section_displayed()

    def test_06_verify_pre_build_account_details_under_add_accounts_in_add_save_screen(self):
        """C51953700
        Verify the pre-build account details under 'Add accounts' in Add save screen.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Navigate 'Add save' screen.
        7. Verify the account section.
        Expected: The list of google accounts should be displayed under the Add accounts sections as shown in the below screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Then click on the Create your own shortcut arrow button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Navigate 'Add save' screen
        self.hpxshortcuts.click_save_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 7: Verify the account section
        self.hpxshortcuts.verify_accounts_section_displayed()

    def test_07_verify_confirmation_dialog_when_user_deletes_the_shortcut(self):
        """C51953701
        Verify the confirmation dialog when user deletes the shortcut.
        1. Install and Launch the HPX app.
        2. Navigate to Shortcuts screen then click on edit link.
        3.Click on Delete icon on shortcuts screen.
        4.Verify the screen.
        Expected: The 'Delete this shortcut' confirmation dialog should be displayed as shown in the screen below.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Add new shortcuts in shortcuts screen
        self.hpxshortcuts.verify_shortcuts_screen()
        # Step 5: Then click on edit button
        self.hpxshortcuts.click_edit_btn()
        # Step 6: Click on Delete icon on shortcuts screen
        self.hpxshortcuts.click_delete_email_shortcut_btn()

    def test_08_verify_position_of_the_buttons_on_the_Delete_this_Shortcut_pop_up_window(self):
        """C51953702
        Verify the behavior when user clicks on the 'OK' button in 'Remove HP access' dialog.
        1. Install and Launch the HPX app.
        2. Navigate to Shortcuts screen then click on edit link.
        3. Click on Delete icon on shortcuts screen.
        4. Verify the buttons of delete this shortcut pop up window.
        Expected: The position of the buttons on the 'Delete this Shortcut?' screen should have 'Delete' as the primary button and 'Cancel' as the secondary button.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Click on Delete icon on shortcuts screen.
        self.hpxshortcuts.verify_shortcuts_screen()
        self.hpxshortcuts.click_edit_btn()
        # Step 4: Verify the buttons of delete this shortcut pop up window
        self.hpxshortcuts.click_delete_email_shortcut_btn()

    def test_09_verify_screen_when_user_clicks_on_Delete_button_in_pop_up_window(self):
        """C51953703
        Verify the screen, when user clicks on Delete button in pop up window.
        1. Install and Launch the HPX app.
        2. Navigate to Shortcut edit turn on screen.
        3. Click on Delete icon on shortcuts screen.
        4. Then click on Delete button on delete this shortcut confirmation screen.
        5. Verify the screen.
        Expected: User should be navigated to the shortcuts screen and deleted shortcuts no longer should be displayed.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Click on Delete icon on shortcuts screen.
        self.hpxshortcuts.verify_shortcuts_screen()
        self.hpxshortcuts.click_edit_btn()
        # Step 4: Then click on Delete button on delete this shortcut confirmation screen
        self.hpxshortcuts.click_delete_email_shortcut_btn()
        self.driver.click("delete_btn")
        # Step 5: Verify the screen
        self.hpxshortcuts.verify_shortcuts_screen()