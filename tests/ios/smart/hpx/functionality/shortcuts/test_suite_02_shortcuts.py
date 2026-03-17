import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
pytest.app_info = "SMART"

class Test_Suite_02_Shortcuts(object):
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

    def test_01_verify_shortcuts_tile_on_device_details(self):
        """C51953630
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Verify the shortcuts tile on device details page.
        Expected: Shortcuts' tile should be displayed on the printer device page.
        """# Step 1: Launch app
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        # Step 3: Verify the shortcuts tile is displayed on device details page
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile")
        self.hpxshortcuts.verify_shortcuts_tile_btn()
    
    def test_02_verify_getting_information_loading_screen(self):
        """
        C51953631
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Verify the behaviour.
        Expected: The user should be navigated to the 'sign in' screen.
        During a slow network when the user clicks on the 'Shortcuts' tile Getting Information loading screen will be displayed.
        """
        # Step 4: Verify the 'Getting information' loading screen is displayed 
        self.hpxshortcuts.click_shortcuts_tile_btn()
        self.home.verify_sign_in_icon()
        
    def test_03_verify_shortcuts_tile_requires_login(self):
        """
        C51953632
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the behaviour.
        Expected: The user should not be able to access the shortcuts tile without logging in.
        """
        # Step 4: Verify that the user is prompted to log in or cannot access shortcuts
        self.home.verify_sign_in_icon()
        self.home.verify_create_account_icon() #"User was able to access shortcuts tile without logging in."
    
    def test_04_verify_sign_in_dialog_displayed_for_shortcuts(self):
        """
        C51953633
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the behaviour.
        Expected: Dialog screen should be displayed as below screen.
        "Sign in to use Shortcuts\ Use Shortcuts to automate tasks you do often, like printing, emailing and saving"
        """
        # Step 4: Verify the sign-in dialog is displayed with the expected message
        self.home.verify_sign_in_icon()
    
    def test_05_verify_sign_in_dialog_back_navigates_to_device_page(self):
        """
        C51953634
        1. Install and Launch the HPX app.
        2. Navigate to the printer details page then click on the shortcuts tile.
        3. In 'Sign in to use shortcuts' dialog screen click on 'Back' button.
        4. Verify the screen.
        Expected: User should be navigated to the Printer device page.
        """
        # Step 3: In 'Sign in to use shortcuts' dialog screen click on 'Back' button
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        # Step 3: Verify the shortcuts tile is displayed on device details page
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.home.verify_sign_in_icon()
        self.home.click_sign_btn_hpx()
        # Step 4: Verify the user is navigated to the Printer device page (e.g., check for a unique element)
        self.hpxshortcuts.click_cancel_btn()
        self.home.verify_device_details_page()

    def test_06_verify_sign_in_dialog_displayed_for_shortcuts(self):
        """
        C51953635
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the behaviour.
        Expected: Dialog screen should be displayed as below screen.
        "Sign in to use Shortcuts\nUse Shortcuts to automate tasks you do often, like printing, emailing and saving"
        """
        # Step 4: Verify the sign-in dialog is displayed with the expected message
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.home.verify_sign_in_icon()

    def test_07_verify_position_of_sign_in_dialog_displayed_for_shortcuts(self):
        """
        C51953636
        Description: Verify the position of the sign-in dialog displayed for shortcuts.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the behaviour.
        Expected: The position of the buttons on the 'Sign in to use Shortcuts' screen should have 'Sign in' as the primary button and 'Create Account' as the secondary button
        """
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.home.verify_sign_in_icon()
        self.home.verify_create_account_icon()
    
    def test_08_verify_sign_in_navigates_to_sign_in_screen(self):
        """
        C51953639
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the Sign in button.
        5. Verify the screen.
        Expected: User should be navigated to the 'Sign in' screen.
        """
        # Step 5: Verify the user is navigated to the 'Sign in' screen
        self.driver.click("signin_btn")
        # self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in(), "User was navigated to the 'Sign in' screen."

    def test_09_verify_sign_in_existing_user_navigates_to_shortcuts_screen(self):
        """
        C51953640
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the Sign in button.
        5. Enter the existing user credentials.
        6. Verify the screen.
        Expected: User should be navigated to the Shortcuts screen.
        """
        # Step 5: Enter the existing user credentials
        assert self.hpid.verify_hp_id_sign_in() # "Sign in screen not displayed."
        self.hpid.login()
        # Step 6: Verify the user is navigated to the Shortcuts screen (e.g., Add Shortcut button is present)
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_10_verify_create_account_dialog_displayed_for_shortcuts(self):
        """C51953637
        Description: Verify the position of the create account dialog displayed for shortcuts.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the Create account button.
        5. Verify the behaviour.
        Expected: User should be navigated to the 'Sign in with your HP account' screen.
        """
        # Step 1: Launch app (do not sign in)
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on the Create account button
        self.home.verify_create_account_icon()
        self.home.select_create_account_icon()
        # Step 4: Verify the sign-in dialog is displayed with the expected message
        assert self.hpid.verify_hp_id_create_account_screen()

    def test_11_verify_create_account_navigates_to_shortcuts_screen(self):
        """
        C51953638
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the Create account button.
        5. Create the account.
        6. Verify the screen.
        Expected: User should be navigated to the 'Shortcuts' screen.
        """
        # Step 5: Create the account (simulate account creation flow)
        assert self.hpid.verify_hp_id_create_account_screen()
        self.hpid.create_account()
        # Step 6: Verify the user is navigated to the 'Shortcuts' screen (e.g., Add Shortcut button is present)
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_12_verify_shortcuts_screen_back_navigates_to_device_page(self):
        """
        C51953647
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the screen.
        Expected: By default Email shortcut should be added in shortcuts screen.[TBD]
        """
        self.hpxshortcuts.verify_shortcuts_screen()
        self.hpxshortcuts.click_edit_btn()
        self.hpxshortcuts.verify_default_email_shortcuts_shows() 
    
    def test_13_verify_delete_default_email_shortcut(self):
        """
        C51953649
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on the Email shortcut.
        5. Click on the Delete button.
        6. Verify the screen.
        Expected: Email shortcut should be removed from the shortcuts screen.
        """
        self.hpxshortcuts.verify_default_email_shortcuts_shows()
        self.hpxshortcuts.click_delete_email_shortcut_btn()

    def test_14_shortcuts_screen_back_navigates_to_device_page(self):
        """
        C51953641
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on Back button in Shortcuts screen.
        5. Verify the screen.
        Expected: User should be navigated to the printer device page.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on Back button in Shortcuts screen
        self.hpxshortcuts.click_back_btn()
        # Step 5: Verify the user is navigated to the printer device page (e.g., check for a unique element)
        self.home.verify_device_details_page()

    def test_15_shortcuts_settings_icon_navigates_to_settings_screen(self):
        """
        C51953642
        1. Install and Launch the HPX app and sign in.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on Settings icon in Shortcuts screen.
        5. Verify the screen.
        Expected: User should be navigated to the Settings screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on Settings icon in Shortcuts screen
        self.hpxshortcuts.verify_settings_screen()
        self.hpxshortcuts.click_settings_btn()

    def test_16_shortcuts_edit_link_navigates_to_edit_screen(self):
        """
        C51953643
        1. Install and Launch the HPX app and sign in.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on Edit link in shortcuts screen.
        5. Verify the screen.
        Expected: User should be navigated to the 'Shortcuts -Edit turned on' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on Edit link in shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 5: Verify the user is navigated to the 'Shortcuts -Edit turned on' screen (e.g., check for a unique element)
        self.hpxshortcuts.verify_edit_page_disabled_shortcuts_btn()


    def test_17_shortcuts_edit_link_and_add_new_shortcut_disabled(self):
        """
        C51953644
        1. Install and Launch the HPX app and sign in.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on Edit link in shortcuts screen.
        5. Verify the screen.
        Expected: The "Edit" link and "Add New Shortcut" element should be disabled, and the user should not be able to access them.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on Edit link in shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 5: Verify the Edit link and Add New Shortcut element are disabled
        self.hpxshortcuts.verify_edit_page_disabled_shortcuts_btn()

    def test_18_edit_mode_back_navigates_to_shortcuts_screen(self):
        """
        C51953645
        1. Install and Launch the HPX app and sign in.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on Edit link in shortcuts screen.
        5. Then click on back button
        6. Verify the screen.
        Expected: User should be navigated to the Shortcuts screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()

        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on Edit link in shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 5: Click on back button
        self.hpxshortcuts.click_back_btn()
        # Step 6: Verify the user is navigated to the Shortcuts screen (e.g., Add Shortcut button is present)
        self.hpxshortcuts.verify_shortcuts_screen()

    def test_19_verify_edit_mode_settings_btn_on_shortcuts_screen(self):
        """
        C51953646
        1. Install and Launch the HPX app and sign in.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Click on Edit link in shortcuts screen.
        5. Then click on back button
        6. Verify the screen.
        Expected: User should be navigated to the Shortcuts screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Click on Edit link in shortcuts screen
        self.hpxshortcuts.click_edit_btn()
        # Step 5: Click on back button
        self.hpxshortcuts.click_settings_btn()

    def test_20_verify_list_of_existing_shortcuts_on_screen(self):
        """
        C51953648
        1. Install and Launch the HPX app and sign in.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the screen.
        Expected: The list of existing shortcuts should be displayed in the shortcuts screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 4: Verify the list of existing shortcuts is displayed in the shortcuts screen
        self.hpxshortcuts.verify_shortcuts_screen()