import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_06_Print_Photos_Click_Outside(object):
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
    def test_02_verify_file_picker_opening_screen_C44256714(self):
        """
        Verify the screen, after observing file picker opening screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44256714
        """  
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_03_click_outside_on_file_picker_screen_without_selecting_file_C44258525(self):
        """
        click on outside the file picker window without selecting file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258525
        """  
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_04_click_outside_on_file_picker_screen_with_selecting_file_C44258516(self):
        """
        click on outside the file picker window with selecting file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258516
        """
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP, press_enter=False)
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_05_click_outside_on_driver_window_C44274938(self):
        """
        In driver windows screen click outside the driver settings screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44274938
        """  
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
    
    @pytest.mark.regression
    def test_06_click_outside_on_driver_window_C44256396(self):
        """
        click on "<-Device Name/back", minimize, maximize and close button in the HPX app of "Print Photos" screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44256396
        """
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_maximize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_close_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
    
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def is_real_printer(self):
        """
        Check if the selected printer is a real printer (not PDF)
        """
        printerhost = self.fc.fd["print"].select_printer(self.hostname)
        return printerhost != 'Microsoft Print to PDF' 