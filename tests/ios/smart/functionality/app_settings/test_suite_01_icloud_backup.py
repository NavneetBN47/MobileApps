import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.mac.smart.utility import smart_utilities


pytest.app_info = "SMART"

class Test_Suite_01_iCloud_Backup(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.files = cls.fc.fd["files"]
        cls.camera = cls.fc.fd["camera"]
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack)

    def test_03_do_not_disable_sync(self):
        """
        IOS & MAC:
        C33408329 - iOS only- Verify Back up to iCloud option
        C37535669 - verify 'Do not disable sync' option
        """
        self.home.select_app_settings()
        self.app_settings.select_backup_to_icloud_cell()
        self.app_settings.verify_backup_to_icloud_ui()
        if pytest.platform == "IOS":
            self.app_settings.toggle_switch("backup_icloud_switch", True, False)
        else:
            self.app_settings.toggle_switch("backup_icloud_switch")
        self.app_settings.verify_icloud_sync_popup()
        self.app_settings.select_do_not_disable_sync()
        self.app_settings.verify_backup_to_icloud_ui()
        assert self.driver.get_attribute("backup_icloud_switch", "value") == "1"

    def test_04_delete_from_iphone(self):
        """
        IOS & MAC:
        C37535670 - verify 'Delete from my iPhone' option
        """
        file_name = self.test_04_delete_from_iphone.__name__
        self.generate_test_image(file_name)
        self.fc.go_to_home_screen()
        self.home.select_app_settings()
        self.app_settings.select_backup_to_icloud_cell()
        self.app_settings.verify_backup_to_icloud_ui()
        if pytest.platform == "IOS":
            self.app_settings.toggle_switch("backup_icloud_switch", True)
        else:
            self.app_settings.toggle_switch("backup_icloud_switch")
        self.app_settings.verify_icloud_sync_popup()
        self.app_settings.select_delete_documents()
        self.app_settings.verify_backup_to_icloud_ui()
        self.fc.go_hp_smart_files_screen_from_home()
        assert self.files.is_empty_screen()

    def test_05_keep_on_iphone(self):
        """
        IOS & MAC:
        C37535668 - verify 'Keep on my iPhone' option
        """
        file_name = self.test_05_keep_on_iphone.__name__
        self.generate_test_image(file_name)
        self.fc.go_to_home_screen()
        self.home.select_app_settings()
        self.app_settings.select_backup_to_icloud_cell()
        self.app_settings.verify_backup_to_icloud_ui()
        if pytest.platform == "IOS":
            self.app_settings.toggle_switch("backup_icloud_switch", True)
        else:
            self.app_settings.toggle_switch("backup_icloud_switch")
        self.app_settings.verify_icloud_sync_popup()
        self.app_settings.select_keep_documents()
        self.app_settings.verify_backup_to_icloud_ui()
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists("{}.jpg".format(file_name))

    def generate_test_image(self, file_name: str):
        if pytest.platform == "MAC":
            smart_utilities.create_hp_smart_file(self.driver.session_data["ssh"], f"{file_name}.jpg")
        else:
            self.fc.go_camera_screen_from_home(tile=True)
            self.camera.verify_camera_btn()
            self.fc.multiple_manual_camera_capture(1)
            self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.common_preview.SHARE_SAVE_TITLE)
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists("{}.jpg".format(file_name))