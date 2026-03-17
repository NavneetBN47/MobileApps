import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES

pytest.app_info = "SMART"


class Test_Suite_01_Files_Photos(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Defines flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    @pytest.mark.parametrize("from_source", ["photos_tile", "doc_tiles", "view_print_nav"])
    def test_01_files_photos_screen_via(self, from_source):
        """
        Description: C31297222
            1/ Load Home screen with user onboarding account
            2/ Click on Print Photos/Print Documents/View & Print nav button

        Expected Result:
            2/ Files and Photos screen
                - title
                - header
                - PDFs and My Photos
                - Facebook with "Log in" as sub text
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        if from_source in ["photos_tile", "doc_tiles"]:
            tile_name = self.driver.return_str_id_value(TILE_NAMES.PRINT_PHOTOS if from_source == "photos_tile"
                                                        else TILE_NAMES.PRINT_DOCUMENTS)
            self.home.select_tile_by_name(tile_name)
        else:
            self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        if from_source == "photos_tile":
            self.local_photos.verify_photo_picker_optional_screen(raise_e=False)
        else:
            self.files_photos.verify_files_photos_screen()
            self.files_photos.verify_local_files_photos_btns()