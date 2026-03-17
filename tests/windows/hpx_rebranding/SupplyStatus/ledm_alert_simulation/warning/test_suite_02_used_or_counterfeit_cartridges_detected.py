import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.warning_simulator_ledm import WarningSimulatorLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_02_used_Or_counterfeit_cartridges_Detected(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.spark
    @pytest.mark.limtane_mfp
    @pytest.mark.limtane_sfp
    @pytest.mark.shaolin
    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_01_validate_cartridge_counterfeit_question_65592(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65592,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_yes_btn()
        assert self.supplies_status.verify_no_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_02_validate_used_or_counterfeit_cartridges_detected_65685(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65685,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_65685(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_yes_btn()
        assert self.supplies_status.verify_no_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_03_validate_used_or_counterfeit_cartridges_installed_65687(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65687,type="warning")
        success = WarningSimulatorLEDM.cartridge_refilled_65687(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_04_validate_cartridge_counterfeit_65617(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65617,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_05_validate_counterfeit_or_used_cartridges_identified_65686(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65686,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_65686(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_06_validate_used_or_refilled_cartridges_installed_66099(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=66099,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_no_instant_ink_sub_66099(self.error_manager, color="k")
        assert success, "Failed to set used or refilled cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_07_validate_used_or_refilled_cartridges_installed_66098(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=66098,type="warning")
        success = WarningSimulatorLEDM.used_or_refilled_cartridges_installed_66098(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_08_validate_cartridge_counterfeit_question_no_instant_ink_sub_66099(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=66099,type="warning")
        success = WarningSimulatorLEDM.cartridge_refilled_66099(self.error_manager, color="k")
        assert success, "Failed to set used or refilled cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_09_used_or_refilled_cartridges_installed_66098(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=66098,type="warning")
        success = WarningSimulatorLEDM.used_or_refilled_cartridges_installed_66098(self.error_manager, color="k")
        assert success, "Failed to set used or refilled cartridges installed warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_10_cartridge_counterfeit_question_yes_cont_instant_ink_sub_65687(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65687,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_yes_cont_instant_ink_sub_65687(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_11_cartridge_counterfeit_question_yes_instant_ink_sub_65686(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65686,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_yes_instant_ink_sub_65686(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_12_cartridge_counterfeit_inksub_65686(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65686,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_inksub_65686(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_13_cartridge_counterfeit_question_yes_instant_ink_sub_65617(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65617,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_yes_instant_ink_sub_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
