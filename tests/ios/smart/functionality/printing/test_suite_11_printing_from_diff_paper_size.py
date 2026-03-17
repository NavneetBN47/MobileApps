import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_08_Printing_From_Diff_Paper_Size(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.p = load_printers_session

        # Define flows
        cls.photos = cls.fc.fd["photos"]
        cls.home = cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]

    @pytest.mark.parametrize("paper_size", ["a4", "letter", "4_6_in", "5_7_in", "legal"])
    def test_01_verify_printing_from_different_paper_size(self, paper_size):
        """
        IOS & MAC:
        Descriptions: C31297406, C31297407, C31297408, C31297410, C31297411, C31297388, C34347729, C31297412
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, click on View and Print button on bottom navigation
         4. Click on Albums -> Recents folder
         5. Select a photo from Recents folder screen
         6. Click on Print Preview button
         7. Select the paper size according to the testing requirements
         8. Click on Print button

        Expected Result:
         8. Verify printing job successfully
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