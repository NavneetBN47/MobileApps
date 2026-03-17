import pytest
import random
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_02_Print_Photos_Copies_And_Duplex_Printing(object):
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
        # The simulator printer driver shows driver is unavaliable.Some options don't display in driver window.
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()

    @pytest.mark.regression
    def test_02_select_any_option_in_copies_dropdown_c44394680(self):
        """
        In copies text field, enter any value in driver window screen. (Ex: 5,10,15,20)
        Then click on Print button in driver settings window.
        User should be able to print successfully with the specified number of copy job.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44394680
        """
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Copies option')
        else:
            source_text = ["5","10","15","20"]
            set_source = random.choice(source_text)
            self.fc.fd["print"].input_copies_number(set_source)
            
    @pytest.mark.regression
    def test_03_select_any_option_in_duplex_printing_dropdown_C44394962(self):
        """
        In driver settings->Click on more settings-> select any option in duplex printing dropdown.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44394962
        """
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WORM_JPEG, w_const.TEST_DATA.WORM_JPEG_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WORM_JPEG)
        self.win_driver['printer'] = self.is_real_printer()
        if self.win_driver['printer']:
           self.fc.fd["print"].verify_detail_simple_photo_print_dialog()
        self.fc.fd["print"].select_more_settings_link()
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Duplex printing')
        else:
           source_text = ["Print on only one side of the page","Flip the long edge","Flip the short edge"]
           set_source = random.choice(source_text)
           self.fc.fd["print"].change_duplex_printing_setting(set_source)

    @pytest.mark.regression
    def test_04_print_with_selected_duplex_printing_dropdown_C44449269(self):
        """
        Verify the duplex printing dropdown and print job.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44449269
        """
        self.fc.fd["print"].select_more_settings_menu_dialog_ok_btn()
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