import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_03_Print_Photos_Different_File(object):
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
    def test_01_go_to_device_detail_page(self):
        """
        go to Printer device page.
        """
        #install printer driver on PC settings
        self.win_driver['printer'] = self.fc.fd["hpx_rebranding_utility"].select_printer_on_win_settings(self.hostname)
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_02_select_the_different_file_size_c44275191(self):
        """
        Select the different file size (Ex:100KB, 202KB, 500KB, 10MB, 15.1MB and 29.4MB) in file picker window->Click on Select Photos to Print button.
        User should be able to print successfully with different file size without any error.(We didn't use a file of about 30MB)
        https://hp-testrail.external.hp.com/index.php?/cases/view/44275191
        """
        pic_list = [
            (w_const.TEST_DATA.WORM_JPEG, w_const.TEST_DATA.WORM_JPEG_PATH),
            (w_const.TEST_DATA.AUTUMN_JPG, w_const.TEST_DATA.AUTUMN_JPG_PATH),
            (w_const.TEST_DATA.PLANT_JPG, w_const.TEST_DATA.PLANT_JPG_PATH),
            (w_const.TEST_DATA.MAP_18MB_JPEG, w_const.TEST_DATA.MAP_18MB_JPEG_PATH)
        ]
        
        for pic_name, pic_path in pic_list:
            self.fc.check_files_exist(pic_name, pic_path)
            
            self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
            self.fc.fd["print"].input_file_name(pic_name)
            printerhost = self.fc.fd["print"].select_printer(self.hostname)
            
            if printerhost == 'Microsoft Print to PDF':
                self.win_driver['printer'] = False
            
            if self.win_driver['printer']:
                self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
            
            self.fc.fd["print"].select_simple_print_dialog_print_btn()
            self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_03_print_photos_with_invalid_file_c44275189(self):
        """
        Verify the functionality of "Print Photos" tile, when user prints invalid file.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44275189
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
