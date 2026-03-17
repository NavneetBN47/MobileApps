import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_21_Cartridge_Out_Laser(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    @pytest.mark.skyreach
    def test_01_cartridge_out_laser(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66039, type="error")
        success = ErrorSimulatorLEDM.cartridge_out(self.error_manager, color="k")
        assert success, "Failed to set cartridge out error"
        assert self.supplies_status.verify_printer_card_present(), "Printer card is not present"
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp(), "Error icon is not present in PDP"
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title), "Error alert title in PDP is incorrect"
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k'), "Cartridge colour icon is not correct"
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not present"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not present"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
