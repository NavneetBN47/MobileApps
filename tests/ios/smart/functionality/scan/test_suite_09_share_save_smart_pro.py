import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "SMART"

class Test_Suite_09_Share_Save_Smart_Pro(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session

        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.camera = cls.fc.fd["camera"]
        cls.files = cls.fc.fd["files"]
        cls.redaction = cls.fc.fd["redaction"]

        cls.stack = request.config.getoption("--stack")
        cls.signed_in_gdrive = False
        ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", pro=True, driver=cls.driver)
        cls.fc.go_home(stack=request.config.getoption("--stack"))
        cls.fc.go_hp_smart_files_and_delete_all_files()

    def test_01_share_save_invalid_password(self):
        '''
        C31299650: [PRO USER] Verify Share/Save UI 
        C31299651: [PRO USER] Enabling Add Password Protection toggle
        C31299652: [PRO USER] User enters less than 6 character password
        C31299658: [PRO USER] User enters more than 32 character password
        C31299659: [PRO USER] User enters a password which is too short and contains spaces
        C31299660: [PRO USER] User enters a password which is too long and contains spaces
        C31299661: [PRO USER] User enters a password which is between 6 to 32 character and contains spaces
        '''
        # valid: 6 - 32 characters password without space
        invalid_pwds = {
            self.common_preview.SHORT_PWD_HINT: "abc12",
            self.common_preview.SHORT_PWD_SPACES_HINT: "ab 12",
            self.common_preview.LONG_PWD_HINT: "abcdefghijklmnopqrstuvwxyz123456789",
            self.common_preview.LONG_PWD_SPACES_HINT: "abcde fghijklmnopqrstuv wxyz123456789",
            self.common_preview.PWD_SPACES_HINT: "abcdefg 1234"
        }
        self.fc.go_camera_screen_from_home()
        self.fc.multiple_manual_camera_capture(number=1)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.verify_action_screen(pro=True)
        for pwd_type, pwd in invalid_pwds.items():
            self.common_preview.toggle_pdf_password(enable=False)
            self.common_preview.toggle_pdf_password(enable=True)
            self.common_preview.verify_pdf_password()
            self.common_preview.enter_pdf_password(pwd)
            self.common_preview.select_action_btn()
            self.common_preview.verify_hint(pwd_type)
            logging.info("Verified proper message for {} password".format(pwd_type))
    
    def test_02_share_save_valid_password(self):
        '''
        C31299653: [PRO USER] Enter password and save (happy path)
        C31299654: [PRO USER] Try to access saved password protected file(happy path)
        '''
        self.fc.go_camera_screen_from_home()
        self.fc.multiple_manual_camera_capture(number=1)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.verify_action_screen(pro=True)
        file_name = self.test_02_share_save_valid_password.__name__
        valid_password = "abc1234"
        self.common_preview.rename_file(file_name)
        self.common_preview.toggle_pdf_password()
        self.common_preview.verify_pdf_password()
        self.common_preview.enter_pdf_password(valid_password)
        self.common_preview.select_action_btn()
        self.fc.save_file_and_handle_pop_up(go_home=True)
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists("{}.pdf".format(file_name))
        self.files.select_a_file("{}.pdf".format(file_name))
        self.files.dismiss_feedback_pop_up()
        self.files.verify_password_protected_popup()
        self.files.enter_password(valid_password)
        self.common_preview.verify_preview_screen()

    def test_03_wrong_pwd_and_cancel_func(self):
        """
        C31299655: [PRO USER] User enters wrong password when accessing protected file 
        C31299656: [PRO USER] Cancel button on pop up when accessing protected file
        """
        self.fc.go_to_home_screen()
        self.fc.go_hp_smart_files_screen_from_home()
        file_name = self.test_02_share_save_valid_password.__name__
        self.files.verify_file_name_exists("{}.pdf".format(file_name))
        self.files.select_a_file("{}.pdf".format(file_name))
        # wrong password validation
        wrong_password = "1234abc"
        self.files.dismiss_feedback_pop_up()
        self.files.verify_password_protected_popup()
        self.files.enter_password(wrong_password)
        self.files.verify_incorrect_password_txt()
        # cancel btn validation
        self.files.select_cancel()
        self.files.select_cancel()
        self.files.verify_hp_smart_files_screen()

    def test_04_smart_file_name(self):
        '''
        C31299592: Language section is not shown for basic file types
        C31299595: Language section is shown when user enables Smart File Name
        C31299596: Coachmark is shown when Language option show up
        '''
        self.fc.go_camera_screen_from_home()
        self.fc.multiple_manual_camera_capture(number=1)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.verify_action_screen(pro=True)
        assert self.common_preview.verify_selected_language(raise_e=False) is False
        self.common_preview.toggle_smart_file_name(enable=True)
        assert self.common_preview.verify_selected_language() == 'en_US', "Selected Language should be en_US"
        self.common_preview.select_language_info_btn()
    
    def test_05_redaction_ui(self):
        """
        Description: C31299675, C31299676, C31299677 & C31299678
         1. Load to Preview screen with 4 images
         2. Select Redaction button
         3. Select Continue button
         4. Select Next button on Coachmark
         5. Select Next button on Coachmark
         6. Select Next(✓) button on Coachmark
         7. Select Next page button
         8. Select Previous page button
        Expected Results:
         2. Verify "Processing pages" popup
         3. Verify First coachmark
         4. Verify Second coachmark
         5. Verify Third Coachmark
         6. Verify First page
         7. Verify Second page
         8. Verify First Page
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(4)
        self.common_preview.select_top_toolbar_btn(self.common_preview.REDACTION_BTN)
        self.common_preview.select_continue()
        self.redaction.verify_coachmark(coach_num=1)
        self.redaction.select_coachmark_button("next")
        self.redaction.verify_coachmark(coach_num=2)
        self.redaction.select_coachmark_button("next")
        self.redaction.verify_coachmark(coach_num=3)
        self.redaction.select_coachmark_button("checkmark")
        self.redaction.verify_current_page(page_num=1)
        self.redaction.select_button("next")
        self.redaction.verify_previous_btn_enabled()
        self.redaction.select_button("previous")
        self.redaction.verify_previous_btn_enabled(enabled=False)

    def test_06_redaction_reset_undo(self):
        """
        Description: C31299681, C31299682 & C31299683
         1. Load Redaction screen with 2 images
         2. Redact some content on First page
         3. Select Next button
         4. Redact some content on Second page
         5. Select Undo button
         6. Redact some content on Second page
         7. Select Reset button
         8. Select Cancel button
         9. Select Reset button
         10. Select Done button
        Expected Results:
         5. Verify First page has redaction(Doesn't match initial image)
            Verify Second page has no redaction(Does match initial image)
         7. Verify popup
         8. Verify First and Second page have redaction(Dont match initial image)
         10. Verify First and Second page do not have redaction(Matches initial image)
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(2)
        self.common_preview.select_top_toolbar_btn(self.common_preview.REDACTION_BTN)
        self.common_preview.select_continue()
        if self.redaction.verify_coachmark(raise_e=False):
            self.redaction.select_coachmark_button("close")
        init_imgs = [self.redaction.screenshot_img()]
        self.redaction.perform_redaction()
        self.redaction.select_button("next")
        init_imgs.append(self.redaction.screenshot_img())
        self.redaction.perform_redaction()
        self.redaction.select_button("undo")
        assert saf_misc.img_comp(self.redaction.screenshot_img(), init_imgs[1]) < 0.06, "Redaction page 2 should match initial image after undo"
        self.redaction.select_button("previous")
        assert saf_misc.img_comp(self.redaction.screenshot_img(), init_imgs[0]) > 0.06, "Redaction page 1 should not match initial image"
        self.redaction.select_button("next")
        self.redaction.perform_redaction()
        self.redaction.select_button("reset")
        self.redaction.verify_confirmation_popup()
        self.redaction.select_confirmation_popup_button("cancel")
        assert saf_misc.img_comp(self.redaction.screenshot_img(), init_imgs[1]) > 0.06, "Redaction page 2 should not match initial image"
        self.redaction.select_button("previous")
        assert saf_misc.img_comp(self.redaction.screenshot_img(), init_imgs[0]) > 0.06, "Redaction page 1 should not match initial image"
        self.redaction.select_button("reset")
        self.redaction.select_confirmation_popup_button("done")
        assert saf_misc.img_comp(self.redaction.screenshot_img(), init_imgs[0]) < 0.06, "Redaction page 1 should match initial image after reset"
        self.redaction.select_button("next")
        assert saf_misc.img_comp(self.redaction.screenshot_img(), init_imgs[1]) < 0.06, "Redaction page 2 should match initial image after reset"

    def test_07_redaction_end_to_end(self):
        """
        Description: C31299685 & C31299684
         1. Load to Redaction screen with two images
         2. Dismiss Coachmarks if present
         3. Long press on redaction image
         4. Select Next page
         5. Long press on redaction image
         6. Select Done button
         7. Select Cancel button
         8. Select Done button
         9. Select Done button
        Expected Results:
         6. Verify "Are you sure you want to delete?" popup
         7. Verify Redaction screen
         9. Verify Preview images have changed
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(2)
        self.common_preview.verify_preview_screen()
        self.common_preview.swipe_to_page(1)
        init_imgs = [self.common_preview.verify_preview_img()]
        self.common_preview.swipe_to_page(2)
        init_imgs.append(self.common_preview.verify_preview_img(page_number=2))
        self.common_preview.select_top_toolbar_btn(self.common_preview.REDACTION_BTN)
        self.common_preview.verify_title(self.common_preview.REDACTION_TITLE)
        self.common_preview.select_continue()
        if self.redaction.verify_coachmark(raise_e=False):
            self.redaction.select_coachmark_button("close")
        self.redaction.perform_redaction()
        self.redaction.select_button("next")
        self.redaction.perform_redaction()
        self.redaction.select_button("done")
        self.redaction.verify_confirmation_popup()
        self.redaction.select_confirmation_popup_button("cancel")
        self.redaction.select_button("done")
        self.redaction.select_confirmation_popup_button("done")
        self.common_preview.verify_preview_screen()
        for i, img in enumerate(init_imgs):
            page_number = i + 1
            self.common_preview.swipe_to_page(page_number)
            assert saf_misc.img_comp(img, self.common_preview.verify_preview_img(page_number=page_number)) > 0.06, f"Preview image {page_number} should have changed after redaction"

    def test_08_text_extract_camera(self):
        '''
        text extract functionality: redirection to text extraction page (success) or a text not detected popup (fail)
        C31299598: Text Extract option in Camera scan
        C31299599: Capture a file by Text Extract
        C31299601: Continue button redirection
        '''
        self.fc.go_camera_screen_from_home()
        self.camera.select_preset_mode(self.camera.TEXT_EXTRACT)
        self.camera.select_capture_btn()
        self.common_preview.verify_title(self.common_preview.TEXT_EXTRACT_TITLE)
        self.common_preview.select_continue()
    
    def test_09_text_extract_preview(self):
        '''
        C31299620: Text Extract from Document option
        '''
        self.fc.go_camera_screen_from_home()
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.fc.multiple_manual_camera_capture(number=1)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_top_toolbar_btn(self.common_preview.TEXT_EXTRACT_BTN)
        self.common_preview.verify_title(self.common_preview.TEXT_EXTRACT_TITLE)
        self.common_preview.select_continue()
