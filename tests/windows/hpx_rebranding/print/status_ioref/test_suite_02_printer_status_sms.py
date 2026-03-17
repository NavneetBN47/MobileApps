import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.web.hpx.printer_status import IorefData
from MobileApps.tests.windows.hpx_rebranding.print.status_ioref.conftest import PrinterStatusSMSBase


pytest.app_info = "HPX"
class Test_Suite_02_Printer_Status_SMS(PrinterStatusSMSBase):
    ioref_num = 2
    ioref_list = IorefData.get_ioref_list(num=ioref_num)
    
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']
        cls.trigger_status = {}

    @pytest.mark.regression
    def test_01_go_to_printer_status_and_trigger(self):
        """
        Go to Printer device screen and trigger the IORef in printer status screen
        """
        self.go_to_printer_status_and_trigger(ioref_num=self.ioref_num)

    @pytest.mark.parametrize("ioref", ioref_list)
    @pytest.mark.regression
    def test_02_check_ioref_content(self, ioref):
        """
        Verify the IORef in printer status screen
        """
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.fc.fd["printer_status"].verify_ps_content(ioref, self.ioref_list)

    

