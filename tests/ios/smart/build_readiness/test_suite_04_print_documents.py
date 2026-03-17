import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_04_Print_Documents:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]
        cls.p = load_printers_session

    def test_01_verify_page_range_manual_input_function(self):
        """
         Description:  C50698984
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file with 4 pages
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Click on Page Range options
         8. Click on Manual Input button
         9. Input an invalid page value
         10. Click on OK button
         11. Input a correct page value, and click on Done button
         12. Click on Back button
         13. Click on Print button

         Expected Results:
         7. Verify Page Range screen
         8. Verify Manual Input popup
         9. Verify Invalid input message displays
         10. Verify Manual Input popup
         11. The page is selected correctly according to the value from step 11
         12. Verify the page value shows correctly on Print Preview screen
         13. Verifying the printing job is completed
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, "test_reg_file_4", no_of_pages=4)
        self.fc.select_a_file_and_go_to_print_preview(file_name="test_reg_file_4")
        self.common_preview.select_page_range_option()
        self.common_preview.select_manual_input_btn()
        assert self.common_preview.check_manual_input_pop_up_msg(input_page_range=True)
        self.common_preview.enter_page_range('5')
        self.common_preview.select_done()
        assert self.common_preview.check_manual_input_pop_up_msg()
        self.common_preview.select_ok_btn()
        assert self.common_preview.check_manual_input_pop_up_msg(input_page_range=True)
        self.common_preview.enter_page_range('1, 3')
        self.common_preview.select_done()
        assert self.common_preview.verify_pages_selected('1')
        assert self.common_preview.verify_pages_selected('3')
        assert self.common_preview.verify_pages_selected('2') is False
        assert self.common_preview.verify_pages_selected('4') is False
        assert self.common_preview.get_page_range() == 'Pages 1, 3'
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_page_range_selected_value() == '1, 3'
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_02_verify_print_quality(self):
        """
        Description:  C50698985
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file with multiple pages
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Click on Print Quality "Best" option
         8. Click on Print button

         Expected Results:
         7. Verifies print quality options ui, select each option and verify its select on
         8. Printing job can be printed success
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        self.common_preview.select_print_quality_option(self.common_preview.PRINT_QUALITY_BEST_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_print_quality_selected_value() == "Best"
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_verify_print_2sided(self):
        """
        Descriptions: C50698986
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file with multiple pages
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Select the paper size according to the testing requirements
         8. Click on Print button

        Expected Result:
         8. Verify printing job successfully
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, "test_reg_file_2", no_of_pages=2)
        self.fc.select_a_file_and_go_to_print_preview(file_name="test_reg_file_2")
        if self.common_preview.verify_2_sided_option(invisible=True, raise_e=False):
            pytest.skip("currently printer doesn't support two sided option")
        self.common_preview.select_2_sided_option(self.common_preview.TWO_SIDED_LONG_EDGE_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_2_sided_selected_value() == "Long Edge"
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=80)

    def test_04_verify_print_documents_tile_behavior(self):
        """
        Description: C50698988
            Tap Tile Print Documents
                Launch the HP Smart app
                Tap on Print Documents and select any file to print and proceed to landing page.
                On the Preview landing page, tap on 'Print'
                Again tap on Print and submit a print job

            Expected Result:
                Verify that the print is successful
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        file_name= "test_pdf_file"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, file_name)
        self.fc.select_a_file_and_go_to_print_preview(file_name)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_done()
        self.fc.go_hp_smart_files_and_delete_all_files()