import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.warning_simulator_ledm import WarningSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_02_used_Or_Counterfeit_cartridges_Detected(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
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
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65592,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_02_validate_used_or_counterfeit_cartridges_detected_65685(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65685,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_65685(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()

    def test_03_validate_used_or_counterfeit_cartridges_installed_65687(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65687,type="warning")
        success = WarningSimulatorLEDM.cartridge_refilled_65687(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()

    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_04_validate_cartridge_counterfeit_65617(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65617,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    def test_05_validate_counterfeit_or_used_cartridges_identified_65686(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65686,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_65686(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    def test_06_validate_used_or_refilled_cartridges_installed_66099(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66099,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_no_instant_ink_sub_66099(self.error_manager, color="k")
        assert success, "Failed to set used or refilled cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()

    def test_07_validate_used_or_refilled_cartridges_installed_66098(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66098,type="warning")
        success = WarningSimulatorLEDM.used_or_refilled_cartridges_installed_66098(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_08_validate_cartridge_counterfeit_question_no_instant_ink_sub_66099(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66099,type="warning")
        success = WarningSimulatorLEDM.cartridge_refilled_66099(self.error_manager, color="k")
        assert success, "Failed to set used or refilled cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()

    def test_09_used_or_refilled_cartridges_installed_66098(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66098,type="warning")
        success = WarningSimulatorLEDM.used_or_refilled_cartridges_installed_66098(self.error_manager, color="k")
        assert success, "Failed to set used or refilled cartridges installed warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_10_cartridge_counterfeit_question_yes_cont_instant_ink_sub_65687(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65687,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_yes_cont_instant_ink_sub_65687(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()

    def test_11_cartridge_counterfeit_question_yes_instant_ink_sub_65686(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65686,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_yes_instant_ink_sub_65686(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    def test_12_cartridge_counterfeit_inksub_65686(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65686,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_inksub_65686(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_13_cartridge_counterfeit_question_yes_instant_ink_sub_65617(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65617,type="warning")
        success = WarningSimulatorLEDM.cartridge_counterfeit_question_yes_instant_ink_sub_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question yes condition warning"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()
