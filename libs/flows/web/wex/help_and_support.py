from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class HelpAndSupport(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "help_and_support"

    ######################## Main Menu ########################

    def verify_help_and_support_button(self):
        return self.driver.wait_for_object("help_and_support_button", raise_e=False, timeout=20)

    def click_help_and_support_button(self):
        return self.driver.click("help_and_support_button")

    def verify_help_and_support_page(self):
        return self.driver.verify_object_string("help_and_support_page_breadcrumb", timeout=30)

    def verify_help_and_support_page_header(self):
        return self.driver.verify_object_string("help_and_support_page_header")
   
    def verify_help_and_support_page_header_description(self):
        return self.driver.verify_object_string("help_and_support_page_header_description")

    ######################### Help and Support Page - Get Started Widget #########################

    def verify_help_and_support_page_get_started_widget(self):
        return self.driver.wait_for_object("help_and_support_page_get_started_widget", raise_e=False)

    def verify_help_and_support_page_get_started_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_get_started_widget_title", raise_e=False)

    def verify_help_and_support_page_get_started_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_get_started_widget_description", raise_e=False)

    def verify_help_and_support_page_get_started_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_get_started_widget_navigation_button", raise_e=False)

    ########################## Help and Support Page - System Requirements Widget #########################

    def verify_help_and_support_page_system_requirements_widget(self):
        return self.driver.wait_for_object("help_and_support_page_system_requirements_widget", raise_e=False)
   
    def verify_help_and_support_page_system_requirements_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_system_requirements_widget_title", raise_e=False)
   
    def verify_help_and_support_page_system_requirements_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_system_requirements_widget_description", raise_e=False)

    def verify_help_and_support_page_system_requirements_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_system_requirements_widget_navigation_button", raise_e=False)    

    ########################## Help and Support Page - Knowledge Base Widget #########################

    def verify_help_and_support_page_knowledge_base_widget(self):
        return self.driver.wait_for_object("help_and_support_page_knowledge_base_widget", raise_e=False)
   
    def verify_help_and_support_page_knowledge_base_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_knowledge_base_widget_title", raise_e=False)

    def verify_help_and_support_page_knowledge_base_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_knowledge_base_widget_description", raise_e=False)

    def verify_help_and_support_page_knowledge_base_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_knowledge_base_widget_navigation_button", raise_e=False)
   
    ########################## Help and Support Page - Software Download Widget #########################

    def verify_help_and_support_page_software_download_widget(self):
        return self.driver.wait_for_object("help_and_support_page_software_download_widget", raise_e=False)
   
    def verify_help_and_support_page_software_download_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_software_download_widget_title", raise_e=False)
   
    def verify_help_and_support_page_software_download_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_software_download_widget_description", raise_e=False)

    def verify_help_and_support_page_software_download_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_software_download_widget_navigation_button", raise_e=False)

    ########################## Help and Support Page - What's New Widget #########################
   
    def verify_help_and_support_page_whats_new_widget(self):
        return self.driver.wait_for_object("help_and_support_page_whats_new_widget", raise_e=False)

    def verify_help_and_support_page_whats_new_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_whats_new_widget_title", raise_e=False)
   
    def verify_help_and_support_page_whats_new_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_whats_new_widget_description", raise_e=False)

    def verify_help_and_support_page_whats_new_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_whats_new_widget_navigation_button", raise_e=False)
   
    ########################## Help and Support Page - Send Feedback Widget #########################

    def verify_help_and_support_page_send_feedback_widget(self):
        return self.driver.wait_for_object("help_and_support_page_send_feedback_widget", raise_e=False)
   
    def verify_help_and_support_page_send_feedback_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_send_feedback_widget_title", raise_e=False)

    def verify_help_and_support_page_send_feedback_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_send_feedback_widget_description", raise_e=False)

    def verify_help_and_support_page_send_feedback_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_send_feedback_widget_navigation_button", raise_e=False)

    ########################## Help and Support Page - My Support Cases Widget #########################

    def verify_help_and_support_page_my_support_cases_widget(self):
        return self.driver.wait_for_object("help_and_support_page_my_support_cases_widget", raise_e=False)
   
    def verify_help_and_support_page_my_support_cases_widget_title(self):
        return self.driver.verify_object_string("help_and_support_page_my_support_cases_widget_title", raise_e=False)
   
    def verify_help_and_support_page_my_support_cases_widget_description(self):
        return self.driver.verify_object_string("help_and_support_page_my_support_cases_widget_description", raise_e=False)

    def verify_help_and_support_page_my_support_cases_widget_navigation_button(self):
        return self.driver.wait_for_object("help_and_support_page_my_support_cases_widget_navigation_button", raise_e=False)