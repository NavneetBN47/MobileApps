
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
pytest.app_info = "SMART"

class Test_Suite_01_Edit_Shortcuts(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        """Class-level setup for Shortcuts test suite 01."""
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

    def test_01_disable_print_destination_toggle_in_edit_shortcut_screen(self):
        """ C51953718
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit icon next to the shortcuts.
        8. Disable the Print destination toggle bar.
        9. Verify the result.

        Expected: User should be able to Disable the 'Print' destination toggle bar in 'Edit Shortcut' screen.
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
        # Step 8: Disable the Print destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        # Step 9: Verify the toggle is disabled
        self.hpxshortcuts.verify_print_destination_toggle_disabled()

    def test_02_enable_email_destination_toggle_in_edit_shortcut_screen(self):
        """ C51953719
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit icon next to the shortcuts.
        8. Enable the Email destination toggle bar.
        9. Verify the result.

        Expected: User should be able to Enable the 'Email' destination toggle bar in 'Edit Shortcut' screen.
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
        self.hpxshortcuts.select_edit_btn_email_shortcuts_on_edit_shortcuts_screen()
        # Step 9: Verify the toggle is enabled
        self.hpxshortcuts.verify_email_destination_toggle_disabled()

    def test_03_disable_email_destination_toggle_in_edit_shortcut_screen(self):
        """ C51953720
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit icon next to the shortcuts.
        8. Disable the Email destination toggle bar.
        9. Verify the result.

        Expected: User should be able to Disable the 'Email' destination toggle bar in 'Edit Shortcut' screen.
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
        self.hpxshortcuts.select_edit_btn_email_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Disable the Email destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 9: Verify the toggle is disabled
        self.hpxshortcuts.verify_email_destination_toggle_disabled()

    def test_04_enable_save_destination_toggle_in_edit_shortcut_screen(self):
        """ C51953721
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit icon next to the shortcuts.
        8. Enable the Save destination toggle bar.
        9. Verify the result.

        Expected: User should be able to Enable the 'Save' destination toggle bar in 'Edit Shortcut' screen.
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
        self.hpxshortcuts.select_edit_btn_save_shortcuts_on_edit_shortcuts_screen()
        # Step 9: Verify the toggle is enabled
        self.hpxshortcuts.verify_save_destination_toggle_disabled()

    def test_05_disable_save_destination_toggle_in_edit_shortcut_screen(self):
        """ C51953722
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit icon next to the shortcuts.
        8. Disable the Save destination toggle bar.
        9. Verify the result.

        Expected: User should be able to Disable the 'Save' destination toggle bar in 'Edit Shortcut' screen.
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
        self.hpxshortcuts.select_edit_btn_save_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Disable the Save destination toggle bar
        self.hpxshortcuts.click_save_destination_toggle()
        # Step 9: Verify the toggle is disabled
        self.hpxshortcuts.verify_save_destination_toggle_disabled()

    def test_06_navigate_to_edit_print_screen_from_edit_shortcut(self):
        """ C51953723
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit print destination icon next to the shortcuts.
        8. Click on the continue button.
        9. Verify the screen.

        Expected: User should be navigated to the 'Edit print' screen.
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
        # Step 7: Click the Edit print destination icon next to the shortcuts
        self.hpxshortcuts.select_edit_btn_print_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Click on the continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 9: Verify navigation to 'Edit print' screen
        self.hpxshortcuts.verify_edit_print_screen_page_displayed()

    def test_07_back_from_edit_print_screen_navigates_to_edit_shortcut_screen(self):
        """ C51953724
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit print destination icon next to the shortcuts.
        8. Click on the continue button.
        9. Click on the back button in Edit print screen.
        10. Verify the screen.

        Expected: User should be redirected to the 'Edit Shortcut' screen without any error.
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
        # Step 7: Click the Edit print destination icon next to the shortcuts
        self.hpxshortcuts.select_edit_btn_print_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Click on the continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 9: Click on the back button in Edit print screen
        self.hpxshortcuts.click_back_btn()
        # Step 10: Verify the screen (should be Edit Shortcut screen)
        self.driver.wait_for_object("shortcuts_title", timeout=10)

    def test_08_select_copies_dropdown_in_edit_print_screen(self):
        """ C51953725
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit print destination icon next to the shortcuts.
        8. Click on the continue button.
        9. Click on the 'Copies' dropdown.
        10. Select any other value.
        11. Verify the screen.

        Expected: The list of other values should be displayed in the 'Copies' dropdown.
        User should be able to select any desired value in 'Copies' dropdown.
        The selected value should be displayed in 'Copies' dropdown.
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
        # Step 7: Click the Edit print destination icon next to the shortcuts
        self.hpxshortcuts.select_edit_btn_print_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Click on the continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 10: Select any other value
        self.hpxshortcuts.select_copies()

    def test_09_select_color_dropdown_in_edit_print_screen(self):
        """ C51953726
        1. Install and launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on shortcuts tile on the device details page.
        4. Verify the shortcut screen.
        5. Click on Add new shortcuts arrow in shortcuts screen.
        6. Then click on edit link.
        7. Then click the Edit print destination icon next to the shortcuts.
        8. Click on the continue button.
        9. Click on the 'Color' dropdown
        10. Select any other value.
        11. Verify the screen.

        Expected: The list of other options should be displayed in the 'Color' dropdown.
            User should be able to select any desired option in 'Color' dropdown.
            The selected option should be displayed in 'Color' dropdown.
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
        # Step 7: Click the Edit print destination icon next to the shortcuts
        self.hpxshortcuts.select_edit_btn_print_shortcuts_on_edit_shortcuts_screen()
        # Step 8: Click on the continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 9: Click on the 'Color' dropdown
        self.hpxshortcuts.select_color()

