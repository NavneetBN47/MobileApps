from MobileApps.libs.flows.android.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class Weblet(JwebDocProviderFlow):
    flow_name = "weblet"

    def select_doc_source_button(self):
        """
        Selects the Doc Source button in the weblet tab
        """
        self.driver.click("doc_source_button", displayed=False)

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

    def select_new_doc_button(self):
        """
        Selects the "New Docset" button from the Doc Source pop up
        Doc Source pop up occurs when selecting Webview after a doc is present in the Doc Set
        """
        self.driver.click("new_docset_button")

    def select_append_button(self):
        """
        Selects the "Append" button from the Doc Source pop up
        Doc Source pop up occurs when selecting webview after a doc is present in the Doc Set
        """
        self.driver.click("append_button")