import pytest

pytest.app_info = "GOTHAM"
class Test_Suite_05_Home_Tiles_Without_Printers(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_verify_get_supplies_correct_behavior(self):
        """
        Verify "Get Supplies" tiles are enabled.
        Verify "To use this..." dialog pop up after clicking the tiles.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061799
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17155819
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16046737
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16069977
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27864781
        """
        self.fc.go_home()

        el = self.home.verify_get_supplies_tile()
        assert el.get_attribute("IsEnabled").lower() == "true"
        
        self.home.select_get_supplies_tile()
        self.home.verify_device_function_dialog()

        self.home.select_device_function_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_02_verify_print_photos_correct_behavior(self):
        """
        Verify "Print Photos" tiles are enabled.
        Verify "To use this..." dialog pop up after clicking the tiles.
        "To use this feature…" dialog UI
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061799
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061800
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890724   
        """
        el = self.home.verify_print_photos_tile()
        assert el.get_attribute("IsEnabled").lower() == "true"

        self.home.select_print_photos_tile()
        self.home.verify_device_function_dialog()

        self.home.select_device_function_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_03_verify_print_documents_correct_behavior(self):
        """
        Verify "Print Documents" tiles are enabled.
        Verify "To use this..." dialog pop up after clicking the tiles.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061799
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061800
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890724 
        """
        el = self.home.verify_print_documents_tile()
        assert el.get_attribute("IsEnabled").lower() == "true"

        self.home.select_print_documents_tile()
        self.home.verify_device_function_dialog()

        self.home.select_device_function_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_04_verify_printer_settings_correct_behavior(self):
        """
        Verify "Printer Settings" tiles are enabled.
        Verify "To use this..." dialog pop up after clicking the tiles.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061799
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061800
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890724
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787542
        """
        el = self.home.verify_printer_settings_tile()
        assert el.get_attribute("IsEnabled").lower() == "true"

        self.home.select_printer_settings_tile()
        self.home.verify_device_function_dialog()

        self.home.select_device_function_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_05_verify_mobile_fax_correct_behavior(self):
        """
        Verify "Mobile Fax" tile opens to mobile fax get stared screen
        Check "Mobile Fax" tile UI 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061799
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27835387
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861530
        """
        el = self.home.verify_mobile_fax_tile()
        assert el.get_attribute("IsEnabled").lower() == "true"

        self.home.select_mobile_fax_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

    def test_06_verify_shortcuts_correct_behavior(self):
        """
        Verify "Shortcuts" tile shows on main UI.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235479
        """
        el = self.home.verify_shortcuts_tile()
        assert el.get_attribute("IsEnabled").lower() == "true"

        self.home.select_shortcuts_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()
        
    def test_07_verify_printable_correct_behavior(self):
        """
        Verify "Play & Learn" tile is changed to "Printables" on main UI.
        Verify "Printables" tile number shows and 4th number.
        Verify correct website opens after clicking printable tile.
        "Printables" Tile UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27864791
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/24809584
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/24809585
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/24809581
        """
        el = self.home.verify_tile_by_index(tile_index=4)

        assert el.get_attribute("IsEnabled").lower() == "true"
        assert el.text == "Printables"

        self.home.select_printables_tile()

        self.web_driver.add_window("PRINTABLES")
        self.web_driver.switch_window("PRINTABLES")

        current_url = self.web_driver.get_current_url()

        for sub_url in self.home.PRINTABLE_URL:
            assert sub_url in current_url

        self.web_driver.close_window(self.web_driver.current_window)
