from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from time import sleep

class Printables(HPXFlow):
    flow_name = "printables"


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_your_privacy_dialog(self):
        return self.driver.wait_for_object("accept_all_btn", timeout=10, raise_e=False)

    def verify_web_print_btn(self):
        if not self.driver.wait_for_object("web_print_btn", timeout=10, raise_e=False):
            if self.driver.driver_type.lower() == "windows":
                self.driver.swipe(distance=6)
        self.driver.wait_for_object("web_print_btn")

    def verify_print_dialog(self):
        self.driver.wait_for_object("dialog_print_btn")


    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_privacy_accept_all_btn(self):
        self.driver.click("accept_all_btn")

    def search_and_select_image(self, value):
        sleep(2)
        self.driver.click("search_edit")
        self.driver.send_keys("search_edit", value, press_enter=True)
        self.driver.click("happy_4_item", raise_e=False)
        sleep(2)
        self.driver.click("happy_4_image", displayed=False)

    def click_web_print_btn(self):
        self.driver.click("web_print_btn")

    def click_dialog_print_btn(self):
        self.driver.click("dialog_print_btn")

  