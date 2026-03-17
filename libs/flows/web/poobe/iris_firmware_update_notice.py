from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare, string_validation


class IrisFWUpdateNotice(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE IRIS Firmware Update Notice only shown for Flex /connect flow
    """
    file_path = __file__
    flow_name = "iris_firmware_notice"
    

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_accept_auto_fw_updates(self):
        """
        Click on continue and confirm auto FW updates
        """
        self.driver.click("page_confirm_and_continue_button")

    def click_auto_update_radio_btn(self):
        """
        Click Auto Update(Recommended) button for firmware-update-notice page seen when decline HP+ for single SKU marconi flow.
        """
        self.driver.click("Auto_update_radio_btn")
    
    def click_cancel_and_manual_setup(self):
        """
        Click on Cancel and Setup manually Button.
        """
        self.driver.click("page_cancel_and_setup_manually_button")

    def click_continue_online_setup_overlay_model_btn(self):
        """
        clcik continue online setup Button on Are you sure overlay.
        """
        self.driver.click("modal_continue_online_setup_button")

    def click_cancel_online_setup_overlay_model_btn(self):
        """
        Verify continue online setup Button on Are you sure overlay.
        """
        self.driver.click("modal_cancel_online_setup_button")

    def click_close_fw_overlay(self):
        """
        click Close (x) on top right corner of overlay.
        """
        self.driver.click("close_popup_x")
    
    def handle_auto_firmware_update_notice_page(self):
        """
        This page shows up on /onboard flow so for marconi and kebin printers if users declines HP+ and skips Ink only then this page show as per
        Figma SMB Portal OOBE 1.4 (smb.stage.portalshell.int.hp.com/us/en/auto-firmware-update-notice)
        """
        self.driver.click("select_fw_auto_update_radio_btn", displayed=False)
        self.driver.click("fw_auto_update_notice_apply_btn", timeout=15)

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="fw_update_modal", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_fw_update_modal_page(self, displayed=True, raise_e=True, timeout=10):
        """
        Verify Firmware updates page.
        """
        return self.driver.wait_for_object("fw_update_modal", displayed=displayed, raise_e=raise_e, timeout=timeout)

    @string_validation("page_header")
    @string_validation("page_content")
    @string_validation("page_cancel_and_setup_manually_button")
    @string_validation("page_confirm_and_continue_button")
    def verify_fw_update_notice_content(self, raise_e=False):
        return self.driver.wait_for_object("page_header")
    
    @screenshot_compare(root_obj="page_content", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_hp_learn_url_fw_page(self):
        """
        Verify Printer Benefit FW Page Learn more details hp url.
        """
        self.driver.wait_for_object("hp_learn_url")

    @screenshot_compare(root_obj="cancel_and_setup_manually_modal", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_cancel_and_setup_manually_overlay(self):
        self.driver.wait_for_object("cancel_and_setup_manually_modal", timeout=20)
    
    def verify_cancel_and_setup_manually_modal(self):
        self.driver.wait_for_object("modal_header")
        self.driver.wait_for_object("modal_content_before_features")
        self.driver.wait_for_object("modal_content_after_features")
    
    def verify_continue_online_setup_pop_model_btn(self):
        """
        Verify continue online setup Button on Are you sure overlay.
        """
        self.driver.wait_for_object("modal_continue_online_setup_button")

    def verify_cancel_online_setup_pop_model_btn(self):
        """
        Verify Cancel Online setup button on Are you Sure you want to cancel Auto-fw update overlay.
        """
        self.driver.wait_for_object("modal_cancel_online_setup_button")

    @screenshot_compare(root_obj="fw_update_modal", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_overlay_close_btn(self):
        """
        Verify Close x button on top right corner of overlay.
        """
        self.driver.wait_for_object("close_popup_x")