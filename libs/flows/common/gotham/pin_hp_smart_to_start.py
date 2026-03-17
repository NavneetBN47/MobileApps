from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow


class PinHPSmartToStart(GothamFlow):
    flow_name = "pin_hp_smart_to_start"


    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_pin_to_start_btn(self):
        self.driver.click("pin_to_start_btn")

    def select_do_you_want_to_pin_dialog_yes_btn(self):
        self.driver.click("do_you_want_to_pin_dialog_yes_btn")

    def select_do_you_want_to_pin_dialog_no_btn(self):
        self.driver.click("do_you_want_to_pin_dialog_no_btn")

    def select_pin_hp_smart_to_start_back_btn(self):
        self.driver.click("pin_hp_smart_to_start_back_btn")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_pin_hp_smart_to_start_screen(self, is_pinned=False):
        """
        Verify Pin HP Smart to Start screen.
        """
        self.driver.wait_for_object("pin_hp_smart_to_start_title")
        self.driver.wait_for_object("pin_hp_smart_to_start_back_btn")
        self.driver.wait_for_object("make_it_easy_to_find")
        self.driver.wait_for_object("pin_this_app_to_the_start_screen")
        self.driver.wait_for_object("pin_to_start_btn")
        self.driver.wait_for_object("note_you_can_unpin")
        self.driver.wait_for_object("pin_to_start_image")
        if is_pinned:
            self.driver.wait_for_object("app_is_already_pinned")
        else:
            assert self.driver.wait_for_object("app_is_already_pinned", raise_e=False) is False

    def verify_pin_to_start_btn_enabled(self):
        return self.driver.wait_for_object("pin_to_start_btn").is_enabled()

    def verify_do_you_want_to_pin_dialog(self):
        """
        Verify Pin HP Smart to Start screen.
        """
        self.driver.wait_for_object("do_you_want_to_pin_dialog")
        self.driver.wait_for_object("do_you_want_to_pin_dialog_yes_btn")
        self.driver.wait_for_object("do_you_want_to_pin_dialog_no_btn")
