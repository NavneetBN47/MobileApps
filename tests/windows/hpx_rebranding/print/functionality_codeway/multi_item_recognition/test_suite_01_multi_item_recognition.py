import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")

class Test_Suite_01_Multi_Item(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.scan = cls.fc.fd["scan"]
        cls.p = load_printers_session
        cls.fc.add_a_printer(cls.p)
        cls.printer_name = cls.p.get_printer_information()["model name"]

    @pytest.mark.regression
    def test_01_verify_gallery_view_screen_C43738519(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devicesDetailsMFE.click_scan_tile()
        self.scan.verify_scan_result_screen(), "Scan result screen is not visible"
        self.scan.click_scan_btn()
        assert self.scan.verify_adv_scan_preview_screen, "Advance preview screen is not visible"
        self.scan.click_add_pages_btn()
        self.scan.select_import_text()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.scan.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.scan.click_import_done_btn()
        assert self.scan.verify_adv_scan_preview_screen, "Advance preview screen is not visible"
        self.scan.click_add_pages_btn()
        self.scan.select_import_text()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.scan.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.scan.click_import_done_btn()
        assert self.scan.verify_adv_scan_preview_screen, "Advance preview screen is not visible"
        self.scan.click_add_pages_btn()
        self.scan.select_import_text()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.scan.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.scan.click_import_done_btn()
        assert self.scan.verify_preview_with_multi_image(3), "Scrollbar is not working"

    
 