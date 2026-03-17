import pytest

from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_03_Nav_Pane_Pin_HP_Smart(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.sp = cls.sf.sp

        cls.home = cls.fc.fd["home"]
        cls.pin_to_start = cls.fc.fd["pin_to_start"]

    def test_01_check_pin_hp_smart_to_start(self):
        """
        (+) Go to Settings > Pin HP Smart/OEM(Samsung Inkjet Printers..) > click Pin to Start, verify HP Smart is added to Start screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721541
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_pin_hp_smart_to_start_listview()
        self.pin_to_start.verify_pin_hp_smart_to_start_screen()

        self.pin_to_start.click_pin_to_start_btn()
        self.pin_to_start.verify_do_you_want_to_pin_dialog()
        self.pin_to_start.select_do_you_want_to_pin_dialog_no_btn()
        self.pin_to_start.verify_pin_hp_smart_to_start_screen()
        assert self.pin_to_start.verify_pin_to_start_btn_enabled() is True

        self.pin_to_start.click_pin_to_start_btn()
        self.pin_to_start.verify_do_you_want_to_pin_dialog()
        self.pin_to_start.select_do_you_want_to_pin_dialog_yes_btn()
        self.pin_to_start.verify_pin_hp_smart_to_start_screen()
        assert self.pin_to_start.verify_pin_to_start_btn_enabled() is False

    def test_02_check_app_is_already_pinned(self):
        """
        Go back to Settings > Pin HP Smart to Start, verify red error message 'App is already pinned'

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721542
        """
        self.pin_to_start.select_pin_hp_smart_to_start_back_btn()
        self.home.verify_home_screen()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_pin_hp_smart_to_start_listview()
        self.pin_to_start.verify_pin_hp_smart_to_start_screen(is_pinned=True)

        self.sp.extend_win_start_list()
        self.sp.verify_win_start_display()
        self.sp.verify_hp_smart_pin_to_start()
        self.sp.unextend_win_start_list()


