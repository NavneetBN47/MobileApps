from MobileApps.libs.flows.ios.jweb_auth.jweb_auth_flow import JwebAuthFlow

class Home(JwebAuthFlow):
    flow_name = "home"

    def select_top_bar_button(self, button, raise_e=True):
        """
        Select Top bar button next to the title 'Accounts'
        """
        button = button.title()
        if button not in ['Plugin', 'Settings', 'Add']:
            raise ValueError("{} button not in top bar. Must pass in 'Plugin' 'Settings' or 'Add'")
        self.driver.click('top_bar_button', format_specifier=[button], raise_e=raise_e)

    def select_accounts_back_button(self):
        """
        From the Plugin page, select the "Accounts" back button in the top left
        """
        self.driver.click("accounts_back_button")

    def select_app_settings_btn(self):
        """
        Select the app settings button from the pop up settings menu
        """
        self.driver.scroll("app_settings_btn", click_obj=True)

    def select_accounts_chevron_btn(self):
        """
        Select the chevron button from the pop up settings menu
        """
        self.driver.click("chevron_btn")