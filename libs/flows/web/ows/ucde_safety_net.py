from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class UCDESafetyNet(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com/ucde/safety-net/
    """
    flow_name = "ucde_safety_net"
    @screenshot_compare()
    def verify_ucde_safety_net(self):
        self.driver.wait_for_object("safety_net_page_div", timeout=20)

    def click_back_to_account_btn(self):
        self.driver.click("back_to_account_btn")

    def click_skip_warrenty_and_account_activation(self):
        self.driver.click("skip_warrenty_and_account_activation_btn")
        
    def click_read_more(self):
        self.driver.wait_for_object("read_more")
        return self.driver.click("read_more")
    
    def click_read_more_ok(self):
        self.driver.wait_for_object("read_more_ok")
        return self.driver.click("read_more_ok")

    def click_skip_account_activation(self):
        self.driver.wait_for_object("skip_account_activation")
        return self.driver.click("skip_account_activation")
    
    def click_skip_account_activation_again(self):
        self.driver.wait_for_object("skip_account_activation_again")
        return self.driver.click("skip_account_activation_again")
    
    def verify_load_paper_visible(self, raise_e=True):
        return self.driver.wait_for_object("load_paper_txt", timeout=10, raise_e=raise_e)
    
    def verify_redeem_4_free_months_txt_visible(self, raise_e=True):
        return self.driver.wait_for_object("redeem_4_free_months_txt", timeout=10, raise_e=raise_e)
    
    def verify_load_account_visible(self, raise_e=True):
        return self.driver.wait_for_object("load_account_txt", timeout=10, raise_e=raise_e)
    
    def click_sign_in(self):
        self.driver.wait_for_object("sign_in_btn")
        return self.driver.click("sign_in_btn")
    
    def click_create_account(self):
        self.driver.wait_for_object("create_account_btn")
        return self.driver.click("create_account_btn")
    
    def click_sign_in(self):
        self.driver.wait_for_object("sign_in_btn")
        return self.driver.click("sign_in_btn")
    
    def click_create_account(self):
        self.driver.wait_for_object("create_account_btn")
        return self.driver.click("create_account_btn")
    
    def verify_loading_hp_account(self):
        self.driver.wait_for_object("load_account_txt", timeout=30)
        
    def verify_read_more_screen(self):
        self.driver.wait_for_object("read_more_txt", timeout=20)
        
    def click_read_more_ok_btn(self):
        self.driver.click("read_more_ok_btn")
        
    def verify_back_to_main_page(self):
        self.driver.wait_for_object("create_account_btn")