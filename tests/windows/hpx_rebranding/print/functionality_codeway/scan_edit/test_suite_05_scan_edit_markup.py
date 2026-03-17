import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_05_Scan_Edit_Markup(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_scan_edit_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()

    @pytest.mark.regression
    def test_02_click_edit_Markup_button_c43738512(self):
        """
        Click on edit in the preview screen
        Click on 'Mark up' button.
        By default, 'Highlight[yellow] should be selected and outline should be displayed as selected.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738512
        """
        self.fc.fd["scan"].click_markup_item()
        self.fc.fd["scan"].verify_edit_makup_setting_screen()
        highlight = self.fc.fd["hpx_rebranding_common"].compare_image_diff("pen_group", folder_n="scan", image_n="markup_default.png")
        assert highlight < 0.02

    @pytest.mark.regression
    def test_03_add_some_markup_and_click_cancel_button_c49175384(self):
        """
        Add some markup in the image.
        Click on cancel button.
        Verify the dialogue UI.
        "Exit without saving?" confirmation dialogue box should be displayed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/49175384
        """
        self.fc.fd["scan"].click_red_pen_btn()
        self.fc.fd["scan"].click_center_image()
        self.fc.fd["scan"].click_edit_cancel_btn()
        self.fc.fd["scan"].verify_exit_without_saving_dialog_for_edit_screen()
        self.fc.fd["scan"].click_cancel_btn()
        self.fc.fd["scan"].verify_edit_makup_setting_screen()

    @pytest.mark.regression
    def test_04_add_some_markup_and_click_done_button_c43738513(self):
        """
        Add some markup in the image.
        Click on done button.
        Verify that changes are reflected in the image.
        All settings changes are saved and should be reflected in the image in Preview screen.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738513
        """
        self.fc.fd["scan"].click_edit_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
