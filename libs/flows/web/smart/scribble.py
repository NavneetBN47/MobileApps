from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from random import random
from time import time, sleep

class Scribble(SmartFlow):
    flow_name = "scribble"

    # ------------------------------- Place Your Mark Screen -------------------------------

    def select_new_mark_button(self):
        """
        From the Place Your Mark screen, select the new mark button on the bottom bar
        """
        self.driver.click("new_mark_button", timeout=8)

    def select_saved_marks_btn(self):
        """
        From the Place Your Mark screen, select the saved marks button
        """
        self.driver.click("saved_marks_btn")

    def move_signature(self, direction="down", distance=100):
        """
        From the Place Your Mark screen, move the signature in the specified direction
        """
        sleep(1)
        drawn_mark_obj = self.driver.wait_for_object("drawn_mark")
        drawn_mark_pos = self.driver.selenium.execute_script("return arguments[0].getBoundingClientRect()", drawn_mark_obj)
        scribble_webview_size = self.driver.wdvr.get_window_size()
        if self.driver.driver_info['platform'].lower() == "ios":
            self.driver.switch_to_webview("NATIVE")
            scribble_native_size = self.driver.wdvr.get_window_size()
            self.driver.switch_to_webview("scribble")
            y_dist_header = scribble_native_size['height']-scribble_webview_size['height']
            start_pos = [drawn_mark_pos['x']+drawn_mark_pos['width']/2, y_dist_header+drawn_mark_pos['y']+drawn_mark_pos['height']/2]
            end_pos = [start_pos[0], start_pos[1]]
        else:
            self.driver.switch_to_webview("NATIVE_APP")
            scribble_native_size = self.driver.wdvr.get_window_rect()
            x_scale, y_scale = scribble_native_size['width']/scribble_webview_size['width'], scribble_native_size['height']/scribble_webview_size['height']
            start_pos = [(drawn_mark_pos['x']+drawn_mark_pos['width']/2)*x_scale, (drawn_mark_pos['y']+drawn_mark_pos['height']/2)*y_scale]
            start_pos = [(drawn_mark_pos['x']+drawn_mark_pos['width']/2), (drawn_mark_pos['y']+drawn_mark_pos['height']/2)]
            end_pos = [start_pos[0], start_pos[1]]
        if direction=="down":
            end_pos[1] += distance
        elif direction=="up":
            end_pos[1] -= distance
        elif direction=="left":
            end_pos[0] -= distance
        elif direction=="right":
            end_pos[0] += distance
        else:
            raise ValueError("{} given. Please pass 'up' 'down' 'left' or 'right'".format(direction))
        self.driver.touch_action.long_press(x=start_pos[0], y=start_pos[1], duration=2000).move_to(x=end_pos[0], y=end_pos[1]).wait(500).release().perform()

    def scale_signature(self):
        """
        From the Place Your Mark screen, scale the signature larger
        """
        self.driver.switch_to_webview("NATIVE")
        place_your_mark_webview_native_size = self.driver.wdvr.get_window_size()
        self.driver.switch_to_webview("scribble")
        drawn_mark_obj = self.driver.wait_for_object("drawn_mark")
        drawn_mark_pos = self.driver.selenium.execute_script("return arguments[0].getBoundingClientRect()", drawn_mark_obj)
        place_your_mark_webview_size = self.driver.wdvr.get_window_size()
        y_dist_header = place_your_mark_webview_native_size['height']-place_your_mark_webview_size['height']
        start_pos = drawn_mark_pos['x']+drawn_mark_pos['width'], drawn_mark_pos['y']+drawn_mark_pos['height']+y_dist_header
        end_pos = start_pos[0]+50, start_pos[1]
        self.driver.drag_and_drop(start_pos, end_pos)

    def select_navigate_back_btn(self):
        """
        From the Place Your Mark screen, select the back arrow button in the top left
        """
        self.driver.click("scribble_back_btn")

    def select_new_mark_btn(self):
        """
        From the Place Your Mark screen, select the new mark button on the bottom bar
        """
        self.driver.click("new_mark_btn")

    def verify_and_close_move_mark_coachmark_pop_up(self):
        """
        From the Place Your Mark screen, After placing and moving the mark on a document for the first time, verify coachmark pop up 
        """
        assert "scale" in self.driver.wait_for_object("place_mark_coachmark_popup", raise_e=False, timeout=3).text.lower()
        self.driver.click("place_mark_coachmark_next_btn")
        assert "done" in self.driver.wait_for_object("place_mark_coachmark_popup", raise_e=False, timeout=3).text.lower()
        self.driver.click("place_mark_coachmark_popup_close_btn")
        return not self.driver.wait_for_object("place_mark_coachmark_popup", raise_e=False, timeout=3)

    def verify_signature(self, multiple=False):
        """
        From the Place Your Mark screen, verify the existance of a placed mark
        """
        return self.driver.wait_for_object("drawn_mark", timeout=3, raise_e=False) if multiple is False else len(self.driver.find_object("drawn_mark", multiple=True)) > 1

    def verify_new_mark_page(self):
        """
        Verify 'mark' in the header for the new mark screen
        """
        return "mark" in self.driver.wait_for_object("new_mark_header").text.lower()

    # ------------------------------- Add a New Mark Screen -------------------------------

    def dismiss_welcome_to_scribble_pop_up(self):
        """
        From the Add a New Mark signature screen, dismiss welcome popup if it's present
        """
        if self.driver.wait_for_object("dismiss_scribble_pop_up_btn", timeout=3, raise_e=False):
            self.driver.click("dismiss_scribble_pop_up_btn")

    def select_trash_btn(self):
        """
        From the Add a New Mark Draw signature screen, select the trash btn
        """
        self.driver.click("trash_btn")

    def select_save_btn(self):
        """
        From the Add a New Mark Draw signature screen, select the save btn
        """
        self.driver.click("save_btn")

    def swipe_on_scribble_pad(self):
        """
        From the Add a New Mark signature screen, draw a new unique scribble 
        """
        scribble_pad_obj = self.driver.wait_for_object("scribble_pad")
        scribble_pad_pos = self.driver.selenium.execute_script("return arguments[0].getBoundingClientRect()", scribble_pad_obj)
        if self.driver.driver_info['platform'].lower() == "ios":
            start_pos = scribble_pad_pos['x'], scribble_pad_pos['y']+scribble_pad_pos['height']/2
            end_pos = scribble_pad_pos['width']+start_pos[0], start_pos[1]
        else:  
            scribble_webview_size = self.driver.wdvr.get_window_size()
            self.driver.switch_to_webview("NATIVE_APP")
            scribble_native_size = self.driver.wdvr.get_window_rect()
            x_scale, y_scale = scribble_native_size['width']/scribble_webview_size['width'], scribble_native_size['height']/scribble_webview_size['height']
            start_pos = scribble_pad_pos['x']*x_scale, (scribble_pad_pos['y']+scribble_pad_pos['height']/2)*y_scale
            end_pos = scribble_pad_pos['width']*x_scale+start_pos[0], start_pos[1]
        touch_action = self.driver.touch_action.long_press(x=start_pos[0], y=start_pos[1], duration=100)
        x_step = (end_pos[0]-start_pos[0])/10
        for i in range(10):
            y = end_pos[1]-random()*15 if random()<0.5 else end_pos[1]+random()*15
            touch_action.move_to(x=start_pos[0]+x_step*i, y=y).wait(250)
        touch_action.release().perform()

    def select_scribble_option(self, option="thin"):
        """
        From the Add a New Mark signature screen, select one of the four scribble options in the bottom bar
        """
        option = option.lower()
        if option not in ["thin", "medium", "thick", "text"]:
            raise ValueError("{} given. Please pass 'thin' 'medium' 'thick' or 'text'".format(option))
        self.driver.click("stroke_thickness_btn", format_specifier=[option]) if option!="text" else self.driver.click("markup_text_option")

    def send_text_to_markup_textbox(self, text):
        """
        From the Add a New Mark signature screen, after selecting the markup text option, send text to textbox
        """
        self.driver.send_keys("markup_textbox", text)

    # ------------------------------- Saved Marks Screen -------------------------------

    def select_saved_marks_select_btn(self):
        """
        From the Saved Marks screen, select the select button in the top right 
        """
        self.driver.click("select_saved_marks_btn")

    def select_saved_mark(self):
        """
        From the Saved Marks screen, select the first signature
        """
        self.driver.click("saved_mark_image")

    def select_single_unchecked_saved_mark(self, displayed=True):
        """
        From the Saved Marks screen, after clicking select button, select the first signature's checkbox
        """
        self.driver.click("saved_mark_image_unchecked", displayed=displayed)

    def select_delete_selected_btn(self):
        """
        From the Saved Marks screen, select Delete Selected button in the bottom bar
        """
        self.driver.click("delete_selected_btn")

    def get_first_saved_mark_data(self):
        """
        From the Saved Marks screen, get the image data of the first signature
        """
        return self.driver.get_attribute("saved_mark_image_data", "src")

    def delete_all_marks(self, displayed=True):
        """
        From the Saved Marks screen, select every unchecked signature images
        """
        timeout=60+time()
        while timeout-time() > 0 and self.driver.wait_for_object("saved_mark_image_unchecked", raise_e=False, timeout=3, displayed=displayed):
            unchecked_signatures_count = len(self.driver.find_object("saved_mark_image_unchecked", multiple=True))
            unchecked_signatures_count = 8 if unchecked_signatures_count > 8 else unchecked_signatures_count
            for i in range(unchecked_signatures_count):
                self.driver.click("saved_mark_image_unchecked", displayed=displayed)
            self.select_delete_selected_btn()

    def verify_empty_saved_marks_list(self):
        """
        From the Saved Marks screen, verify that there are no saved marks in the list
        """
        return self.driver.wait_for_object("empty_marks_list_text", timeout=3, raise_e=False)

    # ------------------------------- Select Your Page Screen -------------------------------

    def select_grid_option_multiple_pages(self):
        """
        From the Select Your Page screen, verify that the grid option is selected
        """
        self.driver.click("grid_view_btn")

    def select_full_screen_page_image(self):
        """
        From the Select Your Page screen, select the full screen page 
        """
        self.driver.click("full_page_image")

    def select_grid_screen_first_page_image(self):
        """
        From the Select Your Page screen, select the first page in the grid 
        """
        self.driver.click("grid_page_first_image")

    def verify_full_view_mode_multiple_pages(self):
        """
        From the Select Your Page screen, verify that the fullscreen option is selected 
        """
        return self.driver.wait_for_object("full_page_selection", timeout=3, raise_e=False)
    
    def verify_grid_view_mode_mulitple_pages(self):
        """
        From the Select Your Page screen, verify that the grid option is selected
        """
        return self.driver.wait_for_object("grid_page_selection", timeout=3, raise_e=False)

    # ------------------------------------- Misc -------------------------------------

    def get_header_height(self):
        """
        Return the pixel count of the header found above the webview to determine if Phone is notched
        """
        self.driver.switch_to_webview("NATIVE")
        native_size = self.driver.wdvr.get_window_size()
        self.driver.switch_to_webview("scribble")
        webview_size = self.driver.wdvr.get_window_size()
        return native_size['height']-webview_size['height']