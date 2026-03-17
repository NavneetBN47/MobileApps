import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.common.smart.preview import IOSPreview
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_02_Print_Settings_Functionality(object):

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

    def test_01_verify_print_copy_setting(self):
        """
        Description:  C37837664, C35855647
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file with multiple pages
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Click on Print Copy item with plus and minus option

         Expected Results:
         7. Verifies Copies number can be changed success
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        assert self.common_preview.get_copies_btn_enabled_status(IOSPreview.COPIES_MINUS_BTN) == "false"
        assert self.common_preview.get_copies_btn_enabled_status(IOSPreview.COPIES_PLUS_BTN) == "true"
        self.common_preview.change_print_copies(IOSPreview.COPIES_PLUS_BTN, no_of_copies=4)
        assert self.common_preview.get_no_of_copies() == 5
        assert self.common_preview.get_copies_btn_enabled_status(IOSPreview.COPIES_PLUS_BTN) == "false"
        self.common_preview.change_print_copies(IOSPreview.COPIES_MINUS_BTN, no_of_copies=3)
        assert self.common_preview.get_no_of_copies() == 2
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.change_print_copies(IOSPreview.COPIES_MINUS_BTN, no_of_copies=1)
        assert self.common_preview.get_no_of_copies() == 1

    def test_02_verify_color_options(self):
        """
        Description:  C37837665, C37839000, C37839001
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file with multiple pages
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Click on Color Option options
         8. Click on Print button

         Expected Results:
         7. Verifies color options ui, select each option and verify its select on
         8. Printing job can be printed success
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        self.common_preview.select_color_mode_option(self.common_preview.GRAYSCALE_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_color_selected_value() == "Grayscale"
        self.common_preview.select_color_mode_option(self.common_preview.BACK_ONLY_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_color_selected_value() == "Black Only"
        self.common_preview.select_color_mode_option(self.common_preview.COLOR_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_color_selected_value() == "Color"
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_verify_print_quality(self):
        """
        Description:  C31297359, C31297360, C31297361
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file with multiple pages
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Click on Print Quality options
         8. Click on Print button

         Expected Results:
         7. Verifies print quality options ui, select each option and verify its select on
         8. Printing job can be printed success
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        self.common_preview.select_print_quality_option(self.common_preview.PRINT_QUALITY_BEST_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_print_quality_selected_value() == "Best"
        self.common_preview.select_print_quality_option(self.common_preview.PRINT_QUALITY_DRAFT_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_print_quality_selected_value() == "Draft"
        self.common_preview.select_print_quality_option(self.common_preview.PRINT_QUALITY_NORMAL_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_print_quality_selected_value() == "Normal"
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_verify_print_2sided(self):
        """
        Descriptions: C31297393, C31297362, C31297363, C31297364, C35855648
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
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, "test_reg_file_2", no_of_pages=2)
        self.fc.select_a_file_and_go_to_print_preview(file_name="test_reg_file_2")
        if self.common_preview.verify_2_sided_option(invisible=True, raise_e=False):
            pytest.skip("currently printer doesn't support two sided option")
        self.common_preview.select_2_sided_option(self.common_preview.TWO_SIDED_LONG_EDGE_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_2_sided_selected_value() == "Long Edge"
        self.common_preview.select_2_sided_option(self.common_preview.TWO_SIDED_SHORT_EDGE_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_2_sided_selected_value() == "Short Edge"
        self.common_preview.select_2_sided_option(self.common_preview.TWO_SIDED_OFF_OPTION)
        self.common_preview.select_navigate_back()
        assert self.common_preview.get_2_sided_selected_value() == "Off"
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=80)