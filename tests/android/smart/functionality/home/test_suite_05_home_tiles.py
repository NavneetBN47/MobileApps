from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest


pytest.app_info = "SMART"

class Test_Suite_05_Home_Tiles(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.bonjour_name = cls.printer_info['bonjour name']

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.help_support = cls.fc.flow[FLOW_NAMES.HELP_SUPPORT]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    @pytest.mark.capture_screen
    def test_01_print_photos(self):
        """
        Description: C31297210, C31297249, C35021993
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Print Photos tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Print Photos tile on Home screen
         5. Press back botton or Cancel button to get back Home screen
         6. Add a printer to carousel
         7. Click on Print Photo tile

        Expected Result:
         4. Verify Print Photos screen
         7. Verify My Photo screen
        """
        # Add reset function to here to avoid the tests get affected by previous test suite. because this test suite require no printer selected
        self.fc.reset_app()
        self.__load_tile_screen(tile_name=TILE_NAMES.PRINT_PHOTOS)
        self.file_photos.verify_limited_access_popup()
        self.file_photos.select_continue_btn()
        if self.local_photos.verify_photo_picker_optional_screen(raise_e=False):
            self.local_photos.select_cancel_btn()
        else:
            self.driver.press_key_back()
        self.home.verify_home_nav()
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.dismiss_print_anywhere_popup()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        if not self.local_photos.verify_photo_picker_optional_screen(raise_e=False):
            self.local_photos.verify_select_photo_screen(raise_e=False)

    def test_02_print_docs(self):
        """
        Description: C31297211
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Printer Documents tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Printer Documents tile on Home screen
        Expected Result:
         4. Verify Files and Photos screen
        """
        # Add reset function to here to avoid the tests get affected by previous test suite. because this test suite require no printer selected
        self.fc.reset_app()
        self.__load_tile_screen(tile_name=TILE_NAMES.PRINT_DOCUMENTS)
        self.file_photos.verify_limited_access_popup()
        self.file_photos.select_continue_btn()
        self.file_photos.verify_files_photos_screen()

    def test_03_help_support(self):
        """
        Description: C31297212
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Get HP Help and Support tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Get HP Help and Support tile on Home screen
        Expected Result:
         4. Verify Get HP Help and Support screen
        """
        self.__load_tile_screen(tile_name=TILE_NAMES.HELP_SUPPORT)
        self.help_support.verify_gettting_to_know_hp_smart()

    @pytest.mark.capture_screen
    def test_04_camera_scan(self):
        """
        Description: C31297214, C35024196
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Camera Scan tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Camera Scan on Home screen
        Expected Result:
         4. Verify No Camera Access screen
        """
        self.__load_tile_screen(tile_name=TILE_NAMES.CAMERA_SCAN)
        self.scan.verify_no_camera_access_screen()

    def test_06_verify_printables_tile_direction(self):
        """
        Description: C31298234
        Steps:
            1. Launch the Smart app
            2. Click accept all button and do HPID log in to home screen
            3. Tap on Printables tile.

        Expected result:
            Step 3: Verify user is directed to Printables webpage.
        """
        self.__load_tile_screen(tile_name=TILE_NAMES.PRINTABLES)
        self.home.verify_printable_sign_in_screen(timeout=20)

    def test_07_verify_ui_and_home_screen_tiles_for_first_launch(self):
        """
        Description: C31298222, C31298225, C31297207, C31297206
        Steps:
            1. Launch the Smart app
            2. Click accept all button and skip HPID log in to home screen
            3. Add any Mobile Fax supported printer on the carousal.

        Expected result:
            2. Verify that only the following tiles are shown:
               - Instant Ink/Get Supplies
               - Printables
               - Shortcuts
               - Mobile Fax - will not be shown
               - Print Photos
               - Print Documents
               - Camera Scan
            Help & Support
            Printer Scan
            Copy
            Verify personalize tile button on the home screen.

            For step 3, verify that the Mobile Fax tile will now be shown on the home screen.
            Tile order is as specified above. Verify personalize tile button on the home screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        assert self.home.get_tile_titles() == [
            'Get Supplies', 'Printables',
            'Shortcuts',
            'Camera Scan', 'Help & Support',
            'Print Photos', 'Print Documents',
            'Printer Scan', 'Copy'
        ]
        self.home.verify_personalize_tile_btn()
        # C31298225
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.dismiss_print_anywhere_popup()
        self.fc.flow_home_enable_softfax_tile()
        self.home.verify_personalize_tile_btn()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_tile_screen(self, tile_name=""):
        """
        If current screen is not Home screen, load to Home screen.
        If there is no connected printer, select a target printer
        If current tile is not enabled on Home screen, then:
           - Click on Personalize tile
           - Enable current tile
           - Select back button to Home screen
           - Click on the tile you need
        - params: tile_name from constant TILE_NAME in flow container
        """
        self.fc.flow_load_home_screen(verify_signin=True)
        if not self.home.verify_tile(self.home.get_text_from_str_id(tile_name), raise_e=False):
            self.home.select_personalize_tiles()
            self.personalize.toggle_tile_by_name(self.personalize.get_text_from_str_id(tile_name), on=True)
            self.personalize.select_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(tile_name))
