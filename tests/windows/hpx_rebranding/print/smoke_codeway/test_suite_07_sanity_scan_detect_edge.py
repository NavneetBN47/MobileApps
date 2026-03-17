import pytest
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep

pytest.app_info = "HPX"
class Test_Suite_07_Sanity_Scan_Detect_Edge(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_verify_auto_opt_is_default_selected_C43738448(self):
        """
        Check the default setting for Detect Edges, verify "Auto" is the default 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738448
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["scan"].verify_import_screen()

        auto_opt_select = self.fc.fd["hpx_rebranding_common"].compare_image_diff("import_screen_auto_group", folder_n="scan", image_n="select_auto.png")
        assert auto_opt_select < 0.05

    @pytest.mark.smoke
    def test_02_switch_to_full_opt_C43738449(self):
        """
        Switch to "Full" from "Auto", verify outline detected to full image 	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738449
        """
        self.fc.fd["scan"].click_import_full_option()
        full_opt_select = self.fc.fd["hpx_rebranding_common"].compare_image_diff("import_screen_full_group", folder_n="scan", image_n="select_full.png")
        assert full_opt_select < 0.05

    @pytest.mark.smoke
    def test_03_click_done_btn_on_detect_edge_screen_C43738453(self):
        """
        Click "Done" on the Detect Edges screen, verify Preview screen displays with image 
 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738453
        """
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

