import time
import logging
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

def ios_share_flow_factory(driver):
    os_version = driver.driver_info["platformVersion"].split(".")[0]
    for sub_cls in saf_misc.all_subclasses(Share):
        if saf_misc.is_abstract(sub_cls) or not getattr(sub_cls, "flow_name", False):
            continue
        if os_version in sub_cls.__name__:
            return sub_cls(driver)
    logging.warning("Cannot satisfy OS: {}".format(os_version))
    logging.warning("Returning default driver (Note if this doesn't work please overload method with child class)")
    return Share(driver)

class Share(SmartFlow):
    flow_name = "share"

    # ------------------------------------------  Action Methods ------------------------------------------
    def select_message(self):
        self.driver.click("message_btn")

    def select_mail(self):
        """
        Click on Mail on  share screen
        End of flow: New Message screen
        Device: Phone
        """
        self.driver.click("mail_btn", timeout=20)
        time.sleep(2)

    def select_gmail(self):
        """
        Click on Gmail on share screen
        End of flow: New Message screen
        Device: Phone
        """
        self.driver.scroll("gmail_btn", direction="right", scroll_object="share_app_carousel", click_obj=True)

    def dismiss_share_mail(self):
        """
        Dismiss Share Mail
        Steps:
            - Click on Cancel button
            - Click on Delete Draft
        """
        self.driver.click("cancel_btn")
        self.driver.click("delete_draft_btn")

    def select_save_to_hp_smart(self):
        self.driver.click("save_to_hp_smart_btn")

    def select_shared_albums(self):
        self.driver.click("add_to_shared_albums")
    
    def select_print_with_hp_smart(self):
        self.driver.click("print_with_hp_smart_option")
    
    def select_edit_actions(self):
        self.driver.click("edit_actions_link")
    
    def toggle_option_on_actions_screen(self, option, enable=True):
        self.verify_is_toggled(option, toggle_on_after_check=enable, raise_e=False)

    # ------------------------------------------  Verification Methods ------------------------------------------
    def verify_share_popup(self):
        if pytest.platform == "IOS":
            self.driver.wdvr.execute_script("mobile: swipe", {"direction": "up",
                                            "element": self.driver.wait_for_object("share_popup")})
        self.driver.wait_for_object("share_popup")
    
    def verify_option_present(self, option, raise_e=False):
        return self.driver.wait_for_object(option, raise_e=raise_e)