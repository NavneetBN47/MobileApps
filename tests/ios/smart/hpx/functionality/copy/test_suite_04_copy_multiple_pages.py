import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import OBJECT_SIZE

pytest.app_info = "SMART"

class Test_Suite_04_Copy_Multiple_Pages:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.fc.hpx = True
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.camera = cls.fc.fd["camera"]
        cls.copy = cls.fc.fd["copy"]
        cls.preview = cls.fc.fd["preview"]

    def test_01_select_copies_and_start_print(self):
        """
        Test Steps: C51924674
        1. Tap on the "Copies" option.
        2. Select the desired number of copies (e.g., 4).
        3. Tap on "Start Black" or "Start Colour" to initiate printing.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.verify_manual_button()
        self.camera.select_capture_btn()
        self.copy.select_number_of_copies(change_copies=3)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_02_add_multiple_images_via_capture_and_add_button(self):
        """
        Test Steps: C51924675
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual mode.
        4. Repeat steps 2 and 3 to add more images as needed.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.driver.swipe(direction="left")
        self.driver.swipe(direction="right")
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_03_add_and_remove_image_in_print_preview(self):
        """
        Test Steps: C51924676
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 2 and 3 to add another image.
        5. Click on the X (Remove/Delete) button on one image to keep only a single image in print preview.
        6. Observe the screen to verify only one image remains.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(1):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        for _ in range(1):
            self.preview.select_delete_page_icon()
        assert self.preview.verify_pages_option() == False, "Print preview does not show page option for only one image after removal."
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_04_add_and_remove_single_image_from_multiple_images(self):
        """
        Test Steps: C51924677
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 2 and 3 to add more images.
        5. Click on the X (Remove/Delete) button on the image and keep only a single image in print preview screen.
        6. Observe the screen to verify only one image remains.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        for _ in range(1):
            self.preview.select_delete_page_icon()
        assert self.preview.get_no_pages_from_preview_label() == 2, "Print preview does not show only one image after removal."
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_05_add_and_remove_all_images_then_back_popup(self):
        """
        Test Steps: C51924678
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 2 and 3 to add more images.
        5. Click on the X (Remove/Delete) button for all added images.
        6. For the final image, click on back button; popup with Yes & No appears.
        7. Click Yes and observe the screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_delete_page_icon()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()
        self.camera.verify_flash_btn()
        self.copy.verify_copy_tile_screen()
        self.copy.verify_manual_enabled()

    def test_06_add_multiple_images_and_handle_back_popup(self):
        """
        Test Steps: C51924679
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual mode.
        4. Repeat steps 1 & 2 to add more images.
        5. Click on back button; popup with Yes & No appears.
        6. Click Yes and observe the screen.
        7. Click No and observe the screen.
        excepted: 
        Step 5:The user lands on the Camera Capture screen with the following options:
            Capture button
        Step 6: User will see the preview screen
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()
        self.camera.verify_flash_btn()
        self.copy.verify_copy_tile_screen()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_no_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_07_single_page_capture_and_handle_back_popup(self):
        """
        Test Steps: C51924680
        1. Click on Capture button (manual or auto mode) to add a single page.
        2. Click on back button; popup with Yes & No appears.
        3. Click Yes and observe the screen.
        4. Click No and observe the screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_no_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_08_add_page_and_print_colour(self):
        """
        Test Steps: C51924681
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Click on Start Colour button.
        5. Click on Done button and observe the screen.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_add_page()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_color()
        self.preview.select_done_button_on_preview(timeout=30)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()

    def test_09_add_multiple_images_and_print_colour(self):
        """
        Test Steps: C51924682
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 1 & 2 to add more images.
        5. Click on Start Colour button.
        6. Click on Done button and observe the screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.copy.select_start_color()
        self.preview.select_done_button_on_preview(timeout=50)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_10_add_images_set_copies_and_print_colour(self):
        """
        Test Steps: C51924683
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Tap on copies and select No.of Copies (e.g., 3).
        5. Click on Start Colour button.
        6. Click on Done button and observe the screen.
        expected: 
        Step 4: User is able to see multiple copies and with single page printed successfully.
        2.Step 5: User sees a message stating "Sent".
        3.Step 6: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_add_page()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_number_of_copies(change_copies=3)
        self.copy.select_start_color()
        self.preview.select_done_button_on_preview(timeout=30)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_11_add_multiple_images_set_copies_and_print_colour(self):
        """
        Test Steps: C51924684
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 1 & 2 to add more images.
        5. Tap on copies and select No.of Copies (e.g., 3).
        6. Click on Start Colour button.
        7. Click on Done button and observe the screen.
        expected:
        1.Step 6: User is able to see multiple copies and pages printed successfully.
        2.Step 7: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.copy.select_number_of_copies(change_copies=3)
        self.copy.select_start_color()
        self.preview.select_done_button_on_preview(timeout=50)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_12_add_page_and_print_black(self):
        """
        Test Steps: C51924685
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Click on Start Black button.
        5. Click on Done button and observe the screen.
        expected:
        1.Step 4: User sees a message stating "Sent".
        2.Step 5: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_add_page()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()
        self.preview.select_done_button_on_preview(timeout=30)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_13_add_multiple_images_and_print_black(self):
        """
        Test Steps: C51924686
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 1 & 2 to add more images.
        5. Click on Start Black button.
        6. Click on Done button and observe the screen.
        expected:
        1.Step 5: User sees a message stating "Sent".
        2.Step 6: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()
        self.preview.select_done_button_on_preview(timeout=50)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_14_add_images_set_copies_and_print_black(self):
        """
        Test Steps: C51924687
        1. Click on Add button in print preview screen.
        2. Click on Capture button in manual or auto mode.
        3. Tap on copies and select No.of Copies (e.g., 3).
        4. Click on Start Black button.
        5. Click on Done button and observe the screen.
        expected:
        1.Step 4: User is able to see multiple copies and with single page printed successfully.
        2.Step 6: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_add_page()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_number_of_copies(change_copies=3)
        self.copy.select_start_black()
        self.preview.select_done_button_on_preview(timeout=30)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_15_add_multiple_images_set_copies_and_print_black(self):
        """
        Test Steps: C51924688
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. Repeat steps 1 & 2 to add more images.
        5. Tap on copies and select No.of Copies (e.g., 3).
        6. Click on Start Black button.
        7. Click on Done button and observe the screen.
        expected:
        1.Step 4: User is able to see multiple copies and pages printed successfully.
        2.Step 5: User sees a message stating "Sent".
        3.Step 6: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.copy.select_number_of_copies(change_copies=3)
        self.copy.select_start_black()
        self.preview.select_done_button_on_preview(timeout=50)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_16_capture_with_object_size_and_print(self):
        """
        Test Steps: C51924691
        1. Click on Capture button.
        2. Tap on "Object Size" at the bottom right corner of the capture screen.
        3. Select the desired document size.
        4. Tap on the Capture button.
        5. Print the captured image using the Black or Colour option.
        expected:
        The user is able to see that the image is printed successfully in A4 size and in Black or Colour.
        """
        self.copy.select_object_size(object_size=OBJECT_SIZE.SIZE_LETTER)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()
        self.preview.select_ok()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_17_add_images_print_and_cancel_popup(self):
        """
        Test Steps: C51924690
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. (Optional) Repeat steps 2 & 3 to add more images if required.
        5. Click on Start Colour or Start Black button.
        6. Click on Done button.
        7. Tap "Cancel" Button from popup window and observe the screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()
        self.preview.select_ok()
        self.preview.select_done_button_on_preview(timeout=50)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.click_cancel_on_popup()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_18_add_images_print_and_go_home(self):
        """
        Test Steps: C51924689
        1. Click on Capture button.
        2. Click on Add button in print preview screen.
        3. Click on Capture button in manual or auto mode.
        4. (Optional) Repeat steps 2 & 3 to add more images if required.
        5. Click on Start Colour or Start Black button.
        6. Click on Done button.
        7. Tap "Yes, Go Home" from popup window and observe the screen.
        expected:
        1.Step 4: User sees a message stating "Sent".
        2.Step 5: User navigated to "Home Screen"(Tiles Page).
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        for _ in range(2):
            self.preview.select_add_page()
            self.camera.select_capture_btn()
            self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()
        self.preview.select_done_button_on_preview(timeout=50)
        self.preview.verify_popup_after_click_done_btn()
        self.preview.select_yes_go_home_btn()

