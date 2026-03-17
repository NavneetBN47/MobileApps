from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
import datetime

pytest.app_info = "SMART"

class Test_Suite_01_Edit_Delete_Smart_Tasks(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.file_photo = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.photo = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)


    @pytest.mark.parametrize("edit_option", ["add_printing", "add_saving"])
    def test_01_edit_shortcuts(self, edit_option):
        """
        Requirements:
          1. C31461662 - Shortcuts Screen: Existing shortcuts
          2. C31461835	Verify shortcut list user experience 
          3. C31461836	Verify 3 button menu items for shortcut
          4. C31461840	Verify 'Edit Shortcut' screen
          5. C31461848	Tap Save button on 'Edit Print' screen
          6. C31461845 Verify 'Edit Email' screen
          7. C31461844	Tap 'Continue' button on Edit Shortcut screen
          8. C31461846	Verify 'Edit Save' screen
          9. C31461852	Tap Save button on 'Edit Save' screen 

        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a new shortcuts for email
          5. Click on More option button for Shortcuts from step4
          6. Click Edit button
             - add_printing: add printing option for executing smart tasks
             - add_saving: add saving option for executing smart tasks
             - If add_printing, then enable Print item for this smart task
             - If add_saving, then enable Save item for this smart task
          7. Click on Continue button
          8. Click on Save button
        Expected Result:
          4. The shortcuts shows on Shortcuts list
          5. Verify More Option screen with below item:
             - Start button
             - Edit button
             - Delete button
          6. Verify Edit screen
          8. Shortcuts can be saved success

        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format(edit_option, (datetime.datetime.now()))
        self.__load_shortcuts_edit_screen(self.email_address, shortcut_name)
        if edit_option == "add_printing":
            self.fc.add_create_you_own_shortcuts_for_print(False, self.shortcuts.SINGLE_COPIES_BTN, self.shortcuts.GRAYSCALE_BTN, self.shortcuts.OFF_BTN)
        else:
            self.fc.add_create_you_own_shortcuts_for_saving(is_new=False, is_google_drive=True)
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.click_continue_btn()
        self.shortcuts.verify_settings_screen()
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.verify_shortcut_saved_screen(timeout=15)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_list_screen()

    @pytest.mark.parametrize("delete_option", ["cancel_btn", "delete_btn"])
    def test_02_edit_shortcuts_delete(self, delete_option):
        """
        Requirements:
          1. C31461837	Verify delete shortcut confirmation pop up 
          2. C31461838	Verify delete shortcut functionality
          3. C31461843	Tap 'Delete' button on Edit Shortcut screen

        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a new shortcuts for email
          5. Click on More option button for Shortcuts from step4
          6. Click Edit button
          7. Click on Delete button
             - cancel_btn: Click on Cancel button
             - delete_btn: Click on Delete button

        Expected Result:
          6. Verify Smart Task delete popup:
             - Title
             - CANCEL button
             - DELETE button
          7. - cancel_btn: Verify Edit Shortcuts screen
             - delete_btn: Verify  Shortcuts lists
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format(delete_option, (datetime.datetime.now()))
        self.__load_shortcuts_edit_screen(self.email_address, shortcut_name)
        self.shortcuts.click_edit_delete_btn()
        self.shortcuts.verify_shortcut_delete_screen()
        if delete_option == "cancel_btn":
            self.shortcuts.click_delete_popup_cancel_btn()
            self.shortcuts.verify_edit_shortcut_screen()
        else:
            self.shortcuts.click_delete_popup_delete_btn()
            self.shortcuts.verify_shortcuts_list_screen(timeout=15)

    @pytest.mark.parametrize("cancel_edit_option", ["yes_btn", "no_btn"])
    def test_03_edit_shortcuts_cancelled(self, cancel_edit_option):
        """
        Requirements:
          1. C31461853	Verify cancel shortcut functionality under Edit Shortcuts screen
          2. C31461853	Verify cancel shortcut functionality under Edit Shortcuts screen
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for email
          5. Click Edit button for smart task from step4
          6. Click on Cancel button
          7. - yes_btn: Click on Yes, Cancel Edits button
             - no_btn: Click on No, Continue Edits button

        Expected Result:
          6. Verify Shortcuts edit cancel popup:
             - Title
             - Yes, Cancel Edits button
             - No, Continue Edits button
          7. - yes_btn: Verify Shortcuts list screen
             - no_btn: Verify Edit Shortcuts screen
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format(cancel_edit_option, (datetime.datetime.now()))
        self.__load_shortcuts_edit_screen(self.email_address, shortcut_name)
        self.shortcuts.click_cancel_btn()
        self.shortcuts.verify_shortcut_cancel_edits_popup()
        if cancel_edit_option == "yes_btn":
            self.shortcuts.click_edits_cancel_popup_yes_btn()
            self.shortcuts.verify_shortcuts_list_screen()
        else:
            self.shortcuts.click_edits_cancel_popup_no_btn()
            self.shortcuts.verify_edit_shortcut_screen()

    @pytest.mark.parametrize("print_remove_option", ["remove_btn", "cancel_btn"])
    def test_04_edit_shortcuts_for_print_remove(self, print_remove_option):
        """
        Requirements:
          1. C31461841	Verify 3 dot menu on 'Edit Shortcut' screen
          2. C31461842	Verify 'Edit Print' screen 
          3. C31461847	Tap Remove button on 'Edit Print' screen
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a shortcuts for print
          5. Click Edit button for shortcuts from step4
          6. Click on More option icon next to Print item
          7. Click on Edit button
          8. Click on Remove button
          9. - remove_btn: Click on Remove button
             - cancel_btn: Click on Cancel button, then click on Save button

        Expected Result:
          6. Verify More option screen with item:
             - Edit button
             - Remove button
          7. Verify Edit Print screen
          8. Verify Remove popup:
             - Title
             - Remove button
             - Cancel button
          9. - remove_btn: Verify Edit Shortcuts screen
             - cancel_btn: Verify Edit Print screen, then verify Edit Shortcut screen
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format(print_remove_option, (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_print(self.shortcuts.GRAYSCALE_BTN)
        self.fc.flow_save_shortcuts(shortcut_name, True)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.select_shortcut(shortcut_name, click_obj=False)
        self.shortcuts.select_shortcut_more_option(shortcut_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_shortcut_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_remove_btn()
        self.shortcuts.verify_shortcut_remove_edits_popup()
        if print_remove_option == "remove_btn":
            self.shortcuts.click_remove_popup_remove_btn()
        else:
            self.shortcuts.click_remove_popup_cancel_btn()
        self.shortcuts.verify_edit_shortcut_screen()

    @pytest.mark.parametrize("email_remove_option", ["remove_btn", "cancel_btn"])
    def test_05_edit_shortcuts_for_email_remove(self, email_remove_option):
        """
        Requirements:
          1. C31461849	Tap Remove button on 'Edit Email' screen 
          2. C31461850	Tap Save button on 'Edit Email' screen 
          3. C31461846	Verify 'Edit Save' screen 
          4. C31461852	Tap Save button on 'Edit Save' screen
          
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a shortcuts for email
          5. Click Edit button for shortcuts from step4
          6. Click on More option icon next to Print item
          7. Click on Edit button
          8. Click on Remove button
          9. - remove_btn: Click on Remove button
             - cancel_btn: Click on Cancel button, then click on Save button

        Expected Result:
          7. Verify Edit Email screen
          8. Verify Remove popup:
             - Title
             - Remove button
             - Cancel button
          9. - remove_btn: Verify Edit Shortcuts screen
             - cancel_btn: Verify Edit Email screen, then verify Edit Shortcut screen
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format(email_remove_option, (datetime.datetime.now()))
        self.__load_shortcuts_edit_screen(self.email_address, shortcut_name)
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_remove_btn()
        self.shortcuts.verify_shortcut_remove_edits_popup()
        if email_remove_option == "remove_btn":
            self.shortcuts.click_remove_popup_remove_btn()
        else:
            self.shortcuts.click_remove_popup_cancel_btn()
        self.shortcuts.verify_edit_shortcut_screen()

    @pytest.mark.parametrize("save_remove_option", ["remove_btn", "cancel_btn"])
    def test_06_edit_shortcuts_for_save_remove(self, save_remove_option):
        """
        Requiremens:
          1. C31461851	Tap Remove button on 'Edit Save' screen
          2. C31461851	Tap Remove button on 'Edit Save' screen 
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a shortcuts for save
          5. Click Edit button for shortcuts from step4
          6. Click on More option icon next to Print item
          7. Click on Edit button
          8. Click on Remove button
          9. - remove_btn: Click on Remove button
             - cancel_btn: Click on Cancel button, then click on Save button


        Expected Result:
          7. Verify Edit Save screen
          8. Verify Remove popup:
             - Title
             - Remove button
             - Cancel button
          9. - remove_btn: Verify Edit Shortcuts screen
             - cancel_btn: Verify Edit Save screen, then verify Edit Shortcut screen
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format(save_remove_option, (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_saving()
        self.fc.flow_save_shortcuts(shortcuts_name=shortcut_name, invisible=False)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.select_shortcut(shortcut_name, click_obj=False)
        self.shortcuts.select_shortcut_more_option(shortcut_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_shortcut_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_remove_btn()
        self.shortcuts.verify_shortcut_remove_edits_popup()
        if save_remove_option == "remove_btn":
            self.shortcuts.click_remove_popup_remove_btn()
        else:
            self.shortcuts.click_remove_popup_cancel_btn()
        self.shortcuts.verify_edit_shortcut_screen()

    def test_07_start_shortcuts_for_email(self):
        """
        Requirements:
          1. C31461839	Verify 'Start' functionality from 3 dot menu
          2. C31461727	Run already created shortcut (Email)
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a shortcuts for Email
          5. Click Start button for shortcuts from step4
          6. Click on File & Photos scan
          7. Click on X button
          8. Start this shortcut again
          9. Click on File & Photos option -> My Photo -> select a photo
          10. Click on Start button

        Expected Result:
          5. Verify Source selecting screen
          7. Verify Shortcut list screen
          10. Shortcuts can be started success
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format("start_shortcut", (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen(create_acc=False)
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_email(self.email_address)
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcut_name)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.verify_shortcuts_list_screen()
        self.shortcuts.select_shortcut(shortcut_name, click_obj=True)
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_x_btn()
        self.shortcuts.select_shortcut(shortcut_name, click_obj=True)
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_files_photo_btn()
        self.file_photo.select_local_item(self.file_photo.MY_PHOTOS_TXT)
        self.photo.select_recent_photo_by_index()
        self.shortcuts.verify_shortcuts_start_preview_screen()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen()

    def test_08_start_shortcuts_for_save(self):
        """
        Requirements:
          1. C31461737	"X" button behavior from Shortcuts page already created shortcut
          2. C31461728	Run already created shortcut (Print) (Quick Run Disabled)
          3. C31461729	Run already created shortcut (Save) 
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Shortcuts screen
          4. Create a shortcuts for Save
          5. Click Start button for shortcuts from step4

        Expected Result:
          5. Verify Source selecting screen
        """
        shortcut_name = "{}_{:%d_%H_%M_%S}".format("test_09", (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_saving()
        self.fc.flow_save_shortcuts(shortcuts_name=shortcut_name, invisible=False)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.select_shortcut(shortcut_name, click_obj=True)
        self.shortcuts.verify_source_select_popup()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_shortcuts_edit_screen(self, email_address, shortcuts_name, is_edit=True):
        """
        - Load Home screen.
        - CLick on Shortcuts tile on Home screen
        - Click on Add Shortcut button
        - Click on Create your own Shortcut button
        - Click on Email Or Print or Save button
        - Click on Add to Shorcut button
        - Click on
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_email(email_address)
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcuts_name)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.verify_shortcuts_list_screen()
        self.shortcuts.select_shortcut(shortcuts_name, click_obj=False)
        self.shortcuts.select_shortcut_more_option(shortcuts_name)
        if is_edit:
            self.shortcuts.click_edit_btn()
            self.shortcuts.verify_edit_shortcut_screen()
        else:
            self.shortcuts.click_delete_btn()
            self.shortcuts.verify_shortcut_delete_screen()