import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import random
from time import sleep
import logging


pytest.app_info = "HPX"
class Test_Suite_01_Scan_Edit_Crop(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_scanner_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_02_select_source_and_edit_c43738493(self):
        """
        Perform 1 or more scan jobs
        click on edit icon.
        Edit screen should be displayed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738493
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            set_source = random.choice([self.fc.fd["scan"].ADF, self.fc.fd["scan"].GLASS])
            logging.info("Scanner Source: {}".format(set_source))
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, set_source)
        
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(timeout=180)
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()

    @pytest.mark.regression
    def test_03_check_custom_crop_is_default_c43738496(self):
        """
        "Custom" crop should be selected by default.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738496
        """
        custom = self.fc.fd["hpx_rebranding_common"].compare_image_diff("tool_navigation_menu", folder_n="scan", image_n="select_custom.png")
        assert custom < 0.02

    @pytest.mark.regression
    def test_04_perform_all_crop_size_c43738497(self):
        """
        Perform all the crop size one by one
        Verify the crop border changes according to the crop size's.
        The crop border should be clearly visible and accurately reflect the selected crop area.(not covered)

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738497
        """
        crop_list = ['Custom', 'Letter', 'Square', 'A4', '5:7', '4:6', '3.5:5']
        for crop in crop_list:
            self.fc.fd["scan"].click_crop_item_btn(crop)
            sleep(1)
