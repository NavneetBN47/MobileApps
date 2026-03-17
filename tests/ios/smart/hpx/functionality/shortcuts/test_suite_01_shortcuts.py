import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
pytest.app_info = "SMART"

class Test_Suite_01_Shortcuts(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        """Class-level setup for Shortcuts test suite."""
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
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.hpxshortcuts = cls.fc.fd["hpx_shortcuts"]

    def test_01_navigate_to_add_shortcut_screen(self):
        """C51953660
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Verify the screen.
        Expected result: User should be navigated to the 'Add shortcut' screen."""
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Verify the Add Shortcut screen is displayed (look for a unique element, e.g., the Save button or a title)
        self.hpxshortcuts.verify_save_destination_toggle()

    def test_02_cancel_add_shortcut_popup(self):
        """C51953661
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Click on the back button in Add Shortcut screen.
        7. Verify the screen.
        Expected result: 'Cancel this Shortcut?' pop up window should be displayed."""
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Click on the cancel button in Add Shortcut screen
        self.hpxshortcuts.click_cancel_btn()
        # Step 7: Verify the 'Cancel this Shortcut?' pop up window is displayed
        assert self.driver.wait_for_object("cancel_yes_btn")

    def test_03_cancel_shortcut_creation_popup_buttons(self):
        """C51953662
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Click on the back button in Add Shortcut screen.
        7. Verify the buttons of cancel shortcut creation pop up window.
        8. Verify the pop up screen.
        Expected result: The position of the buttons on the 'Cancel Shortcut Creation' screen should have 'Yes, cancel' as the primary button and 'Go back' as the secondary button."""
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Click on the cancel button in Add Shortcut screen
        self.hpxshortcuts.click_cancel_btn()
        # Step 7: Verify the buttons of the cancel shortcut creation pop up window
        assert self.driver.wait_for_object("cancel_yes_btn")  # 'Yes, cancel' button
        assert self.driver.wait_for_object("cancel_goback_btn")  # 'Go back' button

    def test_04_cancel_popup_go_back_returns_to_add_shortcut(self):
        """C51953663
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Click on the back button in Add Shortcut screen.
        7. Click on 'Go back' button on pop up screen.
        8. Verify the screen.
        Expected result: User should be redirected to the 'Add Shortcut' screen.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Click on the cancel button in Add Shortcut screen
        self.hpxshortcuts.click_cancel_btn()
        # Step 7: Click on 'Go back' button on pop up screen
        self.driver.wait_for_object("cancel_goback_btn")
        self.driver.click("cancel_goback_btn")
        # Step 8: Verify the user is redirected to the Add Shortcut screen (e.g., Save button is present)
        self.hpxshortcuts.verify_save_destination_toggle()

    def test_05_cancel_popup_yes_cancel_returns_to_shortcuts(self):
        """
        C51953664
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Click on the back button in Add Shortcut screen.
        7. Click on 'Yes, cancel' button on pop up screen.
        8. Verify the screen.
        Expected result: User should be redirected to the 'Shortcuts' screen.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Click on the cancel button in Add Shortcut screen
        self.hpxshortcuts.click_cancel_btn()
        # Step 7: Click on 'Yes, cancel' button on pop up screen
        self.driver.wait_for_object("cancel_yes_btn")
        self.hpxshortcuts.click_cancel_yes_btn()
        # Step 8: Verify the user is redirected to the Shortcuts screen (e.g., Add Shortcut button is present)
        assert self.driver.wait_for_object("add_shortcuts_btn")

    def test_06_enable_print_destination_toggle(self):
        """C51953665
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable the 'Print' destination toggle bar in 'Add Shortcut' screen.
        7. Verify the screen.
        Expected result: User should be able to enable the 'Print' destination toggle bar in 'Add shortcut' screen. After enabling, the 'continue' button should be enabled.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        # Step 7: Verify the Print destination is enabled (e.g., print_destinations element is present/enabled)
        self.hpxshortcuts.verify_continue_btn()

    def test_07_disable_print_toggle_disable_continue(self):
        """
        C51953666
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Disable the 'Print' destination toggle bar in 'Add Shortcut' screen
        7. Verify the screen.
        Expected result: User should be able to disable the 'Print' destination toggle bar in 'Add shortcut' screen. After disbale, the 'continue' button should be disabled.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Disable the 'Print' destination toggle bar (toggle twice: enable then disable)
        self.hpxshortcuts.click_print_destination_toggle()  # Enable first
        self.hpxshortcuts.click_print_destination_toggle()  # Then disable
        # Step 7: Verify the Print destination is disabled and 'continue' button is diabled
        self.hpxshortcuts.verify_continue_btn()

    def test_08_enable_email_toggle_enables_continue(self):
        """C51953667
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable the 'Email' destination toggle bar in 'Add Shortcut' screen.
        7. Verify the screen.
        Expected result: User should be able to enable the 'Email' destination toggle bar in 'Add shortcut' screen. After enabling, the 'continue' button should be enabled.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable the 'Email' destination toggle bar
        self.hpxshortcuts.click_email_destination_toggle()
        # Step 7: Verify the Email destination is enabled and 'continue' button is enabled
        self.hpxshortcuts.verify_continue_btn()

    def test_09_disable_email_toggle_disables_continue(self):
        """C51953668
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Disable the 'Email' destination toggle bar in 'Add Shortcut' screen.
        7. Verify the screen.
        Expected result: User should be able to disable the 'Email' destination toggle bar in 'Add shortcut' screen. After disabling, the 'continue' button should be disabled.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Disable the 'Email' destination toggle bar (toggle twice: enable then disable)
        self.hpxshortcuts.click_email_destination_toggle()  # Enable first
        self.hpxshortcuts.click_email_destination_toggle()  # Then disable
        # Step 7: Verify the Email destination is disabled and 'continue' button is disabled
        self.hpxshortcuts.verify_continue_btn()

    def test_10_enable_save_toggle_enables_continue(self):
        """C51953669
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable the 'Save' destination toggle bar in 'Add Shortcut' screen.
        7. Verify the screen.
        Expected result: User should be able to enable the 'Save' destination toggle bar in 'Add shortcut' screen. After enabling, the 'continue' button should be enabled.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable the 'Save' destination toggle bar
        self.hpxshortcuts.click_save_destination_toggle()
        # Step 7: Verify the Save destination is enabled and 'continue' button is enabled
        self.hpxshortcuts.verify_save_destination_toggle()
        self.hpxshortcuts.verify_continue_btn()

    def test_11_disable_save_toggle_disables_continue(self):
        """C51953670
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Disable the 'Save' destination toggle bar in 'Add Shortcut' screen.
        7. Verify the screen.
        Expected result: User should be able to disable the 'Save' destination toggle bar in 'Add shortcut' screen. After disabling, the 'continue' button should be disabled.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Disable the 'Save' destination toggle bar (toggle twice: enable then disable)
        self.hpxshortcuts.click_save_destination_toggle()  # Enable first
        self.hpxshortcuts.click_save_destination_toggle()  # Then disable
        # Step 7: Verify the Save destination is disabled and 'continue' button is disabled
        self.hpxshortcuts.verify_continue_btn()

    def test_12_enable_print_toggle_and_continue_navigates_to_add_print(self):
        """C51953671
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable only the 'Print' destination toggle bar in 'Add Shortcut' screen.
        7. Then click on the Continue button.
        8. Verify the screen.
        Expected result: User should be navigated to the 'Add print' screen.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable only the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        # Ensure other toggles are off (if needed, can add logic to disable email/save)
        # Step 7: Click on the Continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 8: Verify navigation to 'Add print' screen (look for a unique element, e.g., print settings or print destination)
        assert self.driver.wait_for_object("add_print_screen_title")  # Replace with actual object name if different

    def test_13_cancel_button_returns_to_add_shortcut_screen(self):
        """C51953672
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Click on the cancel button.
        7. Verify the screen.
        Expected result: User should be redirected to the 'Add Shortcut' screen without any error.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Click on the cancel button
        self.hpxshortcuts.click_cancel_btn()
        # Step 7: Click on 'Yes, cancel' button on pop up screen
        self.driver.wait_for_object("cancel_yes_btn")
        self.hpxshortcuts.click_cancel_yes_btn()
        # Step 8: Verify the user is redirected to the Shortcuts screen (e.g., Add Shortcut button is present)
        assert self.driver.wait_for_object("add_shortcuts_btn")

    def test_14_select_copies_dropdown_value_in_add_print_screen(self):
        """C51953673
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable only the 'Print' destination toggle bar.
        7. Click on the Continue button.
        8. Click on the 'Copies' dropdown.
        9. Select any other value.
        10. Verify the screen.
        Expected result: The list of other values should be displayed in the 'Copies' dropdown. User should be able to select any desired value in 'Copies' dropdown. The selected value should be displayed in 'Copies' dropdown.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable only the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        # Step 7: Click on the Continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 8: Click on the 'Copies' dropdown
        self.hpxshortcuts.select_copies()

    def test_15_select_color_dropdown_option_in_add_print_screen(self):
        """C51953674
        1. Install and launch the app.
        2. Add the target device to the root view.
        3. Navigate to device details screen.
        4. Click on Add new shortcuts in shortcuts screen.
        5. Then click on the Create your own shortcut arrow button.
        6. Enable only the 'Print' destination toggle bar.
        7. Click on the Continue button.
        8. Click on the 'Color' dropdown.
        9. Select any other option.
        10. Verify the screen.
        Expected result: The list of other options should be displayed in the 'Color' dropdown. User should be able to select any desired option in 'Color' dropdown. The selected option should be displayed in 'Color' dropdown.
        """
        # Step 1 & 2: Launch app and add printer
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 3: Navigate to device details screen
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("allow_btn")
        # Step 4: Click on the Shortcuts tile (add shortcut)
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_add_shortcut()
        # Step 5: Click on Create your own Shortcut button
        self.hpxshortcuts.click_create_your_own_shortcut_btn()
        # Step 6: Enable only the 'Print' destination toggle bar
        self.hpxshortcuts.click_print_destination_toggle()
        # Step 7: Click on the Continue button
        self.hpxshortcuts.verify_continue_btn()
        # Step 8: Click on the 'Color' dropdown
        self.hpxshortcuts.select_color()