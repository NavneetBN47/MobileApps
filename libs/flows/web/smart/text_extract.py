import pytest

from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from SAF.misc import saf_misc

from selenium.common.exceptions import ElementNotInteractableException


class TextExtract(SmartFlow):
    flow_name = "text_extract"

    # -------------------------------------------------------- Action Methods --------------------------------------------------------
    def select_done(self):
        """
        Selects the done button
        """
        self.driver.click("done_btn")

    def select_copy_all(self):
        """
        Selects the Copy All button
        """
        self.driver.click("copy_all_btn")

    # ----------------------------------------------------- Verification Methods -----------------------------------------------------
    def verify_text_extract_screen(self, timeout=20):
        """
        Verifies the Text Extract screen
        """
        self.driver.wait_for_object("text_extract_title", timeout=timeout)
        self.driver.wait_for_object("done_btn", timeout=timeout)
        self.driver.wait_for_object("copy_all_btn", timeout=timeout)

    def verify_text_copied_popup(self):
        """
        Verifies the "Text copied to clipboard" popup
        """
        self.driver.wait_for_object("copied_txt")
