from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_06_Preview_ID_Card(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.cpreview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    @pytest.mark.parametrize("option", ["scan", "add", "home", "cancel"])
    def test_01_exit_id_card_preview(self, option):
        """
        Description: C31299327, C31299328, C31299329 & C31299330
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan on bottom navbar
         3. Select ID Card Mode
         4. Select shutter button twice to capture ID front and back
         6. Select next button
         7. Select next button
         8. Tap on back(<-) button
         9. Select button based on option param
          - "scan" == "Yes, Start New Scan" button
          - "add_images" == "No, Add Images" button
          - "home" == "Yes, Go Home" button
          - "cancel" == "Cancel" button
        Expected Results:
         9. Verify based on option param
          - "scan" == Verify ID Front message
          - "add_images" == Verify ID Front message
          - "home" == Verify Home screen
          - "cancel" == Verify preview screen
        """
        self.__load_id_scan()
        self.fc.select_back()
        self.cpreview.select_exit_popup_btn(option)
        if option == "scan" or option == "add":
            self.scan.verify_bubble_msg("id_front")
        elif option == "home":
            self.home.verify_home_nav()
        else:
            self.cpreview.verify_preview_screen()

    @pytest.mark.parametrize("option", ["share", "save"])
    def test_02_id_card_page_size(self, option):
        """
        Description: C31299325 & C31299326
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan on bottom navbar
         3. Select ID Card Mode
         4. Select shutter button twice to capture ID front and back
         6. Select next button
         7. Select next button
         8. Select button based on option param
          - "share" == share button on preview bottom nav
          - "save" == save button on preview bottom nav
         9. Select File Type Basic PDF
        Expected Results:
         9. Verify selected Document size is 4x6
        """
        self.__load_id_scan()
        self.cpreview.select_bottom_nav_btn(self.cpreview.SAVE_BTN if option == "save" else self.cpreview.SHARE_BTN)
        self.cpreview.select_file_type(self.cpreview.BASIC_PDF)
        self.cpreview.verify_document_size(selected_size=self.cpreview.DOCUMENT_SIZE_4x6)

    def __load_id_scan(self):
        """Loads smart app and captures an id, ends at preview screen"""
        self.fc.flow_load_home_screen(verify_signin=True)
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT, mode="id_card")
        self.scan.verify_id_preview_screen("front")
        self.scan.select_id_next_btn()
        self.scan.verify_id_preview_screen("back")
        self.scan.select_id_next_btn()
        self.cpreview.verify_preview_screen()