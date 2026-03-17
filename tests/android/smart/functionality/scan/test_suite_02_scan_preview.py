from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Scan_Preview(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]

        # Define variables
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_scan_after_preview(self):
        """
        Description: C31299815, C31299814
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Preview button
            3/ Change Paper Size to another size, then click on Scan button
        Expected Result:
            Verify:
              2/ Preview job is successful
              3/ Scan job is successful. Next screen is Landing Page
        """
        self.fc.flow_home_load_scan_screen(self.p, from_tile=False)
        self.scan.select_preview()
        self.scan.verify_successful_scan_job()
        self.scan.verify_place_content_txt(invisible=True)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()

    def test_02_scan_preview_back_from(self):
        """
        Description: C31299845, C31299846, C31299853, C31299814, C31299817, C31299826
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Preview button
            3/ Press on Back button of mobile device
            4/ Load Scan screen via icon button on Home screen
            5/ Click on Scan button
            6/ At Landing Page, click on Add icon button
            7/ Click on Preview button
            8/ Press on Back button of mobile device
        Expected Result:
            Verify:
              3/ Home screen display
              8/ Landing Page screen.
        @param back_btn: back button. True: mobile back key, False: back button on Scan screen
        """
        self.fc.flow_home_load_scan_screen(self.p, from_tile=False)
        self.scan.select_preview(wait=False)
        self.scan.verify_successful_scan_job()
        self.scan.select_exit_btn()
        self.home.verify_home_nav()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.select_preview(wait=False)
        self.scan.verify_successful_scan_job()
        self.scan.verify_place_content_txt(invisible=True)
        self.driver.press_key_back()
        self.preview.verify_preview_screen()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)