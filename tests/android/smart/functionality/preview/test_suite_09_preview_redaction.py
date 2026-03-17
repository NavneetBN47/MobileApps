import pytest

from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc


pytest.app_info = "SMART"


class Test_Suite_09_Preview_Redaction(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.redaction = cls.fc.flow[FLOW_NAMES.REDACTION]

        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=False, smart_advance=False, pro=True)

    def test_01_redaction_navigation(self):
        """
        Description: C31299675, C31299677 & C31299678
         1. Load to Redaction screen with two images
         2. Select Next button on Coachmark
         3. Select Next button on Coachmark
         4. Select Next(✓) button on Coachmark
         5. Select Next page button
         6. Select Previous page button
        Expected Results:
         1. Verify First Coachmark
         2. Verify Second Coachmark
         3. Verify Third Coachmark
         4. Verify Coachmark is invisible
            Verify on First Page
         5. Verify on Second Page
         6. Verify on First Page
        """
        self.__load_redaction(dismiss_coachmark=False)
        for i in range(1, 4):
            self.redaction.verify_coachmark(coach_num=i)
            self.redaction.select_coachmark_button("next")
        self.redaction.verify_coachmark(invisible=True)
        self.redaction.verify_current_page(page_num=1)
        self.redaction.select_button("next")
        self.redaction.verify_current_page(page_num=2)
        self.redaction.select_button("previous")
        self.redaction.verify_current_page(page_num=1)

    def test_02_reset_undo_redaction(self):
        """
        Description: C31299682 & C31299683, C31299681
         1. Load to Redaction screen with two images
         2. Long press redaction image
         3. Select undo button
         4. Long press redaction image
         5. Select Next page button
         6. Long press redaction image
         7. Select Reset button
         8. Select Cancel button
         9. Select Reset button
         10. Select Done button
        Expected Results:
         2. Verify Image changed
         3. Verify Image changed
         4. Verify Image changed
         6. Verify Image changed
         7. Verify Confirmation Popup
         8. Verify Confirmation Popup is Invisible
         9. Verify Confirmation Popup
         10. Verify Images are same as they were initially
        """
        self.__load_redaction()
        init_imgs = [self.redaction.screenshot_img()]
        self.redaction.select_button("next")
        init_imgs.append(self.redaction.screenshot_img())
        self.redaction.select_button("previous")
        self.redaction.perform_redaction()
        redacted_img = self.redaction.screenshot_img()
        assert saf_misc.img_comp(init_imgs[0], redacted_img) > 0.01, "Redaction image should have changed"
        self.redaction.select_button("undo")
        reverted_img = self.redaction.screenshot_img()
        self.redaction.perform_redaction()
        assert saf_misc.img_comp(reverted_img, self.redaction.screenshot_img()) > 0.01, "Redaciton image should have changed"
        self.redaction.select_button("reset")
        self.redaction.verify_confirmation_popup()
        self.redaction.select_confirmation_popup_button("cancel")
        self.redaction.verify_confirmation_popup(invisible=True)
        self.redaction.select_button("next")
        assert saf_misc.img_comp(init_imgs[1], self.redaction.screenshot_img()) < 0.06, "Redaction image 2 should match initial image"
        self.redaction.select_button("previous")
        saf_misc.img_comp(init_imgs[1], self.redaction.screenshot_img()) < 0.06, "Redaciton image 1 should match initial image"

    @pytest.mark.parametrize("btn", ["done", "cancel"])
    def test_03_redaction_end_to_end(self, btn):
        """
        Description: C31299679, C31299684 & C31299685, C31299676
         1. Load to Redaction screen with two images
         2. Long press redaction image
         3. Select Next page button
         4. Long press redaction image
         5. Select Done button
         6. Select Done or Cancel button
        Expected Results:
         5. Confirmation popup appeared
         6. If btn == "done"
             Verify Preview Images changed
            If btn == "cancel"
             Verify redaction screen
        """
        self.__load_preview()
        if btn == "done":
            init_preview_images = self.preview.screenshot_all_preview_images()
        self.preview.select_top_toolbar_btn(self.preview.REDACTION_BTN)
        if self.redaction.verify_coachmark(raise_e=False):
            self.redaction.select_coachmark_button("close")
        self.redaction.perform_redaction()
        self.redaction.select_button("next")
        self.redaction.perform_redaction()
        self.redaction.select_button("done")
        self.redaction.verify_confirmation_popup()
        self.redaction.select_confirmation_popup_button(btn)
        if btn == "done":
            for i, imgs in enumerate(zip(init_preview_images, self.preview.screenshot_all_preview_images())):
                init, edited = imgs
                assert saf_misc.img_comp(init, edited) != 0.00, f"Preview image {i + 1} should have changed"
        else:
            self.redaction.verify_redaction_screen()

    def __load_preview(self, pages=2):
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages(number_pages=pages)
        self.preview.verify_title(self.preview.PREVIEW_TITLE)

    def __load_redaction(self, pages=2, dismiss_coachmark=True):
        self.__load_preview(pages=pages)
        self.preview.select_top_toolbar_btn(self.preview.REDACTION_BTN)
        if dismiss_coachmark and self.redaction.verify_coachmark(raise_e=False):
            self.redaction.select_coachmark_button("close")