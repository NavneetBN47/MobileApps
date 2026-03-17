import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
pytest.app_info = "SMART"

class Test_Suite_04_Shortcuts(object):

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

    def test_01_verify_two_sided_dropdown_behavior_in_add_print_screen(self):
        """C51953675
        Verify the behavior when the user selects any option in the 'Two-sided' dropdown on the 'Add Print' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to Add Shortcuts screen.
        4. Enable only the 'Print' destination toggle bar.
        5. Click on the 'Two-sided' dropdown.
        6. Select any other option.
        7. Verify the screen.
        Expected: The list of other options should be displayed in the Two-sided dropdown.
        User should be able to select any desired option in Two-sided dropdown.
        The selected option should be displayed in Two-sided dropdown.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to Add Shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 5: Click on the 'Two-sided' dropdown
        self.hpxshortcuts.click_two_sided_dropdown()
        # Step 7: Verify the selected option is displayed
        self.hpxshortcuts.verify_two_sided_dropdown_selection("shortedge")

    def test_02_verify_add_to_shortcut_button_in_add_print_screen(self):
        """C51953676
        Verify the behavior when user clicks on 'Add to Shortcut' button in Add print screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to Add Shortcuts screen.
        4. Enable only the 'Print' destination toggle bar.
        5. Select the print settings.
        6. Click on the Add to Shortcut button.
        7. Verify the behavior.
        Expected: User should be redirected to 'Add shortcut' screen with the saved details from 'Add print' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to Add Shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 5: Select the print settings
        self.hpxshortcuts.select_copies()
        self.hpxshortcuts.select_color()
        # Step 6: Click on the Add to Shortcut button
        self.hpxshortcuts.click_continue_btn()

    def test_03_verify_add_to_shortcut_after_modifying_print_settings(self):
        """C51953677
        Verify the behavior when the user clicks the 'Add to Shortcut' button after modifying the print settings on the 'Add Print' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to Add Shortcuts screen.
        4. Enable only the 'Print' destination toggle bar.
        5. Modify the desired print settings.
        6. Click on the Add to Shortcut button.
        7. Verify the behavior.
        Expected: User should be redirected to 'Add shortcut' screen with the saved details from 'Add print' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to Add Shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        self.hpxshortcuts.click_continue_btn()
        # Step 5: Modify the desired print settings
        self.hpxshortcuts.select_copies()
        self.hpxshortcuts.select_color()
        self.hpxshortcuts.click_two_sided_dropdown()
        self.hpxshortcuts.verify_two_sided_dropdown_selection("shortedge")
        # Step 6: Click on the continue button
        self.hpxshortcuts.click_continue_btn()

    def test_04_verify_email_destination_in_add_shortcut_screen(self):
        """C51953678
        Verify the screen when the user enables only the 'Email' destination in the 'Add Shortcut' screen.
        1. Install and Launch the HPX app.
        2. Click on the printer icon on the root view screen.
        3. Then click on the shortcuts tile on the device details page.
        4. Click on the Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable only the 'Email' destination toggle bar in 'Add Shortcut' screen.
        7. Then click on the Continue button.
        8. Verify the screen.
        Expected: User should be navigated to the 'Add Email' screen.
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
        # Step 6: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 7: Then click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Step 8: Verify the user is navigated to the 'Add Email' screen
        self.hpxshortcuts.verify_add_email_screen_displayed()

    def test_05_verify_back_button_in_add_email_screen(self):
        """C51953679
        Verify the screen when the user clicks the 'Back' button on the 'Add Print' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to 'Add Shortcuts' screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Click on the back button in Add email screen.
        7. Verify the behavior.
        Expected: User should be redirected to the 'Add Shortcut' screen without any error.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to 'Add Shortcuts' screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Step 6: Click on the back button in Add email screen
        self.hpxshortcuts.click_back_btn()
        # Step 7: Verify user is redirected to the 'Add Shortcut' screen
        self.hpxshortcuts.verify_add_shortcut_screen_displayed()

    def test_06_verify_valid_email_address_in_add_email_screen(self):
        """C51953680
        Verify the 'To' section when the user enters a valid email address in the 'Add Email' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to 'Add Shortcuts' screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Enter the valid email address in 'To' section.
        7. Click on the 'Add to Shortcut' button.
        8. Verify the behavior.
        Expected: User should be redirected to the 'Add Shortcut' screen with saved details from 'Add email' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to 'Add Shortcuts' screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Verify Add Email screen is displayed
        self.hpxshortcuts.verify_add_email_screen_displayed()
        # Step 6: Enter the valid email address in 'To' section
        self.hpxshortcuts.enter_multiple_email_addresses_in_to_section(1)
        # Step 7: Click on the 'Add to Shortcut' button
        self.hpxshortcuts.click_continue_btn()

    def test_07_verify_invalid_email_address_in_add_email_screen(self):
        """C51953681
        Verify the 'To' section when the user enters an invalid email address in the 'Add Email' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to 'Add Shortcuts' screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Enter the invalid email address in 'To' section.
        7. Click on the 'Add to Shortcut' button.
        8. Verify the behavior.
        Expected: Error message should be displayed and the user should not be able to move forward.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to 'Add Shortcuts' screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Verify Add Email screen is displayed
        self.hpxshortcuts.verify_add_email_screen_displayed()
        # Step 6: Enter the invalid email address in 'To' section
        self.hpxshortcuts.enter_email_address_in_to_section("invalid-email")
        # Step 7: Click on the 'Add to Shortcut' button
        self.hpxshortcuts.click_add_to_shortcut_btn()
        # Step 8: Verify error message is displayed
        self.hpxshortcuts.verify_email_error_message_displayed()

    def test_08_verify_multiple_email_addresses_in_add_email_screen(self):
        """C51953682
        Verify the 'To' section when the user enters more than one email address in the 'Add Email' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to 'Add Shortcuts' screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Enter more than one email address in 'To' section.
        7. Click on the 'Add to Shortcut' button.
        8. Verify the behavior.
        Expected: User should be redirected to the 'Add Shortcut' screen with saved details from 'Add email' screen.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to 'Add Shortcuts' screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Verify Add Email screen is displayed
        self.hpxshortcuts.verify_add_email_screen_displayed()
        # Step 6: Enter more than one email address in 'To' section
        self.hpxshortcuts.enter_multiple_email_addresses_in_to_section(20)  # Example with 20 email addresses
        # Step 7: Click on the 'Add to Shortcut' button
        self.hpxshortcuts.click_add_to_shortcut_btn()
        # Step 8: Verify user is redirected to 'Add Shortcut' screen with saved details
        self.hpxshortcuts.verify_continue_btn()

    def test_09_verify_more_than_20_email_addresses_in_add_email_screen(self):
        """C51953683
        Verify the 'To' section when the user enters more than 20 email addresses in the 'Add Email' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to 'Add Shortcuts' screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Enter more than 20 email addresses in 'To' section.
        7. Click on the 'Add to Shortcut' button.
        8. Verify the behavior.
        Expected: Error message should be displayed and the user should not be able to move forward.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to 'Add Shortcuts' screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Verify Add Email screen is displayed
        self.hpxshortcuts.verify_add_email_screen_displayed()
        # Step 6: Enter more than 20 email addresses in 'To' section
        self.hpxshortcuts.enter_multiple_email_addresses_in_to_section(21)  # Example with 21 email addresses
        # Step 7: Click on the 'Add to Shortcut' button
        self.hpxshortcuts.click_add_to_shortcut_btn()
        self.hpxshortcuts.verify_continue_btn()
        # Step 8: Verify error message is displayed
        self.hpxshortcuts.verify_too_many_emails_error_message_displayed()

    def test_10_verify_subject_field_in_add_email_screen(self):
        """C51953684
        Verify the 'Subject' dropdown in 'Add email' screen.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to Add Shortcuts screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Select any option from subject dropdown.
        7. Click on the 'Add to Shortcut' button.
        8. Verify the behavior.
        Expected: User should able to select any option from the subject dropdown.[TBD]
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to Add Shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Verify Add Email screen is displayed
        self.hpxshortcuts.verify_add_email_screen_displayed()
        # Step 6: Select any option from subject dropdown
        self.hpxshortcuts.click_subject_field()
        self.hpxshortcuts.enter_subject_field("Test Subject")
        # Step 7: Click on the 'Add to Shortcut' button
        self.hpxshortcuts.enter_email_address_in_to_section(1)
        self.hpxshortcuts.click_add_to_shortcut_btn()
        # Step 8: Verify behavior
        self.hpxshortcuts.verify_continue_btn()

    def test_11_verify_body_section_modification_in_add_email_screen(self):
        """C51953685
        Verify the 'Body' section of the 'Add Email' screen when the user modifies text.
        1. Install and Launch the HPX app.
        2. Navigate to printer details screen.
        3. Navigate to Add Shortcuts screen.
        4. Enable only the 'Email' destination toggle bar.
        5. Click on the Continue button.
        6. Modify the text in 'Body' section.
        7. Click on the 'Add to Shortcut' button.
        8. Verify the behavior.
        Expected: User should able to modify the text in body section and user should be moved forward.
        """
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Navigate to printer details screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Navigate to Add Shortcuts screen
        self.hpxshortcuts.click_add_shortcut()
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 4: Enable only the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 5: Click on the Continue button
        self.hpxshortcuts.click_continue_btn()
        # Verify Add Email screen is displayed
        self.hpxshortcuts.verify_add_email_screen_displayed()
        # Step 6: Modify the text in 'Body' section
        self.hpxshortcuts.modify_email_body_text("This is a test email body message.")
        # Step 7: Click on the 'Add to Shortcut' button
        self.hpxshortcuts.enter_email_address_in_to_section(1)
        self.hpxshortcuts.click_add_to_shortcut_btn()
        # Step 8: Verify behavior
        self.hpxshortcuts.verify_continue_btn()