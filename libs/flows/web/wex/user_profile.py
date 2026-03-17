from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class UserProfile(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "user_profile"

    ####################### Main Menu - User Profile #######################

    def verify_user_profile_button(self):
        return self.driver.wait_for_object("user_profile_button", raise_e=False, timeout=20)
   
    def click_user_profile_button(self):
        return self.driver.click("user_profile_button")

    def click_user_profile_link(self):
        return self.driver.click("user_profile_link")
   
    def verify_user_profile_page_breadcrumb(self):
        return self.driver.verify_object_string("user_profile_page_breadcrumb", timeout=30)

    def verify_user_profile_overview_tab(self):
        return self.driver.wait_for_object("user_profile_page_overview_tab", raise_e=False, timeout=20)

    def verify_user_profile_communication_preference_tab(self,  displayed=True):
        return self.driver.wait_for_object("user_profile_page_communication_preference_tab", raise_e=False, timeout=20)
   
    ###################### User Profile - Overview Tab ######################

    def verify_user_profile_overview_tab_name_label(self):
        return self.driver.verify_object_string("user_profile_overview_tab_name_label")

    def verify_user_profile_overview_tab_mobile_phone_number_label(self):
        return self.driver.verify_object_string("user_profile_overview_tab_mobile_phone_number_label")
   
    def verify_user_profile_overview_tab_office_phone_number_label(self):
        return self.driver.verify_object_string("user_profile_overview_tab_office_phone_number_label")

    def verify_user_profile_overview_tab_preferred_language_label(self):
        return self.driver.verify_object_string("user_profile_overview_tab_preferred_language_label")

    def verify_user_profile_overview_time_zone_label(self):
        return self.driver.verify_object_string("user_profile_overview_tab_time_zone_label")

    def verify_user_profile_overview_tab_title_label(self):
        return self.driver.verify_object_string("user_profile_overview_tab_title_label")
   
    def verify_user_profile_overview_tab_title_edit_button(self):
        return self.driver.wait_for_object("user_profile_overview_tab_title_edit_button", raise_e=False, timeout=20)
    
    def verify_user_profile_overview_tab_name_edit_button(self):
        return self.driver.wait_for_object("user_profile_overview_tab_name_edit_button", raise_e=False, timeout=20)
    
    def verify_user_profile_overview_tab_mobile_phone_number_edit_button(self):
        return self.driver.wait_for_object("user_profile_overview_tab_mobile_phone_number_edit_button", raise_e=False, timeout=20)
    
    def verify_user_profile_overview_tab_office_phone_number_edit_button(self):
        return self.driver.wait_for_object("user_profile_overview_tab_office_phone_number_edit_button", raise_e=False, timeout=20)
    
    def verify_user_profile_overview_tab_preferred_language_edit_button(self):
        return self.driver.wait_for_object("user_profile_overview_tab_preferred_language_edit_button", raise_e=False, timeout=20)
    
    def verify_user_profile_overview_tab_time_zone_edit_button(self):
        return self.driver.wait_for_object("user_profile_overview_tab_time_zone_edit_button", raise_e=False, timeout=20)

    ###################### User Profile - Communication Preference Tab ######################

    def click_user_profile_page_communication_preference_tab(self):
        return self.driver.click("user_profile_page_communication_preference_tab")

    def get_user_profile_communication_tab_whats_new_popup_title(self):
        return self.driver.wait_for_object("user_profile_communication_tab_whats_new_popup_title", raise_e=False, timeout=30).text

    def verify_user_profile_communication_tab_whats_new_popup_toggle_button(self):
        return self.driver.wait_for_object("user_profile_communication_tab_whats_new_popup_toggle_button", raise_e=False, timeout=20)

    def click_user_profile_communication_tab_whats_new_popup_toggle_button(self):
        return self.driver.click("user_profile_communication_tab_whats_new_popup_toggle_button")

    def verify_user_profile_communication_tab_whats_new_popup_toggle_status(self):
        self.driver.wait_for_object("user_profile_communication_tab_whats_new_popup_toggle_button", raise_e=False, timeout=20)
        if self.driver.find_object("user_profile_communication_tab_whats_new_popup_toggle_button_status", raise_e=False):
            return True
        else:
            return False

    def user_profile_communication_tab_whats_new_popup_toggle_button_status(self):
        # Get the initial status of the toggle button
        initial_status = self.verify_user_profile_communication_tab_whats_new_popup_toggle_status()
   
        self.click_user_profile_communication_tab_whats_new_popup_toggle_button()

        # Get the status after the first click
        first_click_status = self.verify_user_profile_communication_tab_whats_new_popup_toggle_status()
       
        # Verify the status has changed
        assert first_click_status != initial_status, "Toggle button status did not change after the first click."

        # Click the toggle button again to revert its state
        self.click_user_profile_page_communication_preference_tab()
        self.click_user_profile_communication_tab_whats_new_popup_toggle_button()
   
        # Get the status after the second click
        second_click_status = self.verify_user_profile_communication_tab_whats_new_popup_toggle_status()
   
        # Verify the status has reverted to the initial state
        assert second_click_status == initial_status, "Toggle button status did not revert to the initial state after the second click."
    
    def get_user_profile_communication_tab_alert_notifications_title(self):
        return self.driver.wait_for_object("user_profile_communication_tab_alert_notifications_title", raise_e=False, timeout=30).text

    def verify_user_profile_communication_tab_alert_notifications_toggle_button(self):
        return self.driver.wait_for_object("user_profile_communication_tab_alert_notifications_toggle_button", raise_e=False, timeout=20)

    def click_user_profile_communication_tab_alert_notifications_toggle_button(self):
        return self.driver.click("user_profile_communication_tab_alert_notifications_toggle_button")

    def verify_user_profile_communication_tab_alert_notifications_toggle_button_status(self):
        self.driver.wait_for_object("user_profile_communication_tab_alert_notifications_toggle_button", raise_e=False, timeout=20)
        if self.driver.find_object("user_profile_communication_tab_alert_notifications_toggle_button_status", raise_e=False):
            return True
        else:
            return False

    def user_profile_communication_tab_alert_notifications_toggle_button_status(self):
        # Get the initial status of the toggle button
        initial_status = self.verify_user_profile_communication_tab_alert_notifications_toggle_button_status()

        self.click_user_profile_communication_tab_alert_notifications_toggle_button()

        # Get the status after the first click
        first_click_status = self.verify_user_profile_communication_tab_alert_notifications_toggle_button_status()

        # Verify the status has changed
        assert first_click_status != initial_status, "Toggle button status did not change after the first click."

        # Click the toggle button again to revert its state
        self.click_user_profile_page_communication_preference_tab()
        self.click_user_profile_communication_tab_alert_notifications_toggle_button()

        # Get the status after the second click
        second_click_status = self.verify_user_profile_communication_tab_alert_notifications_toggle_button_status()

        # Verify the status has reverted to the initial state
        assert second_click_status == initial_status, "Toggle button status did not revert to the initial state after the second click."

    def get_user_profile_communication_tab_general_system_notifications_title(self):
        return self.driver.wait_for_object("user_profile_communication_tab_general_system_notifications_title", raise_e=False, timeout=30).text

    def verify_user_profile_communication_tab_general_system_notifications_toggle_button(self):
        return self.driver.wait_for_object("user_profile_communication_tab_general_system_notifications_toggle_button", raise_e=False, timeout=20)
    
    def click_user_profile_communication_tab_general_system_notifications_toggle_button(self):
        return self.driver.click("user_profile_communication_tab_general_system_notifications_toggle_button")
    
    def verify_user_profile_communication_tab_general_system_notifications_toggle_button_status(self):
        self.driver.wait_for_object("user_profile_communication_tab_general_system_notifications_toggle_button", raise_e=False, timeout=20)
        if self.driver.find_object("user_profile_communication_tab_general_system_notifications_toggle_button_status", raise_e=False):
            return True
        else:
            return False

    def user_profile_communication_tab_general_system_notifications_toggle_button_status(self):
        # Get the initial status of the toggle button
        initial_status = self.verify_user_profile_communication_tab_general_system_notifications_toggle_button_status()

        self.click_user_profile_communication_tab_general_system_notifications_toggle_button()

        # Get the status after the first click
        first_click_status = self.verify_user_profile_communication_tab_general_system_notifications_toggle_button_status()

        # Verify the status has changed
        assert first_click_status != initial_status, "Toggle button status did not change after the first click."

        # Click the toggle button again to revert its state
        self.click_user_profile_page_communication_preference_tab()
        self.click_user_profile_communication_tab_general_system_notifications_toggle_button()

        # Get the status after the second click
        second_click_status = self.verify_user_profile_communication_tab_general_system_notifications_toggle_button_status()

        # Verify the status has reverted to the initial state
        assert second_click_status == initial_status, "Toggle button status did not revert to the initial state after the second click."