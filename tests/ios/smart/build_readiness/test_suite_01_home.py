import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Home:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.files = cls.fc.fd["files"]
        cls.printables = cls.fc.fd["printables"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.scan = cls.fc.fd["scan"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]
        cls.p = load_printers_session

    def test_01_verify_copy_tile(self):
        """
        Description:C50698972
            Verify Copy tile behavior
                1.Install and launch app.
                2. Go through the consents, sign in and navigate to Home screen.
                3. Add a printer to the carousel.
                4. Tap on Copy tile.
                5. Allow access to camera.
        Expected Result:
            Verify the user is directed to camera screen..
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_copy_screen_from_home()

    def test_02_verify_shortcut_tile(self):
        """
        Description: C50698973
            Verify the Shortcut tile behavior.
                Install and launch app.
                Go through the consents, sign in and navigate to Home screen.
                Tap on Shortcuts tile.
            Expected Result:
                Verify the Shortcuts screen opens.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.navigate_to_shortcuts_screen()

    def test_03_verify_camera_scan_tile(self):
        """
        Description:C50698971
            Verify Camera Scan tile behavior.
                Fresh install and launch app.
                Go through the consents, sign in and navigate to Home screen.
                Add a printer to the carousel.
                Tap on Camera Scan tile.
        Expected Result:
            Allow access to camera..
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(self.p)

    def test_04_printable_tile(self):
        '''
        Description:C50698974
            Printables tile redirection
                Install and launch app.
                Go through the consents, and navigate to Home screen.
                Tap on Printables tile.
                Go back to Home screen and sign in.
                Tap on Printables tile.
        Expected Result:
            Step 3: Verify user is directed to Printables webpage.
            Step 5: Verify user is redirected to Printables webpage.
        '''
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_app_settings()
        self.app_settings.select_sign_out_btn()
        self.app_settings.dismiss_sign_out_popup()
        self.fc.go_to_home_screen()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PLAY_LEARN)
        self.printables.verify_printables_title()
        self.printables.select_back()
        self.home.select_app_settings()
        self.app_settings.select_sign_in_option()
        self.hpid.login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
        self.app_settings.verify_successfull_sign_in_screen()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PLAY_LEARN)
        self.printables.verify_printables_title()

    def test_05_verify_printer_scan_tile(self):
        """
        Description:C50698970
            Verify Printer Scan tile behavior
                Install and launch app.
                Go through the consents, sign in and navigate to Home screen.
                Add a printer to the carousel.
                Tap on Printer Scan tile.
                Allow access to camera.
        Expected Result:
            Verify the Camera screen opens.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SCAN)
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_scanner_screen()

    def test_06_verify_print_documents_tile(self):
        """
         Description:C50698968 
         Verify Print Documents tile behavior
            Install and launch app.
            Go through the consents, sign in and navigate to Home screen.
            Add a printer to the carousel.
            Tap on Print Documents tile.
            Allow access to photos on pop up.
        Expected Result:
            On iOS- Verify the View & Print screen shows.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.photos.verify_select_photos_btn()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.files.verify_view_and_print_screen()
    
    def test_07_app_settings_signed_in(self):
        """
        Description:C50699001 
        Verify App Settings UI (signed in)
            Install and launch app.
            Click on App Settings from bottom bar of Home screen.
            Click on 'Sign in'
            Type account name and pwd
        Expected Result:
            Title - 'HP Smart'
            Icon with User initials is displayed
            Sign Out button
            Account information
            Manage HP Account button

        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack) # clicking skip button heres
        self.home.select_settings_icon()
        self.app_settings.verify_app_settings_screen()
        self.app_settings.select_sign_in_option()
        self.hpid.login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
        self.app_settings.verify_successfull_sign_in_screen()
        self.app_settings.select_my_hp_account()

    def test_08_app_settings_unsigned_in(self):
        """
        Description:C50698975 
        Verify App Setting UI with HP account signed in and out
            1. Click on App Settings from Home screen
            2. Click on Sign In button
            3. Type account name and pwd
            4. Click on Sign Out button
            5. Click on Sign Out button on the pop up message
        Expected Result:
            Verify user is signed out successfully.
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_app_settings()
        self.app_settings.select_sign_in_option()
        self.hpid.login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
        self.app_settings.verify_successfull_sign_in_screen()
        self.app_settings.select_sign_out_btn()
        self.app_settings.dismiss_sign_out_popup(signout=False)
        self.app_settings.verify_app_settings_screen()