import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_07_Photo_Edit_Print_Share(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.edit = cls.fc.fd["edit"]
        cls.preview = cls.fc.fd["preview"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.stack = request.config.getoption("--stack")
        cls.gmail = cls.fc.fd["gmail"]
        cls.gmail_api = cls.fc.fd["gmail_api"]
        cls.share = cls.fc.fd["share"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]
    
        cls.p = load_printers_session

        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_01_add_edit_print_photos(self):
        """
        Description: C27152696, C17029648
            1. Launch the Smart app
            2. Scan or Select single and proceed to the landing screen
            3. Perform some edits on the images (crop, text, color change etc)
            4. Tap on Done to save the edit changes.
            5. Submit a print job
         
        Expected Results:
            Verify that the print job is successful with all the edit changes and the print matches the preview
        """
        self.fc.go_to_edit_screen_with_selected_photo()
        original_img = self.common_preview.verify_preview_img()
        # perform edits
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATest")
        self.edit.select_edit_done()
        self.edit.select_edit_text_options(self.edit.TEXT_COLOR, self.edit.TEXT_COLOR_OPTIONS[3])
        self.edit.select_text_color(self.edit.TEXT_COLOR_OPTIONS[2])
        self.edit.select_edit_done() # Finished color Selection
        self.edit.select_edit_done() # Finished color button selection
        self.edit.select_edit_done() # Finished edits
        # verify image changed
        assert abs(self.edit.edit_img_comparision(original_img, self.common_preview.verify_preview_img())) > 0.06, "Preview image should not match original image"
        self.fc.select_print_button_and_verify_print_job(self.p)
        
    def test_02_photos_share_gmail(self):
        """
        C28299202
        Description:
            1. Navigate to Home Screen
            2. Tap on the "Camera Scan" Tile Or select a photo from MY Photo screen
            3. From Adjust Boundaries Screen, Tap on Next
            4. From the Preview screen, tap anywhere on the photo to edit.
            5. Perform the below actions on the clicked photo: 
                a.) Edit a photo 
                b.) Apply a filter 
                c.) Add some adjustments (brightness, contrast, etc) e.) Add text 
            6. After performing the above actions, tap on "Done"
            7. Go back to Files and Photos Screen
            8. Select the same Photo/ File
            9. From the preview Screen, tap on the Photo/file
            10. Observe
            11. Share the Photo/ File using Gmail, PSP, Save to Drive, Messages, Blue Tooth
            12. Observe
        NOTE: Perform the same steps (Step 3 - Step 12) for Printer Scan
        """
        self.fc.go_to_edit_screen_with_selected_photo()
        # Filter image
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.select_edit_main_option(self.edit.FILTER_PHOTO)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_child_option(self.edit.FILTER_PHOTO_OPTIONS[3], direction="right", check_end=False)
        self.edit.verify_and_swipe_adjust_slider(direction="right", per_offset=0.25)
        new_image = self.edit.edit_img_screenshot()
        assert (self.edit.edit_img_comparision(current_image, new_image) != 0), "Filters photo type didn't change successfully"
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        # Adjust image
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.verify_screen_title(self.edit.ADJUST)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        original_img = self.common_preview.verify_preview_img()
        self.edit.select_edit_child_option(self.edit.ADJUST_OPTIONS[0], direction="right", check_end=False)
        self.edit.verify_and_swipe_adjust_slider(direction="left", per_offset=0.25)
        new_img = self.common_preview.verify_preview_img()
        # verify image changed
        assert self.edit.edit_img_comparision(original_img, new_img) != 0, "Adjust type doesn't select success"
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_done() # done editing
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.verify_title(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.select_action_btn()
        self.share.select_gmail()
        subject = "{}_{}".format("test_02_photos_share_gmail", self.driver.driver_info["udid"])
        self.gmail.compose_and_send_email(self.email_address, subject_text=subject)
        msg_id = self.gmail_api.search_for_messages(q_from=self.email_address,
                                                    q_to=self.email_address, q_unread=True,
                                                    q_subject=subject, timeout=300)
        attachment_names = self.gmail_api.get_attachments(msg_id[0][u'id'])
        for index, name in enumerate(attachment_names):
            temp_name = name.split("-")
            attachment_names[index] = "_".join(temp_name)
        self.gmail_api.delete_email(msg_id)
        assert len(attachment_names) == 1