from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare

class DeviceCard(HPXRebrandingFlow):
    flow_name = "device_card"

    def verify_product_information(self):
        self.driver.swipe("product_information")
        return self.driver.wait_for_object("product_information")

    def verify_warrenty_status(self):
        self.driver.swipe("product_information", distance=9)
        return self.driver.wait_for_object("warrenty_status")

    def verify_bell_icon_present(self):
        return self.driver.wait_for_object("bell_icon", timeout=15)

    def get_copyserial_number_text(self):
        return self.driver.get_attribute("copybtn_serialnumber_on_pcdevice","Name")

    def get_copyproduct_number_text(self):
        return self.driver.get_attribute("copybtn_productnumber_on_pcdevice","Name")

    def get_nick_name_from_settings(self):
        return self.driver.get_attribute("nick_name_settings", "Name")

    def get_device_name_from_settings(self):
        return self.driver.get_attribute("device_name_settings", "Name")

    def get_device_name_down_nick_name(self):
        return self.driver.get_attribute("device_name_down_nick_name", "Name")

    def verify_device_name_pc(self):
        return self.driver.wait_for_object("device_card_with_pc", timeout=20)

    def verify_battery_icon(self):
        return self.driver.wait_for_object("battery_icon_device_page", timeout=10)

    def verify_pc_devices_back_button(self):
        if self.driver.wait_for_object("pc_devices_back_button"):
            return True
        else:
            return False

    def verify_devices_back_button(self):
        self.driver.wait_for_object("pc_devices_back_button")
        return self.driver.get_attribute("pc_devices_back_button", "LocalizedControlType")

    def verify_device_details_page(self):
        if self.driver.wait_for_object("pc_devices_back_button"):
            self.driver.wait_for_object("device_card_with_pc")
            self.driver.wait_for_object("battery_icon_device_page")
            return True
        else:
            return False

    def verify_get_help_module(self):
        return self.driver.wait_for_object("get_help", timeout=5)

    def verify_get_help_card_options(self):
        for _ in range(5):
             self.driver.swipe(distance=3)
             if self.driver.wait_for_object("get_help_contact_us", timeout=5, raise_e=False) is not False:
                 break
        self.driver.wait_for_object("get_help_card_title")
        self.driver.wait_for_object("get_help_card_desc")
        self.driver.wait_for_object("get_help_virtual_assistant_btn")
        self.driver.wait_for_object("get_help_manuals_guides")
        self.driver.wait_for_object("get_help_find_repair")
        self.driver.wait_for_object("get_help_start_repair")
        self.driver.wait_for_object("get_help_more_help_website")
        self.driver.wait_for_object("get_help_contact_us")

    def verify_device_type(self):
        self.driver.wait_for_object("device_type_name", timeout=15)
        device_type_name = self.driver.get_attribute("device_type_name", "Name")
        if device_type_name.endswith("Active"):
            device_type_name = device_type_name.replace("Active", "")
        return device_type_name

    def verify_status_in_warranty_status(self):
        return self.driver.wait_for_object("warranty_status_text")

    def verify_warranty_status_button_and_text(self):
        self.driver.wait_for_object("pc_devices_back_button")
        return self.driver.get_attribute("pc_devices_back_button", "LocalizedControlType")

    def get_campaign_ads_num_1(self):
        return self.driver.get_attribute("campaign_ads_num_1", "Name")

    def get_campaign_ads_num_2(self):
        return self.driver.get_attribute("campaign_ads_num_2", "Name")

    def verify_homepage_plus_button(self):
        return self.driver.wait_for_object("homepage_plus_button")

    def verify_hp_app_window_title(self, raise_e=False):
        return self.driver.wait_for_object("hp_app_window_title", timeout=8, raise_e=raise_e)

##################################### CLICK ACTIONS #####################################

    def click_pc_devices_back_button(self):
        self.driver.wait_for_object("pc_devices_back_button")
        self.driver.click("pc_devices_back_button", timeout=10)

    def handle_feature_unavailable_popup(self, timeout=20):
        if self.driver.wait_for_object("feature_unavailable_ok_btn", raise_e=False, timeout=timeout) is not False:
            self.driver.click("feature_unavailable_ok_btn", timeout=10)

    def click_bell_icon(self,raise_e=False,timeout=15):
        if self.driver.wait_for_object("bell_icon",raise_e=raise_e,timeout=timeout):
            self.driver.click("bell_icon", timeout=10)

    def click_homepage_plus_button(self):
        if self.driver.wait_for_object("homepage_plus_button") is not False:
            self.driver.click("homepage_plus_button", timeout = 5)

    def click_get_help_manuals_guides(self):
        self.driver.click("get_help_manuals_guides", timeout=10)

    def click_get_help_find_repair(self):
        self.driver.click("get_help_find_repair", timeout=10)

    def click_get_help_more_help_website(self):
        self.driver.click("get_help_more_help_website", timeout=10)

    def click_start_repair_link(self):
        self.driver.click("get_help_start_repair", timeout=10)

    def click_warrenty_status_btn(self):
        self.driver.click("warrenty_status", timeout=10)

    def get_device_battery_charging_state(self):
        return self.driver.get_attribute("battery_text_device_page", "Name", timeout=15)

    @screenshot_compare(pass_ratio=0.02)
    def verify_color_filter(self):
        return self.driver.wait_for_object("device_card_with_pc", raise_e=False, timeout=10)
