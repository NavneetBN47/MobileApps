from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Files(JwebDataCollectionFlow):
    flow_name = "files"

    def click_downloads_list_item(self):
        """
        select the "Downloads" option in the left hand side of the finder window
        """
        self.driver.click("downloads_list_item")
    
    def send_text_file_name_textbox(self, text):
        """
        sends text to the "File Name:" textbox
        """
        self.driver.send_keys("file_name_edit_box", text)

    def click_open_btn(self):
        """
        selects the "open" button in the bottom right hand corner of the finder window
        """
        self.driver.click("open_btn")