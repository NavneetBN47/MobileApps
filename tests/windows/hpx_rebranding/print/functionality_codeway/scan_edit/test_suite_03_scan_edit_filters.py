import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
import logging


pytest.app_info = "HPX"
class Test_Suite_03_Scan_Edit_Filters(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_scan_edit_filters_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        Select the filter
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_scan_tile()
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)      
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        sleep(2)
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_filters_item()
        self.fc.fd["scan"].verify_edit_filters_screen()

    @pytest.mark.regression
    def test_02_check_undo_and_redo_button_c43738507(self):
        """
        Click on undo/redo icon.
        The filter should be applied correctly, and the scanned page should reflect the changes.
        Clicking the "Undo" icon should remove the filter and restore the scanned page to its previous state with
        the original outline.
        Clicking the "Redo" icon should reapply the filter and change the scanned page accordingly, while
        maintaining the selected outline.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738507
        """
        self.fc.fd["hpx_rebranding_common"].save_image("canvas_image", folder_n=None, image_n="filter_org.png")

        self.fc.fd["scan"].click_dynamic_text_item('Alabaster')
        self.fc.fd["hpx_rebranding_common"].save_image("canvas_image", folder_n=None, image_n="filter_ala.png")
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", folder_n=None, image_n="filter_org.png")
        assert com_org > 0.03
        sleep(1)
        self.fc.fd["scan"].click_dynamic_text_item('Summer')
        self.fc.fd["hpx_rebranding_common"].save_image("canvas_image", folder_n=None, image_n="filter_sum.png")
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", folder_n=None, image_n="filter_org.png")
        assert com_org > 0.03

        self.fc.fd["scan"].click_undo_btn()
        com_ala = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", folder_n=None, image_n="filter_ala.png")
        assert com_ala < 0.02
        self.fc.fd["scan"].click_redo_btn()
        com_sum = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", folder_n=None, image_n="filter_sum.png")
        assert com_sum < 0.02

    @pytest.mark.regression
    def test_03_Increase_decrease_filter_intensity_c43738508(self):
        """
        Select the filter
        Increase/decrease the 'Filter Intensity'
        1.The 'filter intensity' or 'slider' should change according to the value set by the user.
        2.Slider should move from left to right.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738508
        """
        self.fc.fd["scan"].change_filter_intensity_vaule("20")
        self.fc.fd["scan"].change_filter_intensity_vaule("80")

    @pytest.mark.regression
    def test_04_click_reset_filters_button_c43738506(self):
        """
        Click on 'Rest Filters' button
        Image should be restored to the default setting.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738506
        """
        self.fc.fd["scan"].click_reset_filters_btn()
        assert self.fc.fd["scan"].verify_filter_intensity(raise_e=False) is False
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", folder_n=None, image_n="filter_org.png")
        assert com_org < 0.02
        
    @pytest.mark.regression
    def test_05_select_all_filters_c43738505(self):
        """
        Click on edit in the preview screen
        Click on 'Filters' button.
        Select all the filters one by one.
        Each filter setting should be applied correctly, and the filter should be reflected in the image.(not covered)
        The filters button outline should be displayed as selected.(not covered)

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738505
        """  
        filter_list = ['B/W', 'B/W 2', 'Greyscale', 'Alabaster','Summer', 'Aurora', 'Ultraviolet', 'Ink Stains', 'Dusk', 'Noir', 'Daydream', 'Embers', 'Moonlight', 'Snowshine', 'Atmoshperic', 'Honeybee', 'Fireside', 'Seafarer', 'Sauna', 'Glacial', 'Cameo', 'Timeworn', 'Sunlight']
        
        for filter in filter_list:
            logging.info(f"Applying filter: {filter}")
            if not self.fc.fd["scan"].verify_dynamic_text_item(filter, raise_e=False, timeout=2):
                self.fc.fd["scan"].swipe_filter_item(filter)
            self.fc.fd["scan"].click_dynamic_text_item(filter)
            self.fc.fd["scan"].verify_filter_intensity()
            if filter in ['Summer', 'Aurora', 'Ultraviolet']:
                value = "50"
            else:
                value = "100"
            self.fc.fd["scan"].verify_filter_intensity_value(value)
