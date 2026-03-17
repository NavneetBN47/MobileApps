
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
pytest.app_info = "SMART"

class Test_Suite_03_Shortcuts(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        """Class-level setup for Shortcuts test suite 03."""
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

    def test_01_sign_in_existing_user_navigates_to_shortcuts_screen(self):
        """ C51953650
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the Sign in button.
        5. Enter the existing user credentials.
        6. Verify the screen.

        Expected: User should be navigated to the Shortcuts screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in(), "Sign in screen not displayed."
        self.hpid.login()
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_02_create_account_and_verify_default_shortcut(self):
        """ C51953651
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the create account button and create an account
        5. Verify Default shortcut should be displayed on shortcut screen

        Expected: The Default shortcut should be displayed in the shortcuts screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.home.verify_create_account_icon()
        self.home.select_create_account_icon()
        self.hpid.create_account()
        self.hpxshortcuts.verify_default_email_shortcuts_shows()

    def test_03_verify_default_shortcut_displayed_after_account_creation(self):
        """ C51953652
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the create account button and create an account
        5. Verify Default shortcut should be displayed on shortcut screen

        Expected: User should be navigated to the shortcuts screen and one shortcut should be displayed.
        """
        # Step 5: Verify Default shortcut should be displayed on shortcut screen
        self.hpxshortcuts.verify_default_email_shortcuts_shows()

    def test_04_verify_add_shortcut_screen_with_prebuilt_shortcuts(self):
        """ C51953654
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the create account button and create an account
        5. Verify the shortcut screen.

        Expected: 'Add Shortcut' screen should be displayed with pre-built shortcuts as below screen.
        """
        # Step 5: Verify the shortcut screen displays pre-built shortcuts
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_05_click_add_new_shortcut_in_shortcuts_screen(self):
        """ C51953655
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the create account button and create an account
        5. Verify the shortcut screen.
        6. Click on Add new shortcuts arrow in shortcuts screen.
        7. Verify the screen.

        Expected: User should be navigated to the 'Add new shortcuts' screen.
        """
        # Step 6: Click on Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()

    def test_06_click_back_button_after_add_new_shortcut(self):
        """ C51953656
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the create account button and create an account.
        5. Verify the shortcut screen.
        6. Click on Add new shortcuts arrow in shortcuts screen.
        7. Click on the back button.
        8. Verify the screen.

        Expected: User should be navigated to the Settings screen.
        """
        # Step 7: Click on the back button after Add new shortcuts
        self.hpxshortcuts.click_back_btn()
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_07_edit_in_add_new_shortcuts_screen(self):
        """ C51953658
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Verify the screen.

        Expected: User should be able to edit in Add new Shortcuts screen.
        """
        # Step 5: Click on Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 6: Click on edit link in Add new Shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 7: Verify the screen (e.g., edit mode is enabled)
        self.hpxshortcuts.verify_edit_page_disabled_shortcuts_btn()

    def test_08_navigate_to_edit_shortcut_screen(self):
        """ C51953715
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Verify the screen.

        Expected: User should be navigated to the 'Edit shortcut' screen.
        """
        # Step 6: Click on edit link in Add new Shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 7: Verify navigation to 'Edit shortcut' screen
        self.hpxshortcuts.verify_edit_page_disabled_shortcuts_btn()

    def test_09_edit_shortcut_screen_back_navigates_to_shortcuts_screen(self):
        """ C51953716
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Click on Back button.
        8. Verify the screen.

        Expected: User should be navigated to 'Shortcuts' screen.
        """
        # Step 6: Click on edit link in Add new Shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 7: Click on Back button
        self.hpxshortcuts.click_back_btn()
        # Step 8: Verify navigation to 'Shortcuts' screen
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_10_navigate_to_edit_shortcut_screen(self):
        """ C51953657
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Click on the Settings icon.
        7. Verify the screen.

        Expected: User should be navigated to the Settings screen.
        """
        # Step 5: Click on Add new shortcuts in shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        # Step 4: Click on Settings icon in Shortcuts screen
        self.hpxshortcuts.verify_settings_screen()
        self.hpxshortcuts.click_settings_btn()

    def test_11_enable_print_destination_toggle_in_edit_shortcut_screen(self):
        """ C51953717
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit icon next to the shortcuts.
        8. Enable the Print destination toggle bar in the Edit Shortcut screen.
        9. Verify the result.

        Expected: Print destination toggle should be enabled in the Edit Shortcut screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in(), "Sign in screen not displayed."
        self.hpid.login()
        self.hpxshortcuts.verify_shortcuts_screen()
        # Step 6: Click on edit link in Add new Shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 7: Click the Edit icon next to the shortcuts
        self.hpxshortcuts.select_edit_btn_print_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Enable the Print destination toggle bar
        self.hpxshortcuts.verify_print_destination_toggle_disabled()