from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
class BellIcon(HPXRebrandingFlow):
    flow_name = "bell_icon"

    '''
    These Flows are for after clicking bell icon, i.e, the sideflyout of bell icon/notifications
    '''

    def get_notifications_title(self):
        return self.driver.get_attribute("notifications_title", "Name")

    def verify_notifications_title(self):
        return self.driver.wait_for_object("notifications_title", timeout=15)

    def verify_notifications_panel_text(self):
        return self.driver.wait_for_object("sign_in_to_view_msgs")

    def verify_notifications_panel_sign_in_btn(self):
        return self.driver.wait_for_object("notifications_panel_sign_in_btn")

    def verify_notifications_sidebar_ui(self):
        self.driver.wait_for_object("notifications_side_panel")
        self.driver.wait_for_object("sign_in_to_view_msgs")
        self.driver.wait_for_object("notifications_panel_sign_in_btn")
        self.driver.wait_for_object("notifications_title")
        return self.driver.get_attribute("notifications_title", "Name")

    def verify_notifications_panel_close_btn(self):
        return self.driver.get_attribute("notifications_panel_close_btn", "Name")

    def verify_read_text(self):
        return self.driver.wait_for_object("read_text")

    def verify_unread_text(self):
        return self.driver.wait_for_object("unread_text")

    def verify_informative_notifications(self):
        return self.driver.wait_for_object("informative_notifications")

    def get_informative_notifications_name(self):
        return self.driver.get_attribute("informative_read_notifs", "Name")

    def get_urgent_notifications_name(self):
        return self.driver.get_attribute("urgent_read_notifs", "Name")

    def get_warning_notifications_name(self):
        return self.driver.get_attribute("warning_read_notifs", "Name")

    def verify_urgent_notifications(self):
        return self.driver.wait_for_object("urgent_notifications")

    def verify_warning_notifications(self):
        return self.driver.wait_for_object("warning_notifications")

    def verify_urgent_unread_notifs(self):
        self.driver.wait_for_object("urgent_unread_notification")
        return self.driver.get_attribute("urgent_unread_notification", "Name", timeout=10)

    def verify_delete_disabled_urgent_unread_notifs(self):
        return self.driver.wait_for_object("delete_disabled_urgent_unread_notifs")

    def verify_warning_unread_notifs(self):
        self.driver.wait_for_object("warning_unread_notifs")
        return self.driver.get_attribute("warning_unread_notifs", "Name", timeout=10)

    def verify_informative_unread_notifs(self):
        self.driver.wait_for_object("informative_unread_notifs")
        return self.driver.get_attribute("informative_unread_notifs", "Name", timeout=10)

    def verify_notification_side_panel(self):
        if self.driver.wait_for_object("notifications_back_btn"):
            self.driver.wait_for_object("account_title")
            self.driver.wait_for_object("unread_text")
            self.driver.wait_for_object("read_text")
            return True
        else:
            return False

    def verify_notification_dropdown_revealed(self):
        return self.driver.wait_for_object("notification_dropdown_menu")

    def verify_dropdown_mark_as_read_option_present(self):
        return self.driver.wait_for_object("notification_dropdown_mark_read_option")

    def verify_dropdown_delete_option_present(self):
        return self.driver.wait_for_object("notification_dropdown_delete_option", timeout=15)

    def verify_urgent_unread_notification_ellipsis(self):
        return self.driver.wait_for_object("urgent_unread_notification_ellipsis")

    def verify_informative_unread_notification_ellipsis(self):
        return self.driver.wait_for_object("informative_unread_notification_ellipsis")

    def verify_warning_unread_notification_ellipsis(self):  
        return self.driver.wait_for_object("warning_unread_notification_ellipsis")

    def verify_time_stamp(self):
        return self.driver.wait_for_object("notification_timestamp")

    def get_time_stamp(self):
        return self.driver.get_attribute("notification_timestamp", "Name")

    def verify_notification_tile_ellipsis(self):
        return self.driver.wait_for_object("notification_tile_ellipsis")

    def verify_account_category(self):
        self.driver.wait_for_object("account_title")
        return self.driver.get_attribute("account_title", "Name")

    def get_notif_description(self):
        return self.driver.get_attribute("notif_description", "Name")

    def verify_urgent_msg_icon(self):
        return self.driver.wait_for_object("urgent_icon")

    def verify_warning_msg_icon(self):
        return self.driver.wait_for_object("warning_icon")

    def verify_info_msg_icon(self):
        return self.driver.wait_for_object("info_icon")

    def verify_sign_in_to_view_msgs(self):
        return self.driver.wait_for_object("sign_in_to_view_msgs")

    def verify_unread_urgent_notifs_name(self):
        self.driver.wait_for_object("urgent_unread_notifs_name")
        return self.driver.get_attribute("urgent_unread_notifs_name", "Name")

    def verify_unread_informative_notifs_name(self):
        self.driver.wait_for_object("informative_unread_notifs_name")
        return self.driver.get_attribute("informative_unread_notifs_name", "Name")

    def verify_unread_warning_notifs_name(self):
        self.driver.wait_for_object("warning_unread_notifs_name")
        return self.driver.get_attribute("warning_unread_notifs_name", "Name")

    def verify_notification_back_btn(self):
        return self.driver.wait_for_object("notifications_back_btn")

    def verify_detailed_notification_back_btn(self):
        self.driver.wait_for_object("detailed_notification_back_btn")
        return self.driver.get_attribute("detailed_notification_back_btn", "Name")

    def swipe_to_top_notifs_section(self):
        self.driver.swipe("account_title")

    def swipe_till_read_notifs(self):
        self.driver.swipe("read_text")

    def verify_notifs_and_mark_as_read(self):
        assert self.verify_notification_dropdown_revealed(), "notification drop down invisible"
        assert self.verify_dropdown_mark_as_read_option_present(), "mark as read option not visible in dropdown"
        assert self.verify_dropdown_delete_option_present(), "delete option not visible in dropdown"
        self.click_dropdown_mark_as_read()

    def get_detailed_notification_title(self):
        return self.driver.get_attribute("detailed_notification_title", "Name")

    def verify_background_blur(self):
        return self.driver.wait_for_object("background_blur")

