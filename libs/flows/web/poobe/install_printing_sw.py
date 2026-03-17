from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class InstallPrintingSW(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Install Printing SW page of the LF (Large Format) FLOW currently for Beam
    """
    file_path = __file__
    flow_name = "install_printing_sw"

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_personal_or_business_printer(self, p_type):
        self.driver.wait_for_object("install_driver_sw_link")

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    def verify_install_printing_sw_page(self, timeout=10, raise_e=False):
        """
        Verify LF Beam Install Printing SW page
        """
        return self.driver.wait_for_object("install_printing_sw_page", timeout=timeout, raise_e=raise_e)

    def verify_copy_templete_btn(self):
        self.driver.wait_for_object("copy_templete_btn")

    def verify_template_text_box(self):
        self.driver.wait_for_object("template_text")

    def verify_install_printer_driver_link(self):
        self.driver.wait_for_object("install_driver_sw_link")