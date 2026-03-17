import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_15_Scan_Edit(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.sf = SystemFlow(cls.driver)
        cls.sp = cls.sf.sp
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_go_to_scan_preview_screen(self):
        """
        Go to Preview screen.
       
         """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

    def test_02_check_adjust_screen_settings(self):
        """
        Verify Brightness, Saturation, Contrast, Clarity, Exposure, Shadows, Highlights, and Whites sliders 
        all set to default value, 0
        Verify outline displayed as selected
        Click on Adjust and slide the blue icon for Brightness, Saturation, Contrast, Clarity,
        Exposure, Shadows, Highlights, and Whites.
        Click "Reset Adjust" on the adjust section./Click undo/redo icon (located to the up right of the Edit screen
        Verify the outline is restored to the original before modification
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28584892
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28584950
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28585133
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29595507
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13046625
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29595509

        """
        self.scan.click_menu_btn()
        self.scan.click_edit_btn()
        self.scan.verify_edit_screen()
        self.scan.click_crop_letter_btn()
        self.scan.click_reset_crop_btn()
        self.scan.verify_keep_resolution_box_behavior("unchecked")
        self.scan.click_crop_letter_btn()
        self.scan.select_keep_resolution_box()
        self.gotham_utility.click_minimize()
        time.sleep(2)
        assert "HP.Smart" in self.driver.ssh.send_command('Get-Process -Name "*HP.Smart*"')["stdout"]
        # self.driver.launch_app()
        self.sp.click_hp_smart_taskbar()
        time.sleep(3)
        self.scan.verify_keep_resolution_box_behavior("checked")
        self.scan.click_adjust_item()
        self.scan.verify_adjust_setting_default_value()
        self.scan.change_adjust_contrast_edit_vaule("50")
        self.scan.click_reset_adjust_btn()
        self.scan.verify_adjust_contrast_edit_default_value()
        self.scan.change_adjust_contrast_edit_vaule("50")
        self.scan.click_undo_btn()
        self.scan.verify_adjust_contrast_edit_default_value()

    def test_03_check_filters_screen_settings(self):
        """
        Check the Filters setting.
        Click on each Filter under "Document" and "Photo" section and check the outline.
        Click "Reset Filters" on the Filters section.
        Verify the outline is restored to the original before modification
        Verify the "Filter Intensity" slider bar doesn't show
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28585152
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28585153
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28585155
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29595508

        """
        self.scan.click_filters_item()
        self.scan.verify_edit_filters_screen()
        self.scan.verify_slider_adjected_to_100_for_doc_value()
        self.scan.verify_slider_adjected_to_50_for_photo_value()
        self.scan.click_reset_filters_btn()
        self.scan.verify_filter_intensity_does_not_show()
        self.scan.verify_slider_adjected_to_100_for_doc_value()
        self.scan.click_undo_btn()
        self.scan.verify_filter_intensity_does_not_show()
        self.scan.click_filters_bw_btn()
        self.gotham_utility.click_minimize()
        time.sleep(2)
        # self.driver.launch_app()
        self.sp.click_hp_smart_taskbar()
        time.sleep(3)
        self.scan.verify_filter_intensity_value_is_100()

    def test_04_check_text_screen_settings(self):
        """
        Check the Text setting
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28585151(some pic can not check)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29596150
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30229956
        """
        self.scan.click_text_item()
        self.scan.verify_edit_text_setting_screen()
        self.gotham_utility.click_minimize()
        time.sleep(2)
        # self.driver.launch_app()
        self.sp.click_hp_smart_taskbar()
        time.sleep(3)
        self.scan.verify_edit_text_setting_screen()

    def test_05_check_markup_screen_settings(self):
        """
        Check the Markup setting
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30229955(color can not check)

        """
        self.scan.click_markup_item()
        self.scan.verify_edit_makup_setting_screen()

    def test_06_check_print_file(self):
        """
        Click Done button.
        Print the edited file.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13076841

        """
        self.scan.click_red_pen_btn()
        self.scan.click_done_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_print_btn()
        if self.scan.verify_hp_smart_printing_dialog(raise_e=False):
            self.scan.click_hp_printing_print_btn()
        self.scan.verify_scan_result_screen()
