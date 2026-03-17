import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_10_Print_Quality_Tools_Error_Handing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_clean_printheads_with_door_open_C57706985_C57706986_C57706987(self):
        """
        The simulated printer information doesn't support door open action.
    
        Verify the "Door open" dialog pops up with "Retry" and "Cancel" button.
        Verify Clean Printheads job resumes after clicking retry btn when fix door open error.
        Verify the Clean Printheads job is canceled.
        Verify the dialog dismiss and the "Print Quality Tools" screen shows.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706985
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706986
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706987

        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_print_quality_tools()
        self.p.fake_action_door_open()
        self.fc.fd["printersettings"].click_clean_arrow()
        self.fc.fd["printersettings"].verify_door_open_dialog()
        self.p.fake_action_door_close()
        self.fc.fd["printersettings"].click_retry_btn()
        self.fc.fd["printersettings"].verify_cleaning_dialog()
        self.fc.fd["printersettings"].verify_cleaning_dialog_dismiss(timeout=60)
        self.fc.fd["printersettings"].verify_printing_dialog()
        self.fc.fd["printersettings"].verify_printing_dialog_dismiss()
        self.fc.fd["printersettings"].click_cleaning_done_btn()
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog_dismiss()
        self.p.fake_action_door_open()
        self.fc.fd["printersettings"].click_clean_arrow()
        self.fc.fd["printersettings"].verify_door_open_dialog()
        self.fc.fd["printersettings"].click_dialog_cancel_btn()
        self.fc.fd["printersettings"].verify_door_open_dismiss()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()
        
    @pytest.mark.regression
    def test_02_close_the_door(self):
        """
        Close the door.
        """
        self.p.fake_action_door_close()