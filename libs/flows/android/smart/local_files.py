from selenium.common.exceptions import NoSuchElementException
from SAF.exceptions.saf_exceptions import ObjectFoundException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LocalFiles(SmartFlow):
    flow_name = "local_files"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def load_downloads_folder_screen(self):
        """
        Load Download folder screen
        """
        if not self.verify_downloads_folder_screen(raise_e=False):
            self.driver.click("drawer_menu_btn")
            self.driver.wait_for_object("drawer_layout", timeout=10)
            self.driver.click("drawer_item", format_specifier=[self.get_text_from_str_id("download_txt")],
                              change_check={"wait_obj": "drawer_item", "invisible": True,
                                            "format_specifier": [self.get_text_from_str_id("download_txt")]})
        self.verify_downloads_folder_screen()

    def select_file(self, file_name, long_press=False, change_check={"wait_obj": "drawer_menu_btn", "invisible": True}):
        """
        Select a file by file name
        :param file_name:
        :param long_press: Long press instead of click.
        :param change_check: Change check for clicking on file. Ignored when using long_press. Use None when clicking a folder.
        """
        if not self.driver.scroll("file_name_title", format_specifier=[file_name], timeout=60, check_end=False, raise_e=False):
            self.driver.scroll("file_name_title", direction="up", format_specifier=[file_name], timeout=60, check_end=False)
        if long_press:
            self.driver.long_press("file_name_title", format_specifier=[file_name])
        else:
            self.driver.click("file_name_title", format_specifier=[file_name], change_check=change_check)
            self.driver.click("file_name_title", format_specifier=[file_name], raise_e=False)

    def save_file_to_downloads_folder(self, file_name):
        """
        Save file to download folder:
            - Load Downloads folder
            - Change file name (including file extension, such as file_name.pdf)
            - Click on Save button
        :param file_name: file name, including file extension
        """
        self.load_downloads_folder_screen()
        self.driver.send_keys("file_name_edit_text", content=file_name)
        self.driver.click("save_btn", change_check={"wait_obj": "drawer_menu_btn", "invisible": True})

    def select_select_button(self):
        """
        After selecting multiple files, select the select button to the right of the top navigation bar 
        """
        self.driver.click("select_btn")

    def select_list_view_button(self):
        """
        Select the list view button if it's present on the screen
        """
        if self.driver.wait_for_object("list_view_button", timeout=2, raise_e=False):
            self.driver.click("list_view_button")

    def select_save_btn(self):
        """
        click save button in files directory
        """
        self.driver.click("save_btn")

    # *********************************************************************************
    #                               VERIFICATION FLOWS                                *
    # *********************************************************************************

    def verify_selected_file_count(self, count):
        """
        Verifies the number of files selected based on the selection_txt at the top of the screen.
        :param count: The expected number of images selected.
        """
        selection_txt = self.driver.get_attribute("selection_txt", "text", raise_e=False)
        if selection_txt:
            selected = int(selection_txt[0:selection_txt.index(" ")])
        else:
            selected = 0
        assert count == selected, "Selected count {} does not match expected count {}".format(selected, count)

    def verify_downloads_folder_screen(self, invisible=False, raise_e=True):
        """
        Verify Downloads folder screen as current screen via
            - title
        """
        return self.driver.wait_for_object("title", format_specifier=[self.get_text_from_str_id("download_txt").lower()],
                                           timeout=10, raise_e=raise_e, invisible=invisible)

    def verify_selected_file(self, invisible=True):
        """
        Verify the text of the number of files is invisible if no files selected
        """
        self.driver.wait_for_object("selection_txt", invisible=invisible)
        