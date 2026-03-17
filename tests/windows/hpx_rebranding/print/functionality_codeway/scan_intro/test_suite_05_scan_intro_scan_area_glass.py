import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_05_Scan_Intro_Scan_Area_Glass(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.adf_scan_support = {}

        
    @pytest.mark.regression
    def test_01_check_scan_area_glass_C43738408(self):
        """
        Select source to Scanner glass, verify different Scan Area values can be changed and changes are reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738408
        """
        glass_scan_areas = [
            self.fc.fd["scan"].ENTIRE_SCAN_AREA,
            self.fc.fd["scan"].LETTER,
            self.fc.fd["scan"].A4,
            self.fc.fd["scan"].X46,
            self.fc.fd["scan"].X57
            ]
        
        failed_areas = []
        
        for index, glass_scan_area in enumerate(glass_scan_areas):
            try:
                if index == 0:
                    self.fc.launch_hpx_to_home_page()
                    self.fc.add_a_printer(self.p)
                    self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
                    self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
                    self.fc.fd["devicesDetailsMFE"].click_scan_tile()
                    self.fc.fd["scan"].verify_scan_btn(timeout=30)

                    if self.fc.fd["scan"].verify_source_dropdown_enabled():
                        self.adf_scan_support['status'] = True
                        if self.fc.fd["scan"].get_scan_source_value() != self.fc.fd["scan"].GLASS:
                            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].GLASS)
                    else:
                        self.adf_scan_support['status'] = False
                    assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].GLASS
                    assert self.fc.fd["scan"].get_scan_area_value() == self.fc.fd["scan"].ENTIRE_SCAN_AREA
                else:
                    self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].AREA, glass_scan_area)
                    assert self.fc.fd["scan"].get_scan_area_value() == glass_scan_area
                
                logging.info(f"Start to test scan area: {glass_scan_area}")
                self.fc.fd["scan"].click_preview_btn()
                self.fc.fd["scan"].verify_scan_btn(timeout=30)
                self.fc.fd["scan"].verify_scanner_preview_screen()
                self.fc.fd["scan"].click_scan_btn()
                self.fc.fd["scan"].verify_scan_result_screen(timeout=120)
                self.fc.fd["scan"].click_back_arrow()
                self.fc.fd["scan"].verify_exit_without_saving_dialog()
                self.fc.fd["scan"].click_yes_btn()
                self.fc.fd["scan"].verify_scan_btn(timeout=30)
                
            except Exception as e:
                failed_areas.append({"Scan_Area": glass_scan_area, "error": str(e)})
                try:
                    self.fc.restart_hpx()
                    self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
                    self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
                    self.fc.fd["devicesDetailsMFE"].click_scan_tile()
                    self.fc.fd["scan"].verify_scan_btn(timeout=30)
                except Exception:
                    pass
        
        if failed_areas:
            error_msg = f"\n{len(failed_areas)} out of {len(glass_scan_areas)} scan areas failed:\n"
            for item in failed_areas:
                error_msg += f"  - {item['Scan_Area']}: {item['error']}\n"
            raise AssertionError(error_msg)