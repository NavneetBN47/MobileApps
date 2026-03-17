from MobileApps.libs.flows.ios.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class Weblet(JwebDocProviderFlow):
    flow_name = "weblet"

    def select_doc_source_button(self):
        """
        Selects the Doc Source button in the weblet tab
        """
        self.driver.click("doc_source_button")

    def select_file_system_doc_source_button(self):
        """
        Selects the FileSystem Doc Source button in the weblet tab
        """
        self.driver.click("file_system_doc_source_button")

    def select_doc_transformer_button(self):
        """
        Selects the Doc Transformer button in the weblet tab
        """
        self.driver.click("doc_transformer_button")

    def select_doc_destination_button(self):
        """
        Selects the Doc Destination button in the weblet tab
        """
        self.driver.click("doc_destination_button")