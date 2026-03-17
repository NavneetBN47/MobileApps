import pytest
import random
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_10_Print_Photos_Scaling_And_Output_Quality(object):
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
        Go to in file picker window
        """
        #install printer driver on PC settings
        self.win_driver['printer'] = self.fc.fd["hpx_rebranding_utility"].select_printer_on_win_settings(self.hostname)
        #go on test
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
    def test_02_select_any_option_in_Scaling_dropdown_C44277846(self):
        """
        In driver settings, select any option in Scaling dropdown.
        Verify the print job and preview screen in driver window screen.
        User should be able to print successfully using selected scaling settings without any error.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44277846
        """
        source_list = ["Crop","Shrink to fit"]
        set_source = random.choice(source_list)
        self.fc.fd["print"].change_select_scaling_setting(set_source)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        
    @pytest.mark.regression
    def test_03_select_any_option_in_output_quality_dropdown_C44394601(self):
        """
        In driver settings, select any option in Output quality dropdown list.
        User should be able to print successfully using the selected Output quality without any error.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44394601
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        source_list = ["Draft","Normal","High quality"]
        set_source = random.choice(source_list)
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Paper type')
        else:
           self.fc.fd["print"].change_select_output_quality_setting(set_source)
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