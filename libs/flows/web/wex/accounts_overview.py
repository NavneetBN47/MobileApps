from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class AccountsOverview(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "accounts_overview"

    ######################## Main Menu ########################

    def verify_accounts_page(self):
        return self.driver.wait_for_object("accounts_page_breadcrumb", timeout=30, raise_e=False)

    def get_accounts_page(self):
        return self.driver.wait_for_object("accounts_page_breadcrumb", timeout=30, raise_e=False).text
   
    def verify_accounts_page_overview_tab(self, displayed=True):
        return self.driver.wait_for_object("accounts_page_overview_tab", invisible=not displayed, raise_e=False)

    def verify_accounts_page_users_tab(self, displayed=True):
        return self.driver.wait_for_object("accounts_page_users_tab", invisible=not displayed, raise_e=False)

    def verify_accounts_tab_add_ons_tab(self, displayed=True):
        return self.driver.wait_for_object("accounts_tab_add_ons_tab", invisible=not displayed, raise_e=False)

    def verify_accounts_page_licenses_tab(self, displayed=True):
        return self.driver.wait_for_object("accounts_page_licenses_tab", invisible=not displayed, raise_e=False)

    def verify_accounts_page_assigned_partners_tab(self, displayed=True):
        return self.driver.wait_for_object("accounts_page_assigned_partners_tab", invisible=not displayed, raise_e=False)

    def verify_accounts_roles_and_permissions_tab(self, displayed=True):
        return self.driver.wait_for_object("accounts_roles_and_permissions_tab", invisible=not displayed, raise_e=False)

########################## Account Page - Overview Tab ##########################

    def get_accounts_page_overview_tab_title(self):
        return self.driver.wait_for_object("accounts_page_overview_tab").text

    def get_accounts_page_overview_tab_company_size_label(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_company_size_label", raise_e=False).text

    def get_accounts_page_overview_tab_company_name_label(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_company_name_label", raise_e=False).text

    def get_accounts_page_overview_tab_primary_administrator_title(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_primary_administrator_title", raise_e=False).text

    def get_accounts_page_overview_tab_company_address_title(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_company_address_label", raise_e=False).text

    def verify_accounts_page_overview_tab_company_address_edit_button(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_company_address_edit_button", raise_e=False)

    def verify_accounts_page_overview_tab_company_size_edit_button(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_company_size_edit_button", raise_e=False)
    
    def verify_accounts_page_overview_tab_company_name_edit_button(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_company_name_edit_button", raise_e=False)
    
    def verify_accounts_page_overview_tab_primary_administrator_edit_button(self):
        return self.driver.wait_for_object("accounts_page_overview_tab_primary_administrator_edit_button", raise_e=False)

######################### Account Page - Users Tab #########################

    def click_accounts_page_users_tab(self):
        return self.driver.click("accounts_page_users_tab")

    def get_accounts_page_users_tab_title(self):
        return self.driver.wait_for_object("accounts_page_users_tab").text

    def verify_accounts_page_users_table_checkbox(self, displayed=True):
        return self.driver.wait_for_object("accounts_page_users_table_checkbox", invisible=not displayed, raise_e=False)

    def search_accounts_page_users_name(self, name):
        self.driver.click("accounts_page_users_name_search_box", timeout=30)
        return self.driver.send_keys("accounts_page_users_name_search_box", name)

    def click_accounts_page_users_table_checkbox(self):
        return self.driver.click("accounts_page_users_table_checkbox")

    def verify_accounts_page_users_tab_invite_users_button(self):
        return self.driver.wait_for_object("accounts_page_users_tab_invite_users_button", raise_e=False)
   
    def click_accounts_page_users_tab_invite_users_button(self):
        return self.driver.click("accounts_page_users_tab_invite_users_button")

    def get_accounts_page_users_tab_invite_users_popup_title(self):
        return self.driver.wait_for_object("accounts_page_users_tab_invite_users_popup_title", timeout=30).text

    def verify_accounts_page_users_tab_invite_users_popup_cancel_button(self):
        return self.driver.wait_for_object("accounts_page_users_tab_invite_users_popup_cancel_button", raise_e=False)

    def click_accounts_page_users_tab_invite_users_popup_cancel_button(self):
        return self.driver.click("accounts_page_users_tab_invite_users_popup_cancel_button")
   
    def verify_accounts_page_users_tab_delete_button(self):
        return self.driver.wait_for_object("accounts_page_users_tab_delete_button", raise_e=False)

    def click_accounts_page_users_tab_delete_button(self):
        return self.driver.click("accounts_page_users_tab_delete_button")

    def get_accounts_page_users_tab_delete_popup_title(self):
        return self.driver.wait_for_object("accounts_page_users_tab_delete_popup_title").text
   
    def verify_accounts_page_users_tab_delete_popup_cancel_button(self):
        return self.driver.wait_for_object("accounts_page_users_tab_delete_popup_cancel_button", raise_e=False)

    def click_accounts_page_users_tab_delete_popup_cancel_button(self):
        return self.driver.click("accounts_page_users_tab_delete_popup_cancel_button")

    def verify_accounts_page_users_tab_assign_roles_button(self):
        return self.driver.wait_for_object("accounts_page_users_tab_assign_roles_button", raise_e=False)

    def click_accounts_page_users_tab_assign_roles_button(self):
        return self.driver.click("accounts_page_users_tab_assign_roles_button")

    def get_accounts_page_users_tab_assign_roles_popup_title(self):
        return self.driver.wait_for_object("accounts_page_users_tab_assign_roles_popup_title").text

    def verify_accounts_page_users_tab_assign_roles_popup_cancel_button(self):
        return self.driver.wait_for_object("accounts_page_users_tab_assign_roles_popup_cancel_button", raise_e=False)
   
    def click_accounts_page_users_tab_assign_roles_popup_cancel_button(self):
        return self.driver.click("accounts_page_users_tab_assign_roles_popup_cancel_button")
   
####################### Account Page - Add-Ons Tab ######################

    def click_accounts_tab_add_ons_tab(self):
        return self.driver.click("accounts_tab_add_ons_tab")

    def get_accounts_page_add_ons_tab_title(self):
        return self.driver.wait_for_object("accounts_tab_add_ons_tab").text
   
    def get_accounts_page_add_ons_tab_hp_anyware_widget_title(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_hp_anyware_widget_title", raise_e=False).text
   
    def verify_accounts_page_add_ons_tab_hp_anyware_widget_learn_more_link(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_hp_anyware_widget_learn_more_link", raise_e=False)

    def get_accounts_page_add_ons_tab_vyopta_widget_title(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_vyopta_widget_title", raise_e=False).text

    def verify_accounts_page_add_ons_tab_vyopta_widget_connect_button(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_vyopta_widget_connect_button", raise_e=False)
   
    def verify_accounts_page_add_ons_tab_vyopta_widget_learn_more_link(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_vyopta_widget_learn_more_link", raise_e=False)
   
    def get_accounts_page_add_ons_tab_hp_wolf_widget_title(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_hp_wolf_widget_title", raise_e=False).text
   
    def verify_accounts_page_add_ons_tab_hp_wolf_widget_learn_more_link(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_hp_wolf_widget_learn_more_link", raise_e=False)

    def verify_accounts_page_add_ons_tab_hp_anyware_widget_title(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_hp_anyware_widget_title", raise_e=False)
            
    def verify_accounts_page_add_ons_tab_vyopta_widget_title(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_vyopta_widget_title", raise_e=False)

    def verify_accounts_page_add_ons_tab_hp_wolf_widget_title(self):
        return self.driver.wait_for_object("accounts_page_add_ons_tab_hp_wolf_widget_title", raise_e=False)

######################## Account Page - Licenses Tab ######################

    def click_accounts_page_licenses_tab(self):
        return self.driver.click("accounts_page_licenses_tab")

    def get_accounts_page_licenses_tab_title(self):
        return self.driver.wait_for_object("accounts_page_licenses_tab").text

    def verify_accounts_page_licenses_tab_add_licenses_button(self):
        return self.driver.wait_for_object("accounts_page_licenses_tab_add_licenses_button", raise_e=False)

    def click_accounts_page_licenses_tab_add_licenses_button(self):
        return self.driver.click("accounts_page_licenses_tab_add_licenses_button")

    def get_accounts_page_licenses_tab_add_licenses_popup_title(self):
        return self.driver.wait_for_object("accounts_page_licenses_tab_add_licenses_popup_title").text

    def verify_accounts_page_licenses_tab_add_licenses_popup_cancel_button(self):
        return self.driver.wait_for_object("accounts_page_licenses_tab_add_licenses_popup_cancel_button", raise_e=False)

    def click_accounts_page_licenses_tab_add_licenses_popup_cancel_button(self):
        return self.driver.click("accounts_page_licenses_tab_add_licenses_popup_cancel_button")

    ##################### Account Page - Assigned Partners Tab ######################

    def click_accounts_page_assigned_partners_tab(self):
        return self.driver.click("accounts_page_assigned_partners_tab")

    def get_accounts_page_assigned_partners_tab_title(self):
        return self.driver.wait_for_object("accounts_page_assigned_partners_tab", raise_e=False, timeout=20).text
    
    def verify_accounts_page_assigned_partners_tab_assignment_settings_label(self):
        return self.driver.wait_for_object("accounts_page_assigned_partners_tab_assignment_settings_label", raise_e=False)
    
    def verify_accounts_page_assigned_partners_tab_invitations_label(self):
        return self.driver.wait_for_object("accounts_page_assigned_partners_tab_invitations_label", raise_e=False)

    def verify_accounts_page_assigned_partners_tab_assignment_delete_button(self):
        return self.driver.wait_for_object("accounts_page_assigned_partners_tab_assignment_delete_button", raise_e=False)

######################### Account Page - Roles & Permissions Tab ######################

    def click_accounts_roles_and_permissions_tab(self):
        return self.driver.click("accounts_roles_and_permissions_tab")

    def verify_roles_and_permissions_tab_add_button(self):
        return self.driver.wait_for_object("roles_and_permissions_tab_add_button", raise_e=False)
    
    def verify_roles_and_permissions_tab_table(self):
        return self.driver.wait_for_object("roles_and_permissions_tab_table", raise_e=False)