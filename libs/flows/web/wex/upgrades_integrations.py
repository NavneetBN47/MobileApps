from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from time import sleep

class UpgradesIntegrations(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "upgrades_integrations"

    ######################## Main Menu ########################

    def verify_integrations_page(self):
        return self.driver.verify_object_string("integrations_page_breadcrumb", timeout=30)

    def verify_integrations_page_service_now_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_service_now_widget", raise_e=False, timeout=20)

    def verify_integrations_page_tableau_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_tableau_widget", raise_e=False, timeout=20)

    def get_integrations_page_tableau_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_tableau_widget", raise_e=False).text

    def verify_integrations_page_entra_id_accounts_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_entra_id_accounts_widget", raise_e=False)

    def verify_integrations_page_power_automate_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_power_automate_widget", raise_e=False)

    def verify_integrations_page_entra_id_groups_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_entra_id_groups_widget", raise_e=False)

    def verify_integrations_page_power_bi_widget(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_power_bi_widget", raise_e=False)

    def verify_integrations_page_service_now_widget_connect_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_service_now_widget_connect_button", raise_e=False)

    def verify_integrations_page_power_bi_widget_configure_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_power_bi_widget_configure_button", raise_e=False)

    def verify_integrations_page_power_automate_widget_connect_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_power_automate_widget_connect_button", raise_e=False)

    def verify_integrations_page_tableau_widget_configure_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_tableau_widget_configure_button", raise_e=False)

    def verify_integrations_page_entra_id_group_widget_connect_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_entra_id_group_widget_connect_button", raise_e=False)

    def verify_integrations_page_entra_id_account_widget_connect_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_entra_id_account_widget_connect_button", raise_e=False)

    def verify_integrations_page_entra_id_accounts_widget_upgrade_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_entra_id_accounts_widget_upgrade_button", raise_e=False)

    def get_integrations_page_info_message(self):
        return self.driver.wait_for_object("integrations_page_info_message", raise_e=False).text

    def verify_integrations_page_view_all_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_view_all_button", raise_e=False)

    def verify_integrations_page_active_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_active_button", raise_e=False)

    def verify_integrations_page_inactive_button(self):
        self.driver.switch_frame("integrations_page_widgets_frame")
        return self.driver.wait_for_object("integrations_page_inactive_button", raise_e=False)