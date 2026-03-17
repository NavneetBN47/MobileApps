import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_11_Cartridge_Low(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    @pytest.mark.skyreach
    def test_01_validate_cartridge_low(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref= 66086, type="info")
        success = InformationSimulatorLEDM.cartridge_low(self.error_manager, color="k")
        assert success, "Failed to set cartridge low error"
        assert self.supplies_status.verify_printer_card_present(), "Printer card is not present"
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp(), "Info icon is not present in PDP"
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title), "Info alert title in PDP is incorrect"
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k'), "Cartridge colour icon 'k' is not present"
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, f"Alert title text: '{info_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Alert Body text: '{info_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not present"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not present"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()