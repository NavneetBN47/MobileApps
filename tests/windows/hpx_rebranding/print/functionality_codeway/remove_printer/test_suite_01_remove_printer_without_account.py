import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Remove_Printer_Without_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_remove_from_app_button_shows_C53370963(self):
        """
        Verify "Remove from App" Button appear.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53370963
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        sleep(3)
        self.fc.fd["devicesDetailsMFE"].verify_remove_from_app_button()
        
    @pytest.mark.regression
    def test_02_remove_device_confirmation_dialog_C53370976(self):
        """
        click Remove from app button.
        Verify Remove device Confirmation Dialog
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53370976
        """
        self.fc.fd["devicesDetailsMFE"].click_remove_from_app_button()
        self.fc.fd["devicesDetailsMFE"].verify_confirmation_dialog()
        
    @pytest.mark.regression
    def test_03_click_cancel_button_on_confirmation_dialog_C53371053(self):
        """
        The dialog should close and the printer should remain in the printer list after clicking cancel button.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53371053
        """
        self.fc.fd["devicesDetailsMFE"].click_cancel_button()
        assert self.fc.fd["devicesDetailsMFE"].verify_confirmation_dialog(raise_e=False) is False
        self.fc.swipe_window(direction="up", distance=14)
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()
        self.fc.fd["devicesMFE"].verify_device_card_show_up()

    @pytest.mark.regression
    def test_04_successful_removal_single_printer_C53371421(self):
        """
        Remove the printer and verify it is removed successfully from the printer list.
        Failed with HPXG-4068

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53371421
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_remove_from_app_button()
        self.fc.fd["devicesDetailsMFE"].click_remove_from_app_button()
        self.fc.fd["devicesDetailsMFE"].verify_confirmation_dialog()
        self.fc.fd["devicesDetailsMFE"].click_remove_button()
        assert not self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, raise_e=False)


    

        


    