import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_01_Cartridge_Missing(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.add_printer = request.cls.fc.fd["addprinter"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.manhattan_yeti
    def test_01_validate_cartridge_missing_65690(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65690, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_65690(self.error_manager, color="y")
        assert success, "Failed to set cartridge_missing_65690 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.poseidon_wl_flex
    @pytest.mark.kronos_ik_tank_flex
    @pytest.mark.infinity
    @pytest.mark.shaolin
    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_02_validate_cartridge_missing_65537(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65537, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_65537(self.error_manager, color="k")
        assert success, "Failed to set cartridge_missing_65537 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.taccola_base_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_03_missing_cartridge_hybrid_inksub_65769(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65769, type="error")
        success = ErrorSimulatorLEDM.missing_cartridge_hybrid_inksub_65769(self.error_manager, color="k")
        assert success, "Failed to set missing_cartridge_hybrid_inksub_65769 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    def test_04_cartridges_missing_66262(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66262, type="error")
        success = ErrorSimulatorLEDM.cartridges_missing_66262(self.error_manager, color="y")
        assert success, "Failed to set cartridges_missing_66262 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.taccola_base_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_05_validate_missing_cartridge_instantinksub_65769(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65769, type="error")
        success = ErrorSimulatorLEDM.missing_cartridge_instantinksub_65769(self.error_manager, color="k")
        assert success, "Failed to set missing_cartridge_instantinksub_65769 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.poseidon_wl_flex
    @pytest.mark.kronos_ik_tank_flex
    @pytest.mark.infinity
    @pytest.mark.shaolin
    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_06_validate_missing_cartridge_single_65537(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65537, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_single_65537(self.error_manager, color="k")
        assert success, "Failed to set cartridge_missing_single_65537 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.spark
    @pytest.mark.limtane_mfp
    @pytest.mark.limtane_sfp
    def test_07_validate_cartridge_missing_65589(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65589, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_65589(self.error_manager, color="y")
        assert success, "Failed to set cartridge_missing_65589 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
