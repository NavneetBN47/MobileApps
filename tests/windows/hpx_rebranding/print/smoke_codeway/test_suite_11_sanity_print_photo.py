import pytest
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_11_Sanity_Print_Photo(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_check_print_photos_C44256233_C44258706(self):
        """
        Verify the display of "Print photos" tile in printer device page.
        Verify the functionality of "Print Photos" tile, when user clicks on print button in driver window screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44256233
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258706
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["print"].verify_simple_print_dialog()
        # self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()