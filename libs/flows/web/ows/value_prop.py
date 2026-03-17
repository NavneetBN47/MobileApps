from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare

class ValueProp(OWSFlow):
    """
    base class for all value prop - contains common buttons and UI
    - generic buttons locators based on template, actual content depends on the value prop feature
    - https://docs.google.com/document/d/1x9kin_uQZP1DgaJeTaEHGt53oYZkZ_P9GOQ902zOPm0/edit
    """
    project = "ows"
    flow_name = "value_prop"

    def select_primary_btn(self, change_check=False, timeout=10):
        change_check={"wait_obj": "_shared_primary_btn", "invisible": True} if change_check else False
        self.driver.click("_shared_primary_btn", change_check=change_check, timeout=timeout)

    def select_secondary_btn(self, change_check=False, timeout=10):
        change_check={"wait_obj": "_shared_secondary_btn", "invisible": True} if change_check else False
        self.driver.click("_shared_secondary_btn", change_check=change_check, timeout=timeout)
    
    def select_tertiary_btn(self, timeout=10):
        self.driver.click("_shared_tertiary_btn", timeout=timeout)

    @screenshot_compare()
    def verify_ucde_create_hp_account_and_benefits_page(self):
        self.driver.wait_for_object("ucde_create_hp_account_and_benefits_page")

    def click_skip_btn_ucde_account_prop(self):
        self.driver.click("ucde_account_prop_skip_activation")

    def click_sign_in_btn(self):
        self.driver.click("ucde_account_prop_sign_in_btn")

    def click_create_account_btn(self):
        self.driver.click("ucde_account_prop_create_account_btn")

class OWSValueProp(ValueProp):
    """
    https://oss.hpconnectedpie.com/ucde/account-prop/
    """
    def verify_ows_value_prop_screen(self, tile=False, simple=False, timeout=10):
        self.driver.wait_for_object("_shared_primary_btn", timeout=timeout)
        if simple:
            return True
        self.driver.wait_for_object("_shared_secondary_btn")
        self.driver.wait_for_object("_shared_tertiary_btn")
        if tile:            
            self.driver.wait_for_object("image_carousel")
        else:
            self.driver.wait_for_object("background_image")
    
    def select_value_prop_buttons(self, index=0, timeout=10, change_check=False):
        """
        - 0: setup printer / Create account button
        - 1: use hp smart / Sign In button
        - 2: explore hp smart / Close button
        """
        if index == 0:
            self.select_primary_btn(timeout=timeout, change_check=change_check)
        elif index == 1: 
            self.select_secondary_btn(timeout=timeout, change_check=change_check)
        elif index == 2:
            self.select_tertiary_btn(timeout=timeout)
        else:
            raise ValueError("Must specify an index in the range 0-2")

class MobileValueProp(OWSValueProp):
    context = "NATIVE_APP"

    # methods for native app view ows value prop screen
    # inherited this from Webview OWS value prop to make less changes to the whole code base 
    # and at the same time the MobileValueProp can deal with both webview and appview properly.

    def verify_native_value_prop_screen(self):
        """
        In app value prop screen, scenario: select notification bell without sign in
        """
        self.driver.wait_for_object("_shared_sign_in")
        self.driver.wait_for_object("_shared_create_account")
        self.driver.wait_for_object("_shared_close")

    def verify_printer_setup_exit_setup_removed(self):
        """
        Verify "Printer Setup" and "Exit setup" option is removed from the Shell title bar
        """
        assert self.driver.wait_for_object("shell_title_printer_setup", raise_e=False) is False
        assert self.driver.wait_for_object("shell_title_exit_setup", raise_e=False) is False
        
    def verify_windows_ows_value_prop_screen(self, flip=False, raise_e=True):
        """
        Function for Windows testing only!
        Verify ows value prop screen without Skip for now button on flip region
        """
        if flip:
            assert self.driver.wait_for_object("_shared_tertiary_btn", timeout=30, raise_e=False) is False
            return self.driver.wait_for_object("_shared_secondary_btn", raise_e=raise_e, displayed=False) and \
            self.driver.wait_for_object("_shared_create_account", raise_e=raise_e, displayed=False)
        else:
            return self.driver.wait_for_object("_shared_primary_btn", timeout=30, raise_e=raise_e) and \
            self.driver.wait_for_object("_shared_secondary_btn", raise_e=raise_e) and \
            self.driver.wait_for_object("_shared_tertiary_btn", raise_e=raise_e)

    def select_native_value_prop_buttons(self, index=0, timeout=10, raise_e=True):
        """
        - 0: Create account button
        - 1: Sign In button
        - 2: Close button
        - 3: Skip for now button
        """
        btns = ["_shared_create_account", "_shared_sign_in", "_shared_close", "_shared_tertiary_btn"]
        return self.driver.click(btns[index], timeout=timeout, raise_e=raise_e, displayed=False)
        
    def verify_ows_ucde_value_prop_screen(self, raise_e=True):
        return self.driver.wait_for_object("_shared_sign_in", raise_e=raise_e) and \
            self.driver.wait_for_object("_shared_create_account", raise_e=raise_e) and \
            self.driver.wait_for_object("_shared_close", raise_e=raise_e)

########################################################################################################################
#                                    HPX Flows                                                                         #
########################################################################################################################


    def click_sign_btn_hpx(self):
        self.driver.click("sign_in_btn_hpx")
    
    def click_continue_as_guest_btn(self, raise_e=True):
        self.driver.click("continue_as_guest_btn_hpx", raise_e=raise_e)

    def verify_continue_as_guest_btn(self):
        """
        Verify the "Continue as guest" button is displayed
        """
        return self.driver.wait_for_object("continue_as_guest_btn_hpx", raise_e=False)

    def verify_sign_in_btn_hpx(self):
        """
        Verify the "Sign In" button is displayed
        """
        return self.driver.wait_for_object("sign_in_btn_hpx", raise_e=False)
    


class MacValueProp(MobileValueProp):

    def select_native_value_prop_buttons(self, index=0, timeout=3, raise_e=True):
        """
        - 0: Create account button
        - 1: Sign In button
        - 2: Close button
        - 3: Skip for now button
        """
        btns = ["_shared_create_account", "_shared_sign_in", "_shared_close", "_shared_tertiary_btn"]
        return self.driver.click_using_frame(btns[index], timeout=timeout, raise_e=raise_e)