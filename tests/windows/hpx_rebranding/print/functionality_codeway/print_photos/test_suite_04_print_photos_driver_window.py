import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_04_Print_Photos_Driver_Window(object):
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
    def test_02_check_driver_window_opening_C44257023(self):
        """
        File picker window should be closed, and user should be navigated to driver window opening screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44257023
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        # The simulator printer driver shows driver is unavaliable.Some options don't display in driver window.
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()

    @pytest.mark.regression
    def test_03_click_cancel_btn_on_driver_window_opening_C44258709(self):
        """
        In driver window screen click cancel button.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258709
        """
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_04_user_add_printer_in_driver_window_C44275263(self):
        """
        User should be able to select the added device in printer dropdown
    
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44275263
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        
    @pytest.mark.regression
    def test_05_click_close_btn_on_driver_window_opening_c44259556(self):
        """
        Click on close button of driver settings screen.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44259556
        """
        self.fc.fd["print"].select_simple_print_dialog_close_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_06_verify_preview_with_file_c44258647(self):
        """
        Verify the driver window preview screen, after user adding the file in file picker window screen.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258647
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        preview = self.fc.fd["hpx_rebranding_common"].compare_image_diff("simple_preview_image", folder_n="print", image_n="preview_org.png")
        assert preview < 0.02
        

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def is_real_printer(self):
        """
        Check if the selected printer is a real printer (not PDF)
        """
        printerhost = self.fc.fd["print"].select_printer(self.hostname)
        return printerhost != 'Microsoft Print to PDF'   

    