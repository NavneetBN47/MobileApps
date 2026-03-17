import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_04_Device_Page_Tiles:

    @pytest.fixture(scope="class", autouse="true")
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
        cls.photos = cls.fc.fd["photos"]
        cls.fc.hpx = True
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.printers = cls.fc.fd["printers"]

    def test_01_verify_scan_tile(self):
        """
        Description: C52905357
                1. Launch MyHP App
                2. Click onPrinter Device section.
                3. Tap on scan tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to scan. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.click(i_const.HOME_TILES.TILE_SCAN)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.click(i_const.HOME_TILES.TILE_SCAN)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_02_verify_print_documents_tile(self):
        """
        Description: C52905565
                1. Launch MyHP App
                2. Click onPrinter Device section.
                3. Tap on Print Documents tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to Print Documents. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.click(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.click(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_03_verify_camera_scan_tile(self):
        """
        Description: C52905566
                1. Launch MyHP App
                2. Click onPrinter Device section.
                3. Tap on Camera Scan tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to Camera Scan. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.click(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.click(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_04_verify_print_photo_tile(self):
        """
        Description: C52905567
                1. Install and launch the app
                2. Add a scan supported printer to the device list
                3. Tap on Print Photos tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to Print Photos. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_print_photos_tile", click_obj=True)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.scroll("_shared_print_photos_tile", click_obj=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_05_verify_copy_tile(self):
        """
        Description: C52905568
                1. Install and launch the app
                2. Add a scan supported printer to the device list
                3. Tap on copy tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to copy. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_06_verify_mobile_fax_tile(self):
        """
        Description: C52905569
                1. Install and launch the app
                2. Add a scan supported printer to the device list
                3. Tap on mobile fax tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to mobile fax. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_mobile_fax_tile", click_obj=True)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.scroll("_shared_mobile_fax_tile", click_obj=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_07_verify_shortcut_tile(self):
        """
        Description: C52905571
                1. Install and launch the app
                2. Add a scan supported printer to the device list
                3. Tap on shorcut tile in device details page
                4. Repeat step 1 and tap on each option one by one and verify
            Expected Result:
                3. verify value prop screen is displayed related to shorcut. This value prop has three options Create Account, Sign In and Back.
                4. User is able to successfully create account or sign in. Once user signs in, they will be directed to the next screen in the flow. If user taps Back, user is directed to the device details screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.printers.verify_back_arrow_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.select_navigate_back()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()

    def test_08_verify_printables_tile(self):
        """
        Description: C44019432
                1. Install and launch the app
                2. Add a printer and Tap on Printer and navigate to Device Details page.
                3. Tap on Printables tile and Observe
                4. Tap on back arrow on Printables page.
            Expected Result:
                3. Verify the user is not asked to sign in and is directed to Printables page directly. 
                4. Verify user is directed back to Device details page.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_printables_tile", click_obj=True)
        self.app_settings.select_navigate_back()
        self.home.verify_device_details_page()

    def test_09_verify_print_dashboard_tile(self):
        """
        Description: C52905572
                1. Install and launch the app
                2. Add a printer and Tap on Printer and navigate to Device Details page.
                3. Tap on Print Dashboard tile and Observe
                4. Tap on Cancel.
            Expected Result:
                3. Verify login screen is displayed.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_print_dashboard_tile", click_obj=True)
        self.home.select_cancel()
        self.home.verify_device_details_page()