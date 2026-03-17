import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Setup_Catridge(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_01_setup_cartridge_for_pha_65591_65851(self):
        # error alert for PHA 65591 and 65851
        alert_title, alert_img, alert_detailed_body = self.fc.read_supplies_status_json_files(ioref=65591,type="error")
        success = InformationSimulatorLEDM.setup_cartridge_for_pha_65591_65851(self.error_manager, color="k")
        assert success, "Failed to set up cartridge for PHA error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(alert_title, alert_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(alert_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == alert_title, f"Alert Title text: '{alert_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(alert_detailed_body), f"Alert Body text: '{alert_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
