import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_05_Print_Photos_Multi_Photos(object):
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
        Verify the Print photos tile in Printer device page.
        """
        #install printer driver on PC settings
        self.win_driver['printer'] = self.fc.fd["hpx_rebranding_utility"].select_printer_on_win_settings(self.hostname)
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_02_check_driver_window_opening_C44257261(self):
        """
        User should be navigated to driver window opening screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44257261
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP, press_enter=False)
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
    
    @pytest.mark.regression
    def test_03_verify_user_can_select_multiple_photos_C44451136(self):
        """
        user can select multiple files to print.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44451136
        """
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["print"].input_file_name('"' + w_const.TEST_DATA.WOMAN_BMP + '"' + '"' + w_const.TEST_DATA.AUTUMN_JPG + '"', press_enter=False)

    @pytest.mark.regression
    def test_04_verify_prints_multiple_photos_C44275261(self):
        """
        User can print multiple photos.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44275261
        """
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_05_verify_prints_multiple_photos_with_preview_C44451141(self):
        """
        Verify the print job and preview screen, after user adding multiple files in file picker window.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44451141
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["print"].input_file_name('"' + w_const.TEST_DATA.WOMAN_BMP + '"' + '"' + w_const.TEST_DATA.AUTUMN_JPG + '"')
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
   
    @pytest.mark.regression
    def test_06_user_prints_with_various_file_format_C44274940(self):
        """
        user prints with various file format.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44274940
        """
        self.fc.check_files_exist(w_const.TEST_DATA.AUTUMN_JPG, w_const.TEST_DATA.AUTUMN_JPG_PATH)
        file_list = [w_const.TEST_DATA.WORM_JPEG, w_const.TEST_DATA.FISH_PNG, w_const.TEST_DATA.AUTUMN_JPG, w_const.TEST_DATA.WOMAN_BMP]
        for file in file_list:
            print(file)
            self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
            self.fc.fd["print"].verify_file_picker_dialog()
            self.fc.fd["print"].input_file_name(file, press_enter=False)
            self.fc.fd["print"].select_file_picker_dialog_print_btn()
            self.win_driver['printer'] = self.is_real_printer()
            if self.win_driver['printer']:
               self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
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


    

    

