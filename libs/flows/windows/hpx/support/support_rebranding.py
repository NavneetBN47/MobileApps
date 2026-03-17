from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SupportRebranding(HPXFlow):
    flow_name = "support_rebranding"

    def click_rebranding_btn1(self):
        self.driver.click("rebranding_btn1")

    def get_rebranding_btn2_text(self):
        self.driver.wait_for_object("rebranding_btn2").get_attribute("Name")

    def click_rebranding_btn3(self):
        self.driver.find_object("rebranding_btn3").click()

    def click_rebranding_btn4(self):
        self.driver.click("rebranding_btn4")

    def input_sn(self, sn):
        self.driver.send_keys("sn_input", sn)

    def click_rebranding_btn5(self):
        self.driver.click("rebranding_btn5", timeout=30)

    def click_rebranding_btn6(self):
        self.driver.click("rebranding_btn6", displayed=False)

    def click_country_dropdown(self):
        self.driver.click("country_dropdown", timeout=30)

    def click_country_option(self, option):
        self.driver.click("country_option", format_specifier=[option], displayed=False)

    def click_show_more_btn(self):
        self.driver.click("show_more_btn")

    def click_start_va_btn(self):
        self.driver.click("start_va_btn", displayed=False)