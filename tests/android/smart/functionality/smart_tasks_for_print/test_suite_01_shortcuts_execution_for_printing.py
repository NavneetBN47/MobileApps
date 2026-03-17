from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
import datetime

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Shortcuts_Execution_For_Printing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.print_preview = cls.fc.flow[FLOW_NAMES.PRINT_PREVIEW]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_execute_shortcuts_with_color_single_print(self):
        """
        Requirements:
          1. C31461734	Source selection dialog when Printer is selected 
          2. C31461721	"Your file is being uploaded for processing" pop up 
          3. C31461738	"Your file is processing" pop up 
          4. C31461723	"Home" button behavior from Your file is processing pop up
          5. C31461725	"Your file is processing" pop up when "Quick Run" is enabled 
          6. C31461726	"Your file is processing" pop up when "Quick Run" is enabled with print 
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a new shortcut screen for single/color print with different printing settings
          5. Start a shortcut from step4
          6. If print_option is two_sided_off, then click Camera from  source files
          7. - If from Camera, then click capture screenshot with manual mode
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

        Expected Result:
          8. Verify Shortcuts send success screen popup:
             - Message
             - Home button
             - More Option button
             - Activity button
          9. Verify Home screen
        """
        shortcuts_name = "{}_{}_{:%H_%M_%S}".format(self.udid, "color_two_side", (datetime.datetime.now()))
        self.__load_shortcuts_source_files_through_print(self.shortcuts.SINGLE_COPIES_BTN, self.shortcuts.COLOR_BTN, self.shortcuts.OFF_BTN, shortcuts_name,
                                                    is_invisible=True)
        self.shortcuts.click_camera_btn()
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT, mode="document")
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.shortcuts.verify_shortcuts_start_preview_screen()
        self.shortcuts.click_start_btn()
        self.print_preview.verify_print_preview_screen()
        self.preview.select_print_btn()
        self.driver.back()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen()
        self.shortcuts.click_more_options_btn()
        self.preview.verify_bottom_nav([self.preview.SAVE_BTN, self.preview.SHARE_BTN])

    def test_02_execute_shortcuts_with_black_multiple_print(self):
        """
        Requirements:
          1. C31461718	'Printer Scan' button redirection from Select a Source pop-up
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a new shortcut screen for single/color print with different printing settings
          5. Start a shortcut from step4
          6. If print_option is two_sided_off, then click Camera from  source files
          7. - If from Camera, then click capture screenshot with manual mode
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

        Expected Result:
          8. Verify Shortcuts send success screen popup:
             - Message
             - Home button
             - More Option button
             - Activity button
          9. Verify Home screen
        """
        shortcuts_name = "{}_{}_{:%H_%M_%S}".format(self.udid, "black_multiple", (datetime.datetime.now()))
        self.__load_shortcuts_source_files_through_print(self.shortcuts.MULTIPLE_COPIES_BTN, self.shortcuts.GRAYSCALE_BTN, self.shortcuts.SHORT_EDGE_BTN, shortcuts_name,
                                                    is_invisible=True)
        self.shortcuts.click_scanner_btn()
        self.scan.dismiss_coachmark()
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.shortcuts.verify_shortcuts_start_preview_screen()
        self.shortcuts.click_start_btn()
        self.print_preview.verify_print_preview_screen()
        self.preview.select_print_btn()
        self.driver.back()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen()
        self.shortcuts.click_shortcuts_home_btn()
        self.home.verify_home_nav()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_shortcuts_source_files_through_print(self, copies_num, color_btn, two_sided_option, shortcuts_name, is_invisible=False):
        """
        - Load Home screen.
        - CLick on Shortcuts tile on Home screen
        - Click on Add Shortcut button
        - Click on Create your own Shortcut button
        - Click on Print button
        - Select Copies, Color, Two-sided option
        """
        self.fc.reset_app()
        self.fc.flow_home_load_shortcuts_screen(create_acc=False, printer_obj=self.p)
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_print(is_new=True, copies_num=copies_num, color_btn=color_btn, two_sided_option=two_sided_option)
        self.fc.flow_save_shortcuts(invisible=is_invisible, shortcuts_name=shortcuts_name)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()