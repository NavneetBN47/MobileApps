import pytest
import random
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_07_Print_Photos_Orientation_Dropdown(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.hostname = cls.p.get_printer_information()['serial number']
        cls.win_driver = {'printer': True}
        
  
    @pytest.mark.regression
    def test_01_go_to_in_driver_window(self):
        """
        Go to in file picker window.
        """
        #install printer driver on PC settings
        self.win_driver['printer'] = self.fc.fd["hpx_rebranding_utility"].select_printer_on_win_settings(self.hostname)
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()

    @pytest.mark.regression
    def test_02_check_orientation_dropdown_C44275488(self):
        """
        Verify the Orientation dropdown option
    
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44275488
        """
        self.fc.fd["print"].verify_orientation_setting()

    @pytest.mark.regression
    def test_03_check_landscape_option_by_default_C44275269(self):
        """
        Landscape option should be displayed by default.
        According to HPXG-2216: [Dogfood] Portrait photo set as landscape by default., it's closed as design.
        The default value is landscape.

        TestRails ->https://hp-testrail.external.hp.com/index.php?/cases/view/44275269
        """
        self.fc.fd["print"].verify_landscape_opt_display()

    @pytest.mark.regression
    def test_04_select_any_option_in_orientation_C44275621(self):
        """
        Select any option in orientation dropdown of driver window.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44275621
        """
        source_list = ["Portrait", "Landscape"]
        set_source = random.choice(source_list)
        self.fc.fd["print"].change_orientation_setting(set_source)

    @pytest.mark.regression
    def test_05_print_with_selected_orientation_C44276665(self):
        """
        User should be able to print successfully with the selected orientation settings.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44276665
        """
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def is_real_printer(self):
        """
        Check if the selected printer is a real printer (not PDF)
        """
        printerhost = self.fc.fd["print"].select_printer(self.hostname)
        return printerhost != 'Microsoft Print to PDF' 