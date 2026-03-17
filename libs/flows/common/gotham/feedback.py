from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow

class ContentRequiredException(Exception):
    pass

class ContentMissingException(Exception):
    pass

class Feedback(GothamFlow):
    flow_name = "feedback"

    USER_GUIDE_FAQ = ["support.hp.com"]
    SMART_FORUM = ["Printer-Setup-Software-Drivers"]

    REASON = "main reason"
    MODEL = "printer model"
    GENDER = "gender"
    AGE = "age"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_feedback_page_title(self):
        """
        Need to click somewhere else to collapse the dropdown list.
        """
        self.driver.click("feedback_title")

    def select_satisfication_stars(self, star_idx):
        """
        @param star_idx:
            1 ~ 5
        """
        el = self.driver.find_object("satisfication_stars")
        self.driver.click_by_coordinates(el, 12 * (2 * star_idx - 1), 16)

    # ---------------- dropdown ---------------- #
    # Expand the dropdown list
    def select_reason_dropdown(self):
        self.driver.click("reason_dropdown")

    def select_printer_model_dropdown(self):
        self.driver.click("printer_model_dropdown")

    def select_gender_dropdown(self):
        self.driver.swipe()
        self.driver.click("gender_dropdown")

    def select_age_range_dropdown(self):
        self.driver.swipe()
        self.driver.click("age_range_dropdown")
    # ---------------- dropdown ---------------- #

    def select_dropdown_listitem(self, dropdown, name):
        """
        @param dropdown:
            - main reason
            - printer model
            - gender
            - age

        @param name:
            name of the listitem
        """
        if dropdown == "main reason":
            self.select_reason_dropdown()
        elif dropdown == "printer model":
            self.select_printer_model_dropdown()
        elif dropdown == "gender":
            self.select_gender_dropdown()
        elif dropdown == "age":
            self.select_age_range_dropdown()

        self.verify_dropdown_listitem(name).click()

    def select_recommendation(self, num):
        """
        @param num:
            0 ~ 10
        """
        self.driver.click("dynamic_radio_btn", format_specifier=[str(num)])

    def write_other_reason(self, content):
        """
        Fill in reason if select Other.
        """
        self.driver.wait_for_object("reason_textbox")
        return self.driver.send_keys("reason_textbox", content)

    def write_printer_model(self, content):
        """
        Fill in printer model if select Other.
        """
        self.driver.wait_for_object("printer_model_textbox")
        self.driver.send_keys("printer_model_textbox", content)
        return self.driver.find_object("printer_model_textbox")

    def write_additional_opinion(self, content):
        """
        Write in "Additional Feedback" textbox.
        """
        self.driver.wait_for_object("additional_feedback_textbox")
        self.driver.send_keys("additional_feedback_textbox", content)
        return self.driver.find_object("additional_feedback_textbox")

    def click_additional_opinion_title(self):
        self.driver.click("additional_feedback_title")

    def select_email_back(self, answer_idx):
        """
        An email address is not a must even you select Yes.

        @param answer:
            0 = Yes
            1 = No
        """
        answer = ["Yes", "No"]
        self.driver.click("dynamic_radio_btn", format_specifier=[answer[answer_idx]])

    def input_email_address(self, content):
        self.driver.wait_for_object("email_back_textbox")
        self.driver.send_keys("email_back_textbox", content)

    def select_submit_btn(self, raise_e=False):
        if self.driver.click("submit_btn", raise_e=raise_e) is False:
            self.driver.click("_system_max_btn")
            self.driver.click("submit_btn")

    def click_submit_btn_for_invalid_email_test(self):
        self.driver.click("submit_btn")

    # ---------------- three links ---------------- #
    def select_user_guide_faq_link(self):
        self.driver.swipe()
        self.driver.click("user_guide_faq_link")

    def select_hp_support_forum_link(self):
        self.driver.swipe()
        self.driver.click("hp_support_forum_link")

    def select_send_email_link(self):
        self.driver.swipe()
        self.driver.click("send_email_link")
    # ---------------- three links ---------------- #

    # ---------------- send email dialog ---------------- #
    def select_email_cancel_btn(self):
        self.driver.click("send_email_cancel_btn")

    def select_email_continue_btn(self):
        self.driver.click("send_email_continue_btn")
    # ---------------- send email dialog ---------------- #

    # ---------------- thank you for feedback screen ---------------- #
    def select_done_btn(self):
        self.driver.click("thank_you_done_btn")
    # ---------------- thank you for feedback screen ---------------- #

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_feedback_screen(self):
        self.driver.wait_for_object("feedback_title")

    def verify_thank_you_feedback_screen(self):
        self.driver.wait_for_object("thank_you_title")
        self.driver.wait_for_object("thank_you_subtitle")

    def verify_dropdown_listitem(self, name):
        return self.driver.wait_for_object("dynamic_listitem", format_specifier=[name])

    def verify_recommendation_radio_btn(self, num):
        """
        @param num:
            0 ~ 10
        """
        return self.driver.wait_for_object("dynamic_radio_btn", format_specifier=[str(num)])

    # ---------------- send email dialog ---------------- #
    def verify_email_dialog_title(self, raise_e=True):
        return self.driver.wait_for_object("send_email_title", raise_e=raise_e)

    def verify_email_cancel_btn(self):
        self.driver.wait_for_object("send_email_cancel_btn")

    def verify_email_continue_btn(self):
        self.driver.wait_for_object("send_email_continue_btn")

    def verify_invalid_address_text(self):
        self.driver.wait_for_object("invalid_email_address_text")
    # ---------------- send email dialog ---------------- #
