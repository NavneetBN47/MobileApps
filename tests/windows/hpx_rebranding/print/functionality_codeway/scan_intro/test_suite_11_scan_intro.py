import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_11_Scan_Intro_Document_Feeder(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
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
    def test_01_run_scan_with_document_feeder_C43738432(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devicesDetailsMFE.verify_scan_tile(), "Scan tile is not visible"
        self.devicesDetailsMFE.click_scan_tile()
        self.scan.select_source_dropdown()
        assert self.scan.verify_source_list_items(), "source items are not present"
        self.scan.select_source_document_feeder()
        self.scan.select_import_text()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.scan.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.scan.click_import_done_btn()
        assert self.scan.verify_scan_result_screen(), "scanner page result not shown up"
        self.scan.click_save_btn()
        self.scan.click_dialog_save_btn()
        self.scan.click_save_as_dialog_save_btn()
        assert self.scan.verify_file_saved_dialog(), "File saved Dialog box is not visible"
 