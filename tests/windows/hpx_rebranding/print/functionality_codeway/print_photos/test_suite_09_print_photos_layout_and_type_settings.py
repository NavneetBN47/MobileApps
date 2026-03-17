import pytest
import random
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_09_Print_Photos_Layout_And_Type_Settings(object):
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
    def test_02_layout_dropdown_shows_C44277318(self):
        """
        Verify the Select a layout dropdown list.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277318
        """
        self.fc.fd["print"].verify_select_a_layout_setting()

    @pytest.mark.regression
    def test_03_select_any_option_in_layout_dropdown_C44277335(self):
        """
        The different options should be displayed in the Select a layout dropdown list.
        User should be able to select all the values in select a layout dropdown.
     
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277335
        """
        source_list = ["One photo per page","Multiple photos per page"]
        set_source = random.choice(source_list)
        self.fc.fd["print"].change_select_a_layout_setting(set_source)

    @pytest.mark.regression
    def test_04_print_with_any_option_in_layout_dropdown_C44277474(self):
        """
        User should be able to print successfully with the selected settings.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277474
        """
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
    
    @pytest.mark.regression
    def test_05_select_any_option_in_paper_type_dropdown_C44277540(self):
        """
        Verify the print job, when user selects any option in paper type dropdown list of driver window screen.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277540
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        source_list = ["Plain Paper", "Photo paper"]
        set_source = random.choice(source_list)
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Paper type')
        else:
           self.fc.fd["print"].change_paper_type_setting(set_source)
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
   