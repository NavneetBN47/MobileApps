import pytest
import random
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_08_Print_Photos_Size_Settings(object):
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
    def test_02_select_any_option_in_paper_size_dropdown_C44276677(self):
        """
        The different types of paper size settings should be displayed in the paper size dropdown list.
        User should be able to select all the values in paper size dropdownlist.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44276677
        """
        source_list = ['Letter', 'Statement', 'Legal', 'Executive', 'A5', 'A4']
        set_source = random.choice(source_list)
        self.fc.fd["print"].change_paper_size_setting(set_source)

    @pytest.mark.regression
    def test_03_print_with_selected_paper_size_C44276679(self):
        """
        User should be able to print successfully with the selected.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44276679
        """
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_04_photo_size_shows_C44276875(self):
        """
        In driver settings, select any option in Photo Size dropdown.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44276875
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        self.fc.fd["print"].verify_photo_size_setting()
        
    @pytest.mark.regression
    def test_05_select_any_option_in_photo_size_dropdown_C44277097(self):
        """
        User should be able to select all the values in Photo size dropdown.
        Verify the Photo size dropdown list.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277097
        """
        source_list = ["Full Page","3.5x5 in.","4x6 in.","5x7 in.","8x10 in.","9x13 cm","10x15 cm","13x18 cm"]
        set_source = random.choice(source_list)
        self.fc.fd["print"].change_photo_size_setting(set_source)

    @pytest.mark.regression
    def test_06_print_with_selected_photo_size_C44277314(self):
        """
        User should be able to print successfully with the selected Photo size.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277314
        """
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_07_verify_paper_size_dropdown_C44276669(self):
        """
        Verify the display of paper size dropdown list in driver window.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44276669
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        self.fc.fd["print"].verify_paper_size_setting()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def is_real_printer(self):
        """
        Check if the selected printer is a real printer (not PDF)
        """
        printerhost = self.fc.fd["print"].select_printer(self.hostname)
        return printerhost != 'Microsoft Print to PDF' 
    