##################################### CLICK ACTIONS #####################################

    def click_notifications_panel_close_btn(self):
        self.driver.click("notifications_panel_close_btn")

    def click_notifications_panel_sign_in_btn(self):
        self.driver.click("notifications_panel_sign_in_btn", timeout=10)

    def click_notification_account(self):
        self.driver.wait_for_object("notification_account")
        self.driver.click("notification_account")

    def click_urgent_unread_notification_ellipsis(self):
        self.driver.click("urgent_unread_notification_ellipsis")

    def click_warning_unread_notifs_ellipsis(self):
        self.driver.click("warning_unread_notifs_ellipsis")

    def click_delete_warning_unread_notifs(self):
        self.driver.click("delete_warning_unread_notifs")

    def click_notifications_back_btn(self):
        self.driver.click("notifications_back_btn")

    def click_informative_unread_notifs_ellipsis(self):
        self.driver.click("informative_unread_notifs_ellipsis")

    def click_delete_informative_unread_notifs(self):
        self.driver.click("delete_informative_unread_notifs")

    def click_informative_unread_notification_ellipsis(self):
        self.driver.click("informative_unread_notification_ellipsis")

    def click_warning_unread_notification_ellipsis(self):
        self.driver.click("warning_unread_notification_ellipsis")

    def click_notification_tile_ellipsis(self):
        self.driver.click("notification_tile_ellipsis")

    def click_informative_unread_notifs(self):
        self.driver.click("informative_unread_notifs")

    def click_urgent_unread_notifs(self):
        self.driver.click("urgent_unread_notification")

    def click_warning_unread_notifs(self):
        self.driver.click("warning_unread_notifs")

    def click_informative_read_notifs(self):
        self.driver.click("informative_notifications")

    def click_urgent_read_notifs(self):
        self.driver.click("urgent_notifications")

    def click_warning_read_notifs(self):
        self.driver.click("warning_notifications")

    def click_detailed_notification_back_btn(self):
        self.driver.click("detailed_notification_back_btn")

    def click_dropdown_mark_as_read(self):
        self.driver.click("notification_dropdown_mark_read_option")

    def verify_shortcuts_category(self):
        self.driver.wait_for_object("shortcuts_title")
        return self.driver.get_attribute("shortcuts_title", "Name")
