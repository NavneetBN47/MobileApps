import pytest
from time import sleep

from MobileApps.resources.const.ios.const import BUNDLE_ID
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.mac.smart.utility import smart_utilities

pytest.app_info = "SMART"


class Test_Suite_01_HP_Smart_Files(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.files = cls.fc.fd["files"]
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]
        if pytest.platform == "IOS":
            cls.ios_system = cls.fc.fd["ios_system"]
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        cls.fc.go_home(stack=cls.stack)
        cls.fc.dismiss_tap_here_to_start()
        cls.local_fpath = ma_misc.get_abs_path("/resources/test_data/documents/pdf/1page.pdf")
        cls.file_name = "1page.pdf"
        if pytest.platform == "IOS":
            cls.driver.push_file(BUNDLE_ID.FIREFOX, cls.local_fpath)
        def delete_file():
            if pytest.platform == "MAC":
                smart_utilities.delete_all_hp_smart_files(cls.driver.session_data["ssh"])
            else:
                cls.driver.delete_file(BUNDLE_ID.FIREFOX, cls.file_name)
        request.addfinalizer(delete_file)

    def test_01_all_files_recents_ui(self):
        """
        C27655028
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_all_files_image()
        self.files.select_and_verify_all_files()

    def test_02_browse_icloud_drive_folder(self):
        """
        C27655029- Verify the iCloud Drive screen
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.dismiss_tap_here_to_start()
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_my_photos_files_screen()
        self.files.select_all_files_image()
        self.files.select_browse_button()
        self.files.verify_hp_smart_screen_ui()
        self.files.verify_icloud_screen()
        self.files.verify_recent_button()
        self.files.verify_icloud_ui_elements_screen()
        self.files.select_close()
        self.files.verify_hp_smart_files_home_screen()

    def test_03_only_pdf_available_to_select(self):
        """
        The test case depends on pdf file pushed to phone in load_file_to_phone
        C31297712 - Verify only PDFs available to select
        C31297714 - Verify PDF available under browse folder
        """
        if pytest.platform == "IOS":
            self.ios_system.dismiss_hp_local_network_alert(timeout=10)
        else:
            smart_utilities.create_hp_smart_file(self.driver.session_data["ssh"], file_name=self.file_name,
                                                 create_new_file=False, file_path=self.local_fpath)
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_rootbar_view_and_print_icon()
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_view_and_print_screen()
        self.files.select_all_files_image()
        if pytest.platform == "IOS":
            if not self.files.verify_item_cell("1page"):
                self.files.navigate_to_application_folder_or_go_back("Firefox")
            self.files.select_item_cell("1page")
        else:
            self.files.verify_item_cell(self.file_name)
            self.files.select_item_cell(self.file_name)
        if pytest.platform == "IOS":
            self.common_preview.verify_preview_screen()
        else:
            self.files.verify_file_selected(self.file_name)