from MobileApps.libs.flows.windows.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class Home(JwebDocProviderFlow):
    flow_name = "home"

    def load_doc_source_weblet(self):
        self.enable_launch_as_web_service_btn()
        self.select_service_btn("Doc Source")

    def select_top_nav_button(self, btn_name, raise_e=True):
        """
        From the top navigation bar, select locator btn_name
        """
        if btn_name not in ["Doc Provider", "Event History"]:
            raise ValueError("{} not a a btn available in the top navigation bar".format(btn_name))
        self.driver.click("top_nav_btn", format_specifier=[btn_name], raise_e=raise_e)

    def select_service_btn(self, btn_name, raise_e=True):
        """
        From the service bar, select locator btn_name: "Doc Source", "Doc Transformer", "Doc Destination"
        """
        if btn_name not in ["Doc Source", "Doc Transformer", "Doc Destination"]:
            raise ValueError("{} not a a btn available in the service bar".format(btn_name))
        self.driver.click("service_btn", format_specifier=[btn_name], raise_e=raise_e)

    def enable_launch_as_web_service_btn(self):
        """
        From the service bar, enable locator "Launch as web service" button
        """
        self.driver.check_box("launch_as_web_service_btn")

    def get_doc_set_id(self):
        """
        Returns lower-case DocSet id found under Doc sets: below the Services pane
        """
        return self.driver.get_attribute("doc_set", "Name").lower()

    def get_doc_info(self, raise_e=True):
        """
        Returns Doc info found under Docs: including; DocID, DocFileName, DocFileType, DocSize
        """
        return self.driver.get_attribute("doc_item", "Name", raise_e=raise_e)

    def select_create_new_doc_set(self):
        """
        From the "You have a document set selected" prompt, select Create new doc set
        """
        self.driver.click("create_new_doc_set")

    def select_use_selected_doc_set(self):
        """
        From the "You have a document set selected" prompt, select Use selected doc set
        """
        self.driver.click("use_selected_doc_set")

    # Doc Source Functions

    def select_add_document(self):
        """
        From the Doc Source pane, select 'Add document' btn
        """
        self.driver.click("add_document_btn")

    def select_close_btn(self):
        """
        From the Doc Source pane, select 'Close' btn
        """
        self.driver.click("close_btn")
