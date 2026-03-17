from MobileApps.libs.flows.android.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class DocProvider(JwebDocProviderFlow):
    flow_name = "doc_provider"

    def select_services_button(self):
        """
        Selects the services button in the top right of the Doc Provider page
        """
        self.driver.click("services_btn")

    def select_file_system_doc_source_option(self):
        """ 
        After clicking Services button, select FileSystemDocSource service
        """
        self.driver.click("file_system_doc_source_option")

    def select_doc_transformer_option(self):
        """ 
        After clicking Services button, select DocTransformer service
        """
        self.driver.click("doc_transformer_option")

    def select_doc_destination_option(self):
        """ 
        After clicking Services button, select DocDestination service
        """
        self.driver.click("doc_destination_option")

    def select_docs_button(self):
        """
        Select the Docs button for the first DocSet in the list
        """
        self.driver.click("docs_button")

    def get_doc_name(self):
        """
        Returns the str value of the first document name in the DocSet 
        """
        doc_name = self.driver.wait_for_object("doc_item", format_specifier=["."], raise_e=False, timeout=3)
        return doc_name if doc_name is False else doc_name.text

    def select_doc_from_list(self, doc_name):
        """
        Select the doc via doc_name after selecting the docs button for a DocSet
        """
        self.driver.click("doc_item", format_specifier=[doc_name])

    def get_doc_info(self):
        """
        After selecting on a doc within the docset, return resulting data as json
        """
        result_str, result_dict = self.driver.wait_for_object("doc_item_data").text.split("\n"), {}
        for r in result_str:
            key, value = r.split(":")
            key = key.lower().replace(" ", "_")
            result_dict[key] = value.replace(" ", "")
        return result_dict

    def get_doc_set_id(self):
        """
        Returns the DocSet id of the first DocSet in the list 
        """
        return self.driver.wait_for_object("doc_set").text