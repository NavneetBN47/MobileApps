import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_10_Scan_Settings_For_Advance_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_go_to_scaner_screen(self):
        """
        go to scaner screen
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()   
        self.scan.click_get_started_btn()

    def test_02_check_auto_enhancement_panel(self):
        """
        Click on auto enhancement icon located on the top right of scanner screen 
        below the title bar near gear icon to display auto enhancement panel
        Toggle "Auto- Enhancement" and "Auto-Heal", and "Auto-Orientation" 'on' and 'off' in auto enhancement panel
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28735637
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28735634
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28746990
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28735636
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29169666
        """
        self.scan.select_auto_enhancement_icon() 
        self.scan.verify_auto_enhancement_panel_setting_by_default()
        self.scan.click_auto_enhancements_toggle()
        self.scan.click_auto_orientation_toggle()   
        self.scan.verify_auto_enhancement_is_off()
        self.scan.verify_auto_heal_is_off()
        self.scan.verify_auto_orientation_is_on()
        self.scan.click_auto_heal_toggle()
        self.scan.verify_auto_enhancement_is_on()
        self.scan.verify_auto_heal_is_on()

    def test_03_check_presets_dropdown_for_advance(self):
        """
        Click "Advance Presets" dropdown and change the value from 
        "Document" to “Photo" to "Mulit-item", to "Book", to "ID Card"
        Check the Scan settings default values.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28734591
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28734568
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29224262
       
        """
        self.scan.click_gear_icon()
        self.scan.select_presets_dropdown()

        advance_preset = ["Document", "Photo", "Multi-Item", "Book", "ID Card"]
        preset = ["Document", "Photo"]

        for item in advance_preset:
            el = self.scan.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.scan.click_start_scan_text()
        so = self.scan.verify_source_dropdown()
        if so.get_attribute("IsEnabled").lower() == "true":
            self.scan.select_dropdown_listitem(self.scan.SOURCE, "Document Feeder")
            self.scan.select_presets_dropdown()
            for item in preset:
                el = self.scan.verify_dropdown_listitem(item)
                assert el.get_attribute("IsEnabled").lower() == "true"

            self.scan.click_start_scan_text()

    def test_04_check_resolution_info_less_than_300dpi(self):
        """
        Select any value that is less than 300 dpi from the Resolution dropdown box
        Verify the string "Change Your resolution to 300dpi or higher to improve 
        the Save as Text Files feature." shows under the Resolution dropdown box
        Scan multiple pages and check the top of the right settings panel
        Verify number icon shows
        Verify number match to the scanned pages    
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29368110
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572543
       
        """
        self.scan.select_dropdown_listitem(self.scan.DPI, "75 dpi")
        self.scan.verify_resolution_info_less_than_300dpi_msg()
        self.scan.click_scan_btn_with_doc_feeder()
        self.scan.verify_scan_result_screen()
        self.scan.click_add_pages_btn() 
        self.scan.verify_scanner_screen()
        self.scan.verify_number_icon_shows("1")
        