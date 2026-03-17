import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_01_Scan_Share_Flyout(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_scan_share_flyout_C43738689(self):
        """
        Share flyout UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738689
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=60)
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()

    @pytest.mark.regression
    def test_02_check_default_file_type_C43738691(self):
        """
        Check default file type in Share flyout, verify default file type is correct

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738691
        """
        if "Photo_" in self.fc.fd["scan"].get_current_file_name():
            self.fc.fd["scan"].verify_file_type("jpg")
        else:
            self.fc.fd["scan"].verify_file_type("pdf")

    @pytest.mark.regression
    def test_03_click_share_flyout_cancel_btn_C43738710(self):
        """
        Click "Cancel" button on Share flyout, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738710
        """
        self.fc.fd["scan"].click_dialog_cancel_btn()
        self.fc.fd["scan"].verify_share_dialog(invisible=True)

    @pytest.mark.regression
    def test_04_click_share_flyout_save_btn_C43738711(self):
        """
        Click "Share" button on Share flyout, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738711
        """
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.fc.fd["scan"].click_dialog_share_btn()
        self.fc.fd["scan"].verify_share_picker_popup()
        self.fc.fd["scan"].dismiss_share_picker_popup()
        self.fc.fd["scan"].verify_share_picker_popup(invisible=True)
