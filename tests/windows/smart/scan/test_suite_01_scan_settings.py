import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import SPL.driver.driver_factory as driver_factory

pytest.app_info = "GOTHAM"
class Test_Suite_01_Scan_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        system_cfg = ma_misc.load_system_config_file()
        pp_info = system_cfg["printer_power_config"]
        db_info = system_cfg.get("database_info", None)
        cls.p_2 = driver_factory.get_printer(pp_info , db_info = db_info)
        cls.p_2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p_2.get_printer_information()
        logging.info("Printer Information:\n {}".format(cls.printer_info2))

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
     
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_source_dropdown(self):
        """
        Verify the source values can be changed
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792491
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/13900761 
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792919
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/13762553
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/28580617(color not check)
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072237
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072312
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072335
           -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793721
        
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        source = ["Document Feeder", "Scanner Glass"]
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        so = self.scan.verify_source_dropdown()
        if so.get_attribute("IsEnabled").lower() == "true":
            self.scan.select_source_dropdown()
            for item in source:
                el = self.scan.verify_dropdown_listitem(item)
                assert el.get_attribute("IsEnabled").lower() == "true"

            self.scan.click_start_scan_text()
        else:
            so.get_attribute("Selection.Selection") == "\"Scanner Glass\" list item"
                
    def test_02_presets_dropdown(self):
        """
        Verify the Presets values can be changed
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792490 
        
        """
        self.scan.select_presets_dropdown()

        preset = ["Document", "Photo"]

        for item in preset:
            el = self.scan.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.scan.click_start_scan_text()

    def test_03_scan_area_dropdown(self):
        """
        Verify the Scan Area values can be changed
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792852
        
        """
        self.scan.select_scan_area_dropdown()

        scan_area = ["Entire Scan Area", "Letter (8.5 x 11 in)", "A4 (210 x 297mm)", \
            "4 x 6 in (10 x 15 cm)", "5 x 7 in (13 x 18 cm)"]

        for item in scan_area:
            el = self.scan.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.scan.click_start_scan_text()

    def test_04_out_put_dropdown(self):
        """
        Verify the Output values can be changed
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792847
        
        """
        self.scan.select_output_dropdown()

        output = ["Color", "Gray"]

        for item in output:
            el = self.scan.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.scan.click_start_scan_text()

    def test_05_check_reset_settings(self):
        """
        Check the 'Reset Settings' located at the top of the scan settings right panel.
        Change some scan settings from default
        Verify 'Reset Settings' is inactive
        Verify 'Reset Settings' is enabled.
        Verify all the changed values in scan setting get revert to default value after clicking on 'Reset Settings', and 'Reset Settings' becomes inactive
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30238083
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30238086 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29367919  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072343      
        """
        self.scan.verify_reset_settings_btn(enable=False)
        self.scan.select_dropdown_listitem(self.scan.OUTPUT, "Gray")
        self.scan.verify_reset_settings_btn()
        self.scan.click_reset_settings_btn()
        self.scan.verify_reset_settings_btn(enable=False)

    def test_06_resolution_dropdown(self):
        """
        Verify the Resolution values can be changed
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792921
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24829218  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792948   
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14783571   
        """
        re = self.scan.verify_resolution_dropdown()
        re.get_attribute("Selection.Selection") == "\"300 dpi\" list item"
        self.scan.select_dropdown_listitem(self.scan.preset, "Document")
        re.get_attribute("Selection.Selection") == "\"300 dpi\" list item"
        self.scan.select_resolution_dropdown()

        resolution = ["75 dpi", "150 dpi", "300 dpi", "600 dpi", "1200 dpi"]

        for item in resolution:
            el = self.scan.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.scan.click_start_scan_text()
        self.scan.select_dropdown_listitem(self.scan.OUTPUT, "Gray")
        self.scan.hover_resolution_icon()
        self.scan.verify_resolution_tooltip()

    def test_07_auto_enhancement_panel(self):
        """
        Verify auto enhancement settings panel shows
        Verify both "Auto-Enhancement" toggle is 'on' and "Auto-Orientation" toggle is 'off' by default
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572539
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572540
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572542
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572544
        """
        self.scan.select_auto_enhancement_icon() 
        self.scan.verify_auto_enhancement_panel_setting_by_default()

    @pytest.mark.parametrize("behaviors", ["add_job","return_scan","reopen_app","select_dif_printer"])
    def test_08_all_changed_settings_are_sticky(self, behaviors):
        """
        Change scan settings (gear icon) and auto settings (magic stick icon), then perform a scan job.
        Add more scan jobs.
        Leave and return to Scan screen.
        Close and re-open the app.
        Select a different printer and go to Scan screen.
        Check the scanner settings and auto settings
        Verify all changed settings are sticky.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793718
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14783573 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14783574
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14783575 
        """
        if behaviors == "add_job":
            self.scan.click_scan_btn()
            self.scan.verify_scan_result_screen() 
            self.scan.click_add_pages_btn()
            self.scan.verify_scanner_screen()
        elif behaviors == "return_scan":
            self.home.select_navbar_back_btn(return_home=False)
            self.scan.verify_exit_without_saving_dialog()
            self.scan.click_yes_btn()
            self.home.verify_home_screen()
            self.home.select_scan_tile()
            self.scan.verify_scanner_screen()
        elif behaviors == "reopen_app":
            self.driver.restart_app()
            self.home.verify_home_screen(20)
            self.home.select_scan_tile()
            self.scan.verify_scanner_screen()
        else:
            self.home.select_navbar_back_btn()
            self.fc.select_a_printer(self.p_2)
            self.home.select_scan_tile()
            self.scan.verify_scanner_screen()
        presets_opt = self.scan.verify_presets_dropdown()
        presets_opt.get_attribute("Selection.Selection") == "\"Document\" list item"
        output_opt = self.scan.verify_output_dropdown()
        output_opt.get_attribute("Selection.Selection") == "\"Gray\" list item"
        re_opt = self.scan.verify_resolution_dropdown()
        re_opt.get_attribute("Selection.Selection") == "\"300 dpi\" list item"
