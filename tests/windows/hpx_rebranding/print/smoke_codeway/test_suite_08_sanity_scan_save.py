import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_08_Sanity_Scan_Save(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_check_scan_save_flyout_default_type_C43738465(self):
        """
        Check default file type in Save flyout, verify default file type is correct
        Verify the "Image(*.jpg)" is selected as default file type if the files are recognized as photo.
        Verify the "Basic PDF" is selected as default file type if the files are recognized as document.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738465
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=60)
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()

        if "Photo_" in self.fc.fd["scan"].get_current_file_name():
            self.fc.fd["scan"].verify_file_type("jpg")
        else:
            self.fc.fd["scan"].verify_file_type("pdf")