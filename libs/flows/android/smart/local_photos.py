from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time

class LocalPhotos(SmartFlow):
    flow_name = "local_photos"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def select_album(self, album_name):
        """
        At Select Photo screen:
            - Click on target album by name
        Note: -> Album should have some photos. (4 or 5 is good)
        :param album_name: album's name
        """
        # New image picker is available as it comes with Google Play service not based on OS version. User either see Select a Photo screen or Photo Picker optional screen
        if not self.verify_select_photo_screen(raise_e=False):
            self.verify_photo_picker_optional_screen()
            self.select_album_btn()
        if not self.driver.scroll("photo_album_title", format_specifier=[album_name], scroll_object="photos_lv", timeout=60, check_end=False, click_obj=True, raise_e=False):
            self.driver.scroll("photo_album_title", direction="up", format_specifier=[album_name],scroll_object="photos_lv", timeout=60, check_end=False, click_obj=True)

    def select_album_photo_by_index(self, album_name, photo_index=1, change_check={"wait_obj": "photo_thumbnail", "invisible": True}):
        """
        At Select Photo screen:
            - Click on target album by name
            - Select its photo by index number
        Note: At screen of target album, photo_index only apply all elements at first list.
              -> Album should have some photos. (4 or 5 is good)
              PHOTO THUMBNAIL STARTS INDEX AT 1
        End of flow: Landing Page or Select Photo screen based on types of photo
                        + supported type such as png,jpg,...: Landing Page
                        + unsupported type: stay at Select Photos screen
        :param album_name: album's name
        :param photo_index: index number of photo
        """
        # New image picker is available as it comes with Google Play service not based on OS version. User either see Select a Photo screen or Photo Picker optional screen
        time.sleep(3)
        self.select_album_btn(raise_e=False)
        if not self.driver.scroll("photo_album_title", format_specifier=[album_name], scroll_object="photos_lv",timeout=90, check_end=False, raise_e=False):
            self.driver.scroll("photo_album_title", direction="up", format_specifier=[album_name],scroll_object="photos_lv", timeout=90, check_end=False)
        self.driver.click("photo_album_title", format_specifier=[album_name], change_check={"wait_obj": "photo_thumbnail", "invisible": False})
        self.driver.click("photo_thumbnail", index=photo_index - 1, change_check=change_check)

    def select_cancel_btn(self):
        """
        Click on X button on Select a photo screen
        """
        self.driver.click("close_btn")

    def select_album_btn(self, raise_e=False):
        """
        Click on Album button from Photo Picker Optional screen
        """
        self.driver.click("album_option", raise_e=raise_e)

    def select_photo_btn(self):
        """
        Click on Album button from Photo Picker Optional screen
        """
        self.driver.click("photo_option")

    def select_photo_picker_add_btn(self):
        """
        Click on Add button on Photo Picker Optional screen
        """
        self.driver.click("photo_picker_add_btn")

    def select_photo_picker_view_selected_btn(self):
        """
        Click on View Selected button on Photo Picker Optional screen
        """
        self.driver.click("photo_picker_view_selected_btn")

    def select_photo_picker_done_btn(self):
        """
        Click on Done button for old Photo Picker Optional screen
        """
        self.driver.click("done_btn")

    def select_recent_photo_by_index(self, album_name="jpg", photo_index=1):
        """
        At Select Photo screen:
            - Select its photo by index number
        Note: At screen of Recent Photo tab, photo_index only apply all elements at first list.
              -> Recent Photo tab should have some photos. (4 or 5 is good)
              PHOTO THUMBNAIL STARTS INDEX AT 1
        :param photo_index: index number of photo
        """
        if self.verify_select_photo_screen(raise_e=False):
            self.driver.scroll("photo_album_title", format_specifier=[album_name], scroll_object="photos_lv", timeout=60, check_end=False, click_obj=True)
        self.driver.click("photo_thumbnail", index=photo_index - 1)

    def get_number_selection(self):
        """
        Get number of selected photos
        :return: number of selected photos
        """
        return self.driver.get_attribute("selected_num_txt", "text")

    def select_multiple_photos(self, num, album_name="jpg"):
        """
        Select multiple photos on Photo Picker Optional screen
        """
        if self.verify_select_photo_screen(raise_e=False):
            self.driver.scroll("photo_album_title", format_specifier=[album_name], scroll_object="photos_lv", timeout=60, check_end=False, click_obj=True)
        for i in range(0, num):
            self.driver.click("photo_thumbnail", index=i)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_select_photo_screen(self, raise_e=False):
        """
        Verify that current screen is 'Select a Photos' via:
            - It's title
        """
        return self.driver.wait_for_object("select_photo_title", raise_e=raise_e)

    def verify_photo_picker_optional_screen(self, raise_e=True, timeout=15):
        """
        Verify that current screen is Photo picker optional screen:
            - Album option
            - Message: This app can only access the photos you select
        """
        return self.driver.wait_for_object("photo_picker_option", raise_e=raise_e, timeout=timeout) and self.driver.wait_for_object("album_option", raise_e=raise_e)

    def verify_photo_picker_view_selected_option(self, raise_e=True):
        """
        Verify View Selected button on Photo Picker Optional screen
        """
        return self.driver.wait_for_object("photo_picker_view_selected_btn", raise_e=raise_e)

    def verify_photo_picker_add_option(self, raise_e=True):
        """
        Verify Add button on Photo Picker Optional screen
        """
        return self.driver.wait_for_object("photo_picker_add_btn", raise_e=raise_e)

    def verify_photo_picker_closed_option(self, raise_e=True):
        """
        Verify Close button for old Photo Picker Optional screen
        """
        return self.driver.wait_for_object("close_btn", raise_e=raise_e)

    def verify_multi_selection_screen(self):
        """
        Verify Multi-Selection screen of Photos for old version of photo picker via:
            - X icon button
            - Number of selection text
            - Done button
        """
        self.driver.wait_for_object("close_btn")
        self.driver.wait_for_object("selected_num_txt")
        self.driver.wait_for_object("done_btn")