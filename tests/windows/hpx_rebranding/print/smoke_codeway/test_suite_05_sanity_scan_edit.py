import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep

pytest.app_info = "HPX"
class Test_Suite_05_Sanity_Scan_Edit(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_click_edit_makeup_cancel_btn_C43738514(self):
        """
        Click Cancel button, verify a confirmation dialog shows

        Steps:
        1.Launch the HPx app.
        2.Click on the printer card.
        3.Click on the scan tile.
        4.Perform a scan job.
        5.Click on edit in the preview screen.
        6.Click on the 'Markup' button.
        7.Add some markup in the image.
        8.Click on cancel button.
        9.Verify the confirmation dialog.

        Expected:
        "Exit without saving?" confirmation dialog box should be displayed.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738514
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_markup_item()
        self.fc.fd["scan"].verify_edit_makup_setting_screen()
        self.fc.fd["scan"].edit_markup_item()
        self.fc.fd["scan"].click_center_image()
        self.fc.fd["scan"].click_edit_cancel_btn()
        self.fc.fd["scan"].verify_exit_without_saving_dialog_for_edit_screen()
        self.fc.fd["scan"].click_exit_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.smoke
    def test_02_click_edit_reset_crop_btn_C43738498(self):
        """
        Crop scanned page and click reset, verify original outline is restored

        Steps:
        1.Launch HPx app.
        2.Click on printer card.
        3.Click on scan tile.
        4.Perform scan job
        5.Click on edit in the preview screen
        6.Select any one of the crop size.
        7.Click on 'Reset Crop' button.

        Expected:
        'Custom' crop should be selected after clicking on reset crop button.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738498
        """
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_crop_item_btn('Letter')
        self.fc.fd["scan"].click_reset_crop_btn()
        custom = self.fc.fd["hpx_rebranding_common"].compare_image_diff("tool_navigation_menu", folder_n="scan", image_n="select_custom.png")
        assert custom < 0.05
        self.fc.fd["scan"].click_edit_cancel_btn()
        self.fc.fd["scan"].verify_scan_result_screen()