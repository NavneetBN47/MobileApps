import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_05_Print_Photos:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]

    def test_01_verify_print_photos_tile_without_printer(self):
        """
         Description: C50698966
            Verify Print Photo tile when no printer added in the carousel.
                Install and launch app.
                Go through the consents, sign in and navigate to Home screen.
                Tap on Print Photos tile.
                Tap Cancel on Limited Access message screen.
        """
        self.fc.go_home(button_index=1, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.verify_limited_access_screen()
        self.home.select_cancel()
        self.home.verify_home()

    def test_02_verify_print_photos_tile_with_printer(self):
        """
         Description: C50698967
            Verify Print Photo tile when printer is added in the carousel.
                Install and launch app.
                Go through the consents, sign in and navigate to Home screen.
                Add a printer to the carousel.
                Tap on Print Photos tile.
                Tap on Allow access to all photos on pop up.
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.verify_home()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup(allow_access=True)

    @pytest.mark.parametrize("paper_size", ["a4", "letter", "4_6_in", "5_7_in", "legal"])
    def test_03_verify_printing_from_different_paper_size(self, paper_size):
        """
        Description: C50698989
            Tap Tile Print Photos.
                Launch the HP Smart app
                Tap on Print Photos and select any file/files to print and proceed to landing page.
                On the Preview landing page, tap on 'Print'
                Again tap on Print and submit a print job
                        """
        paper_size_types = {
            "a4": self.common_preview.PAPER_SIZE_A4,
            "letter": self.common_preview.PAPER_SIZE_LETTER,
            "4_6_in": self.common_preview.PAPER_SIZE_4x6,
            "5_7_in": self.common_preview.PAPER_SIZE_5x7,
            "legal": self.common_preview.PAPER_SIZE_LEGAL
        }
        if pytest.platform == "MAC":
            paper_size_types["8_10_in"] = self.common_preview.PAPER_SIZE_8x10
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next()
        self.common_preview.go_to_print_preview_pan_view()
        self.common_preview.select_paper_size_dropdown()
        self.common_preview.verify_paper_screen()
        if self.common_preview.verify_paper_size_option(paper_size_types[paper_size], invisible=True, raise_e=False):
            pytest.skip("currently printer doesn't support currently paper size {}".format(paper_size))
        self.common_preview.select_paper_size_option(paper_size_types[paper_size])
        self.common_preview.select_navigate_back(index=1)
        self.common_preview.verify_button(self.common_preview.PRINT_BTN)
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        self.common_preview.verify_job_sent_and_reprint_buttons_on_print_preview()

    def test_04_verify_orientation_setting_landscape(self):
        """
        Descriptions: C50698987
            Verify Orientation setting - Landscape
        Steps:  
            Launch HP Smart app & navigate to homescreen
            Tap on View & Print -> select a file
            Navigate to Print Preview screen
            Set Orientation to "Landscape"
            Proceed with printing

        Expected Result:
            Verify the preview and output are in Landscape
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_photo_by_index()
        self.photos.select_next_button()
        self.common_preview.verify_retrieving_page_size_popup(timeout=5, raise_e=False)
        self.common_preview.verify_dynamic_studio_screen(timeout=15)
        self.common_preview.verify_cards_options(invisible=True)
        self.common_preview.verify_paper_main_tray_option(timeout=15)
        self.common_preview.verify_paper_photo_tray_option(raise_e=False)
        self.common_preview.select_printer_title(self.printer_name)
        self.common_preview.verify_select_printer_screen()
        self.common_preview.select_close()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_ds_layout_btn()
        self.common_preview.verify_layout_options()
        self.common_preview.verify_info_btn()
        self.common_preview.select_info_btn()
        self.common_preview.dismiss_tooltip(raise_e=True)
        self.common_preview.select_ds_paper_btn()
        self.common_preview.select_landscape_orientation_button()
        self.common_preview.select_undo_btn()
        self.common_preview.select_potrait_orientation_button()
        self.common_preview.select_redo_btn()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_preview_btn()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
        self.common_preview.select_navigate_back()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_navigate_back()
        self.common_preview.verify_exit_without_saving_popup()
        self.common_preview.select_no()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_navigate_back()
        self.common_preview.select_yes()
        self.photos.verify_multi_selected_photos_screen()