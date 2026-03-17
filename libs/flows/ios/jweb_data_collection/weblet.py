from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Weblet(JwebDataCollectionFlow):
    flow_name = "weblet"
    
    def select_info_button(self):
        """
        Selects the info button in the top right of the app next to the weblet header
        """
        self.driver.click("info_button", timeout=10)

    def select_open_settings_button(self):
        """
        Selects the open settings pop up button after selecting the info button
        """
        self.driver.click("open_settings_button")

    def clear_text_from_textbox(self, object_id):
        """
        Clear a textbox of the Weblet page from the Native context (needed to clear completely clear textbox, list can be added as needed) 
        """
        if object_id not in ['screen_name_textbox']:
            raise ValueError("{}: not present within list of textboxes".format(object_id))
        
        self.driver.clear_text(object_id)