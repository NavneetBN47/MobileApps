from MobileApps.libs.flows.web.cec.cec_flow import CECflow


class CustomEngagementCenter(CECflow):
    flow_name = "custom_engagement_center"

    SINGLE_COPIES_BTN = "single_copies_label"
    MULTIPLE_COPIES_BTN = "mul_copies_label"
    COLOR_BTN = "color_option"
    GRAYSCALE_BTN = "grayscale_option"
    OFF_BTN = "off_option"
    SHORT_EDGE_BTN = "short_edge_option"
    LONG_EDGE_BTN = "long_edge_option"

    def __init__(self, driver, context=None):
        super(CustomEngagementCenter, self).__init__(driver, context=context)

    # *********************************************************************************
    #                                ACTION FLOWS--Create Shortcuts                   *
    # *********************************************************************************

    def click_see_all(self):
        """
        Click on See All button on Home screen
        """
        self.driver.click("see_all_btn", timeout=30)

    def click_back_btn(self):
        """
        Click on Back button on See All screen
        """
        self.driver.click("back_btn")
    
    def click_view_plans_btn(self):
        """
        Click on View Plans button on under Never Run Out save tile screen
        """
        self.driver.click("view_plans_btn")

    def click_never_run_out_save_close_btn(self):
        """
        Click on Close button on under Never Run Out save tile screen
        """
        self.driver.click("never_run_out_save_close_btn")
    
    def click_never_run_out_save_tile(self):
        """
        Click on Never Run Out save tile
        """
        self.driver.click("never_run_out_save_item")

    def click_create_account_sign_in_btn(self):
        """
        Click on Create account or sign in button on under Unlock cloud Features tile screen
        """
        self.driver.click("create_account_sign_in_btn")

    def click_unlock_cloud_features_close_btn(self):
        """
        Click on Close button on under Unlock cloud Features tile screen
        """
        self.driver.click("unlock_cloud_features_close_btn")

    def click_create_account_btn(self):
        """
        Click on Create Account button on under Unlock cloud Features tile screen
        """
        self.driver.click("create_account_btn")

    def click_sign_in_btn(self):
        """
        Click on Sign In button on under Unlock cloud Features tile screen
        """
        self.driver.click("sign_in_btn")
    
    def click_back_btn_on_sign_in_or_create_account_screen(self):
        """
        Click on Back button on Sign in Or Create account screen
        """
        self.driver.click("create_account_sign_in_back_btn")
    
    def click_back_btn_do_more_with_hp_smart_screen(self):
        """
        Click on Back button on Do more with HP Smart screen
        """
        self.driver.click("back_btn_do_more_with_hp_smart_screen")

    def click_unlock_cloud_features_tile(self):
        """
        Click on Unlock cloud Features tile
        """
        self.driver.click("unlock_cloud_features_item")

    def click_shortcuts_save_time_learn_more_btn(self):
        """
        Click on Learn More button under Shortcuts save time tile screen
        """
        self.driver.click("shortcuts_save_time_learn_more_btn")

    def click_shortcuts_save_time_close_btn(self):
        """
        Click on Close button under Shortcuts save time tile screen
        """
        self.driver.click("shortcuts_save_time_close_btn")
    
    def click_shortcuts_save_time_tile(self):
        """
        Click on Shortcuts save time tile
        """
        self.driver.click("shortcuts_save_time_item")

    def click_try_camera_scan_learn_more_btn(self):
        """
        Click on Learn More button under Try camera scan tile screen
        """
        self.driver.click("try_camera_scan_learn_more_btn")

    def click_try_camera_scan_close_btn(self):
        """
        Click on Close button under Try camera scan tile screen
        """
        self.driver.click("try_camera_scan_close_btn")
    
    def click_try_camera_scan_tile(self):
        """
        Click on Try camera scan tile
        """
        self.driver.click("try_camera_scan_item")

    def click_view_all_feature_btn(self):
        """
        Click on View all feature button under Use hp smart advance tile screen
        """
        self.driver.click("view_all_feature_btn")

    def click_use_hp_smart_advance_close_btn(self):
        """
        Click on Close button under Use hp smart advance tile screen
        """
        self.driver.click("use_hp_smart_advance_close_btn")
    
    def click_use_hp_smart_advance_tile(self):
        """
        Click on Use hp smart advance tile
        """
        self.driver.click("use_hp_smart_advance_item")


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_cec_section(self):
        pass

    def verify_see_all_btn(self, timeout=20, raise_e=True):
        """
        Verify See All button on Home screen:
        """
        return self.driver.wait_for_object("see_all_btn", timeout=timeout, raise_e=raise_e)

    def verify_do_more_with_hp_smart_screen(self, timeout=20, raise_e=True):
        """
        Verify Do more with HP Smart screen:
        """
        return self.driver.wait_for_object("see_all_header", timeout=timeout, raise_e=raise_e)

    def verify_never_run_out_save_tile(self, invisible=False, displayed=False):
        """
        Verify Never Run out& Save tile displays on Do more with HP Smart screen:
        """
        self.driver.wait_for_object("never_run_out_save_item", invisible=invisible, displayed=displayed)

    def verify_unlock_cloud_features_tile(self, invisible=False, displayed=False, raise_e=True):
        """
        Verify Unlock cloud features tile displays on Do more with HP Smart screen:
        """
        return self.driver.wait_for_object("unlock_cloud_features_item", invisible=invisible, displayed=displayed, raise_e=raise_e)

    def verify_create_account_or_sign_in_screen(self):
        """
        Verify Create a account or Sign in screen via:
        + Title
        + Create Account button
        + Sign in button
        """
        self.driver.wait_for_object("create_account_sign_in_title")
        self.driver.wait_for_object("create_account_btn")
        self.driver.wait_for_object("sign_in_btn")

    def verify_shortcuts_save_time_tile(self, invisible=False):
        """
        Verify Shortcuts Save Time tile displays on Do more with HP Smart screen:
        """
        self.driver.wait_for_object("shortcuts_save_time_item", invisible=invisible, displayed=False)
    
    def verify_shortcut_save_time_screen(self):
        """
        Verify Shortcut Save Time screen via:
        + Title
        + Message
        + Got it button
        """
        self.driver.wait_for_object("shortcuts_save_time_title")
        self.driver.wait_for_object("shortcuts_save_time_message")
        self.driver.wait_for_object("got_it_btn")

    def verify_try_camera_scan_tile(self, invisible=False):
        """
        Verify Try Camera Scan tile displays on Do more with HP Smart screen:
        """
        self.driver.wait_for_object("try_camera_scan_item", invisible=invisible, displayed=False)
    
    def verify_try_camera_scan_screen(self):
        """
        Verify Try camera scan screen via:
        + Title
        + Message
        + Got it button
        """
        self.driver.wait_for_object("try_camera_scan_title")
        self.driver.wait_for_object("try_camera_scan_message")
        self.driver.wait_for_object("try_camera_scan_got_it_btn")

    def verify_use_hp_smart_advance_tile(self, invisible=False):
        """
        Verify Use HP Smart Advance tile displays on Do more with HP Smart screen:
        """
        self.driver.wait_for_object("use_hp_smart_advance_item", invisible=invisible)
    
    def verify_view_all_feature_screen(self):
        """
        Verify HP Smart Advance screen via:
        + Message
        """
        self.driver.wait_for_object("view_all_feature_message", displayed=False, timeout=25)

    def verify_multi_item_recognition_screen(self):
        """
        Verify Multi-Item Recognition screen via:
        + Title
        + Message
        + Explore Your Features button
        """
        self.driver.wait_for_object("multi_item_recognition_title")
        self.driver.wait_for_object("multi_item_recognition_message")
        self.driver.wait_for_object("explore_your_features_btn")
    
    def verify_auto_heal_scanning_screen(self):
        """
        Verify Auto Heal Scanning screen via:
        + Title
        + Message
        + Explore Your Features button
        """
        self.driver.wait_for_object("auto_heal_scanning_title")
        self.driver.wait_for_object("auto_heal_scanning_message")
        self.driver.wait_for_object("auto_heal_scanning_btn")

    def verify_add_a_printer_screen(self, timeout=20):
        """
        Verify Add a Printer screen via:
        - title
        """
        self.driver.wait_for_object("add_a_printer_text", timeout=timeout)
    
    def verify_printer_information_screen(self, timeout=10):
        """
        Verify Printer Information screen via:
        - printer information img
        """
        self.driver.wait_for_object("printer_information_img", timeout=timeout)