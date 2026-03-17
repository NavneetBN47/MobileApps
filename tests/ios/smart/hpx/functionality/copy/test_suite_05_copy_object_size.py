import pytest
from MobileApps.resources.const.ios import const as i_const
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_05_Copy_Object_Size:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = None
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

    def test_01_print_4x6_object_size_black_and_colour(self):
        """
        C51924692: Verify that the printer page's object size is set to 4*6 in/10*15 cm when the "Start Black" or "Start Colour" button is clicked.
        1. Tap on "Object Size" at the bottom right corner of the capture screen.
        2. Select the desired document size (4x6 in/10x15 cm).
        3. Tap on the "Capture" button.
        4. Print the captured image using the Black or Colour option.
        Expected: The image is printed successfully in 4x6 in/10x15 cm size and in Black or Colour.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.select_object_size(i_const.OBJECT_SIZE.SIZE_4x6)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()

    def test_02_print_5x7_object_size_black_and_colour(self):
        """
        C51924693: Verify that the printer page's object size is set to 5*7 in/13*18 cm when the "Start Black" or "Start Colour" button is clicked.
        1. Tap on "Object Size" at the bottom right corner of the capture screen.
        2. Select the desired document size (5x7 in/13x18 cm).
        3. Tap on the "Capture" button.
        4. Print the captured image using the Black or Colour option.
        Expected: The image is printed successfully in 5x7 in/13x18 cm size and in Black or Colour.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.select_object_size(i_const.OBJECT_SIZE.SIZE_5x7)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()

    def test_03_print_id_card_object_size_black_and_colour(self):
        """
        C51924694: Verify that the printer page's object size is set to ID Card when the "Start Black" or "Start Colour" button is clicked
        1. Tap on "Object Size" at the bottom right corner of the capture screen.
        2. Select the desired document size (ID Card).
        3. Tap on the "Capture" button.
        4. Print the captured image using the Black or Colour option.
        Expected: The image is printed successfully in ID Card size and in Black or Colour.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.select_object_size(i_const.OBJECT_SIZE.SIZE_DRIVER_LICENSE)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()

    def test_04_print_id_card_object_size_black_and_colour(self):
        """
        C51924695: Verify that the printer page's object size is set to Business Card when the "Start Black" or "Start Colour" button is clicked
        1. Tap on "Object Size" at the bottom right corner of the capture screen.
        2. Select the desired document size (ID Card).
        3. Tap on the "Capture" button.
        4. Print the captured image using the Black or Colour option.
        Expected: The image is printed successfully in ID Card size and in Black or Colour.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.select_object_size(i_const.OBJECT_SIZE.SIZE_BUSINESS_CARD)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_start_black()