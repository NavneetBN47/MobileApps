import pytest
import time
from MobileApps.libs.flows.web.ows import ows_utility
pytest.app_info = "POOBE"

class Test_012_back_button_behaviour(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation") 
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.pairing_code_page = self.fc.fd["pairing_code_page"]

        if self.printer_profile in self.fc.dual_sku_printers:
            self.sim_printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        
    """
    C32822013
    Steps:
    1. Clear the browser history and cookies/cache. Open the URL in your browser: https://smb.stage.portalshell.int.hp.com/onboard. Verify the "Access Delta Program" page is shown with a password required.
    2. Enter the security word "HPDELTA2022" and click Go. The Marconi Landing page is displayed.
    3. Login or create an account. Verifiy the The Account Type page is displayed.
    4. Press browser back arrow. Verify that there is a message prompt to the user.
    5. Check the UI and VX. Verify page matches the VX design and copy is correct against latest copydeck.Figma design:https://www.figma.com/file/l7qWK3iO3q8a1Q4n3wEeU9/SMB-Portal-OOBE-22.04.01?node-id=10957%3A79391.
    6. Select the cancel button on the overlay. Verify the Account Type page is still displayed.
    7. Select the Personal Use or Business Use. Sparse with Personal scenario and Business scenario. Verify the next "Assgin printer owner" or "Getting the most out of your account" page is displayed.
    8. Press browser back arrow. Verify that there is a message prompt to the user.
    9. Select the OK button. Verify the flow is lose to setup, it directs to the dashboard page.
    """
        

    def test_08_portal_browser_back_button_behaviour(self):
        if self.printer_profile not in self.fc.dual_sku_printers:
            pytest.skip()
        self.hpid.handle_privacy_popup()
        self.value_prop_page.verify_value_prop_page()
        self.value_prop_page.verify_landing_page_header()
        self.value_prop_page.verify_landing_page_subheader()
        self.value_prop_page.verify_landing_page_steps()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        time.sleep(3)
        self.p_oobe.verify_web_page(sub_url="pairing-code")
        self.pairing_code_page.verify_pairing_code_screen()
        self.p_oobe.verify_left_panel_printer_container(self.biz_model)
        # Click back button 3 times to see the alert on Pairing code page
        time.sleep(5)
        self.pairing_code_page.clear_entered_code()
        for _ in range(3):
            self.driver.click_browser_back_button()
            time.sleep(3)
        assert self.driver.check_if_browser_alert_present() is True, "pop-up msg did not show up"
        self.driver.accept_or_dismiss_browser_alert(accept=False)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.sim_printer_info, biz=self.biz_model)
        self.driver.click_browser_back_button()
        assert self.driver.check_if_browser_alert_present() is True
        self.driver.accept_or_dismiss_browser_alert(accept=True)
        self.hpid.handle_privacy_popup()
        self.value_prop_page.verify_value_prop_page()
        self.fc.remove_printer(self.printer_info, self.biz_model, timeout=80)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")