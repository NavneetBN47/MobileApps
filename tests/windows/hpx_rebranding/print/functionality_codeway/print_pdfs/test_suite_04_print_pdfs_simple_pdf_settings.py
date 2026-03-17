import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import random


pytest.app_info = "HPX"
class Test_Suite_04_Print_Pdfs_Simple_Pdf_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.hostname = cls.p.get_printer_information()['serial number']
        cls.ori_pre = {}
        cls.win_driver = {'printer': True}

    
    @pytest.mark.regression
    def test_01_go_to_simple_pdf_print_dialog_c44256134(self):
        """
        Select PDF file in file picker window.
        Preview screen should not be displayed between document selection and print driver launch.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44256134
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF)
        printerhost = self.fc.fd["print"].select_printer(self.hostname)
        if printerhost == 'Microsoft Print to PDF':
            self.win_driver['printer'] = False
        if self.win_driver['printer']:
            self.fc.fd["print"].verify_detail_simple_pdf_print_dialog()

    @pytest.mark.regression
    def test_02_verify_orientation_dropdown_list_c44255491(self):
        """
        Verify the default value of Orientation dropdown in driver settings.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255491
        """
        self.fc.fd["hpx_rebranding_common"].save_image("preview_image", image_n="preview_org.png")
        self.fc.fd["print"].verify_orientation_setting()

    @pytest.mark.regression
    def test_03_select_orientation_value_c44255492(self):
        """
        Verify the display of orientation dropdown when user selects any option.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255492
        """
        orientation = random.choice(['Portrait', 'Landscape'])
        self.ori_pre['val'] = orientation
        self.fc.fd["print"].change_orientation_setting(orientation)
        self.fc.fd["print"].verify_display_text(orientation)

    @pytest.mark.regression
    def test_04_verify_preview_screen_after_select_orientation_value_c44255493(self):
        """
        Verify the preview screen when user selects any option in orientation dropdown.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255493
        """
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("preview_image", image_n="preview_org.png")
        if self.ori_pre['val'] == 'Portrait':
            com_org < 0.02
        else:
            com_org > 0.33

    @pytest.mark.regression
    def test_05_verify_paper_size_dropdown_list_c44255604(self):
        """
        Verify the display of paper size dropdown list in driver window.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44255604
        """
        self.fc.fd["print"].verify_paper_size_setting()

    @pytest.mark.regression
    def test_06_select_paper_size_value_c44255609(self):
        """
        Verify the display of paper size dropdown, when user selects any value in paper size dropdown of driver window.
        User should be able to select all the values in paper size dropdown. (not fully covered)
        The selected value should be displayed in paper size dropdown.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255609  (not fully covered)
        """
        paper_size = self.fc.fd["print"].change_paper_size_setting()
        self.fc.fd["print"].verify_display_text(paper_size)

    @pytest.mark.regression
    def test_07_verify_output_quality_setting_c44255611(self):
        """
        In driver settings, select any option in Output quality dropdown.
        Then click on Print button in driver windows screen.
        User should be able to print successfully using selected Output quality without any error.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255611
        """
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Output quality')
        else:
            self.fc.fd["print"].verify_output_quality_setting()
            output_quality = random.choice(['Normal', 'Draft', 'High quality'])
            self.fc.fd["print"].change_output_quality_setting(output_quality)
            self.fc.fd["print"].verify_display_text(output_quality)

    @pytest.mark.regression
    def test_08_verify_copies_settings_c44255612(self):
        """
        In copies textbox enter any value in driver window. (Ex: 5,10,15,20)
        User should be able to print successfully with the specified copy operation.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255612
        """
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Copies')
        else:
            copies = random.choice(['5', '10', '15', '20'])
            self.fc.fd["print"].change_copies_setting(copies)

    @pytest.mark.regression
    def test_09_verify_duplex_printing_settings_c44255614(self):
        """
        Verify the display of Duplex printing dropdown, when user selects any value in duplex printing dropdown of driver window screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255614
        """
        if not self.win_driver['printer']:
            pytest.skip('print to PDF has no Duplex printing')
        else:
            self.fc.fd["print"].verify_duplex_printing_setting()
            duplex_printing = random.choice(['Print on only one side of the page', 'Flip the long edge', 'Flip the short edge'])
            self.fc.fd["print"].change_duplex_printing_setting(duplex_printing)
            self.fc.fd["print"].verify_display_text(duplex_printing)

    @pytest.mark.regression
    def test_10_verify_page_range_dropdown_list_c44255664(self):
        """
        Verify the display of Page range dropdown list in driver window.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255664
        """
        self.fc.fd["print"].verify_page_range_setting()

    @pytest.mark.regression
    def test_11_select_page_range_value_c44255665(self):
        """
        Verify the display of Page Range dropdown, when user selects any option in page range dropdownlist of driver window.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255665
        """
        page_range = random.choice(['Print all pages', 'Print current page', 'Print pages in range'])
        self.fc.fd["print"].change_page_range_setting(page_range)
        self.fc.fd["print"].verify_display_text(page_range)

    @pytest.mark.regression
    def test_12_verify_page_range_textbox_c44255672(self):
        """
        In driver settings, select "print pages in range" option in Page Range dropdown.
        Page Range textbox should be displayed with the empty value.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255672
        """
        if not self.fc.fd["print"].verify_display_text('Print pages in range', raise_e=False):
            self.fc.fd["print"].change_page_range_setting('Print pages in range')
        self.fc.fd["print"].verify_page_range_edit()

    @pytest.mark.regression
    def test_13_enter_page_range_value_c44255795(self):
        """
        Verify the print job, when user enters the valid page range value in driver settings screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255795
        """
        range_value = random.choice(['1', '2', '1-2'])
        self.fc.fd["print"].enter_page_range_value(range_value)

    @pytest.mark.regression
    def test_14_print_c44255603_c44255610_c44255615_c44255671_c44255801(self):
        """
        User should be able to print successfully with the selected orientation settings.
        Printed orientation should match with the preview screen. (not covered)
 
        https://hp-testrail.external.hp.com/index.php?/cases/view/44255603  (not fully covered)

        Verify the print job when user selects any value in paper size dropdown of driver window
        User should be able to print successfully with the selected paper size.
        Printed output should match with the preview screen. (not covered)

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255610 (not fully covered)

        Verify the print job, when user selects any option in duplex printing dropdown of driver window.
        User should be able to print successfully with the selected duplex printing option.
        Printed output should match with the preview screen.(not covered)

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255615  (not fully covered)

        User should be able to select all the options in Page Range dropdown. The selected option should be displayed in Page range dropdown.
        User should be able to print successfully with the selected page range option.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255671

        Verify the Print job and preview screen, when user selects any option in Page Range dropdown list.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44255801
        """
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
        