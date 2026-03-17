import pytest

from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from SAF.misc import saf_misc

from selenium.common.exceptions import ElementNotInteractableException


class Redaction(SmartFlow):
    flow_name = "redaction"

    # -------------------------------------------------------- Action Methods --------------------------------------------------------
    def select_button(self, btn):
        """
        Selects a button on the bottom toolbar
        :param btn: The button to select. "next", "previous", "reset", "undo", "done" or "cancel"
        """
        if btn not in ["next", "previous", "reset", "undo", "done", "cancel"]:
            raise ValueError(f"Invalid button: {btn} given to select_button()")
        self.driver.click(f"{btn}_btn")
    
    def select_confirmation_popup_button(self, btn):
        """
        Selects a button on the confirmation popup
        :param btn: The button to select. "done" or "cancel"
        """
        # Must try clicking all instances of the button
        for btn in [e for e in self.driver.find_object(f"confirm_popup_{btn}_btn", multiple=True) if e.is_displayed and len(e.text) > 0]:
            try:
                btn.click()
                return True
            except ElementNotInteractableException:
                pass
        raise ElementNotInteractableException(f"Could not click confirm_popup_{btn}_btn")

    def select_coachmark_button(self, btn):
        """
        Selects a button on the coachmark
        :param btn: The button to select. "next", "previous" or "close
        """
        self.driver.click(f"coachmark_{btn}_btn")

    def perform_redaction(self):
        """
        Performs a redaction. Long press and drag.
        NOTE: Switches to native context to guarantee accurate screen dimensions.
        """
        self.driver.switch_to_webview("NATIVE_APP")
        rect = self.driver.wdvr.get_window_rect()
        position = [int((rect["width"] / 2) * 0.7), int((rect["height"] / 2) * 0.7)]
        redaction_size = 0.3  # redaction size as percent of screen size
        touch_action = self.driver.touch_action.long_press(x=position[0], y=position[1], duration=3000)
        if pytest.platform.lower() == "ios":  # iOS image will pan if moving too quickly. No way to set duration of move_to so moving bit by bit with delays between
            step_size = (int(rect["width"] * 0.05), int(rect["height"] * 0.05))
            for _ in range(int(redaction_size / 0.05)):
                position[0] += step_size[0]
                position[1] += step_size[1]
                touch_action = touch_action.move_to(x=position[0], y=position[1]).wait(250)
        else:
            touch_action.move_to(x=int(position[0] + rect["width"] * redaction_size), y=int(position[1] + rect["height"] * redaction_size))
        touch_action.wait(1000).release().perform()
        
    # ----------------------------------------------------- Verification Methods -----------------------------------------------------
    def verify_current_page(self, page_num=None):
        """
        Verifies the current page number.
        :param page_num: The expected page number. Indexed at 1.
        """
        current_page_num = int(self.driver.wait_for_object("page_number_txt").text.split(" ")[0].strip())
        if page_num is None:
            return current_page_num
        assert page_num == current_page_num, f"Current page {current_page_num} is not expected page {page_num}"
    
    def verify_redaction_screen(self):
        """
        Verify the redaction screen
         - redaction title text
         - redaction image
         - cancel button
         - done button
         - next page button
         - previous page button
         - reset button
         - page number text
        """
        self.driver.wait_for_object("title_txt")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("done_btn")
        self.driver.wait_for_object("next_btn")
        self.driver.wait_for_object("previous_btn")
        self.driver.wait_for_object("reset_btn")
        self.driver.wait_for_object("page_number_txt")

    def verify_coachmark(self, coach_num=None, invisible=False, raise_e=True):
        """
        Verifies the redaction coachmark that appears on first launch
         - text
         - sub text
         - close button
         - next button
         - previous button
        :param coach_num: The expected coachmark. Indexed at 1.
        """
        if not invisible:
            coach_sub_txt = self.driver.wait_for_object("coachmark_sub_txt", raise_e=raise_e)
            if coach_sub_txt is False:
                return False
            current_coach_num = int(coach_sub_txt.text.split(" ")[0].strip())
            if coach_num is None:
                coach_num = current_coach_num
            else:
                assert coach_num == current_coach_num
        return self.driver.wait_for_object("coachmark_txt", invisible=invisible, raise_e=raise_e) is not False and \
            self.driver.wait_for_object("coachmark_close_btn", invisible=invisible, raise_e=raise_e) is not False and \
            self.driver.wait_for_object("coachmark_next_btn", invisible=invisible, raise_e=raise_e) is not False and \
            self.driver.wait_for_object("coachmark_previous_btn", invisible=invisible if invisible else coach_num == 1, raise_e=raise_e) is not False

    def verify_confirmation_popup(self, invisible=False):
        """
        Verifies the undo/reset confirmation popup
         - header text
         - body text
         - done button
         - cancel button
        """
        self.driver.wait_for_object("confirm_popup_header_txt", displayed=False)
        # objects invisible state is always False, objects are "invisible" when their text is empty
        is_invis = lambda elements: len([e for e in elements if e.is_displayed and len(e.text) > 0]) == 0
        for locator in ["confirm_popup_header_txt", "confirm_popup_body_txt", "confirm_popup_done_btn", "confirm_popup_cancel_btn"]:
            assert is_invis(self.driver.find_object(locator, multiple=True)) == invisible, f"{locator} should{'' if invisible else ' not'} have empty text"

    def screenshot_img(self):
        """
        Screenshots the redaction image.
        NOTE: Requires native context locator for "redaction_img".
        """
        self.driver.switch_to_webview("NATIVE_APP")
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("redaction_img"))


class IOSRedaction(Redaction):

    context = "NATIVE_APP"

    def select_button(self, btn):
        """
        Selects a button on the bottom toolbar
        :param btn: The button to select. "next", "previous", "reset", "undo", "done" or "cancel"
        """
        self.driver.click(f"{btn}_btn")
    
    def verify_previous_btn_enabled(self, enabled=True):
        """
        Verifies if previous_btn is enabled when next_btn is selected
        """
        if enabled:
            self.driver.wait_for_object("previous_btn_enabled")
        else:
            assert not self.driver.wait_for_object("previous_btn_enabled", raise_e=False)