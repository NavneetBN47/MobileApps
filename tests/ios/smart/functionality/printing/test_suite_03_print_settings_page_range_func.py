import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_03_Print_Settings_Page_Range_Func(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        # Define flows
        cls.common_preview = cls.fc.fd["common_preview"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]

    def test_01_verify_page_range_selection(self):
        """
        verify selection/unselection of pages in page range screen- C16932518, C16932517
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, "test_reg_file_4", no_of_pages=4)
        self.fc.select_a_file_and_go_to_print_preview(file_name="test_reg_file_4")
        assert self.common_preview.get_page_range_selected_value() == 'All'
        self.common_preview.select_page_range_option()
        assert self.common_preview.get_page_range() == 'Pages 1-4'
        assert self.common_preview.verify_pages_selected('1')
        assert self.common_preview.verify_pages_selected('3')
        self.common_preview.select_or_unselect_pages(['1', '3'])
        assert self.common_preview.verify_pages_selected('1') is False
        assert self.common_preview.verify_pages_selected('3') is False
        assert self.common_preview.get_page_range() == 'Pages 2, 4'
        self.common_preview.select_or_unselect_pages('3')
        assert self.common_preview.verify_pages_selected('3')
        assert self.common_preview.get_page_range() == 'Pages 2-4'
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_page_range_selected_value() == '2-4'
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_02_verify_page_range_select_and_deselect_all_option(self):
        """
        verify selection/unselection of pages in page range screen- C16932519
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, "test_reg_file_4", no_of_pages=4)
        self.fc.select_a_file_and_go_to_print_preview(file_name="test_reg_file_4")
        self.common_preview.select_page_range_option()
        self.common_preview.select_or_unselect_pages(['2', '4'])
        assert self.common_preview.verify_pages_selected('2') is False
        assert self.common_preview.verify_pages_selected('4') is False
        assert self.common_preview.get_page_range() == 'Pages 1, 3'
        self.common_preview.select_select_all_btn()
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_page_range_selected_value() == 'All'
        self.common_preview.select_page_range_option()
        assert self.common_preview.get_page_range() == 'Pages 1-4'
        self.common_preview.select_deselect_all_btn()
        assert self.common_preview.verify_pages_selected('1') is False
        assert self.common_preview.verify_pages_selected('3') is False
        assert self.common_preview.verify_static_text('Pages 1-4') is False
        self.common_preview.select_navigate_back()
        assert self.common_preview.check_manual_input_pop_up_msg()
        self.common_preview.select_ok_btn()
        self.common_preview.verify_page_range_screen()

    def test_03_verify_page_range_manual_input_function(self):
        """
         Description:  C31297357, C31297358
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
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
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