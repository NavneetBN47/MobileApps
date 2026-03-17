# encoding: utf-8
'''
Description: check send feedback screen

@author: ten
@create_date: July 22, 2019
'''

import logging
import time
from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class FeedBack(SmartScreens):
    folder_name = "menubar"
    flow_name = "feedback"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(FeedBack, self).__init__(driver)

    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("feedback_title", timeout=timeout, raise_e=raise_e)

    def wait_for_drop_down_option_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[wait_for_drop_down_option_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("feedback_dropdown_very_easy", timeout=timeout, raise_e=raise_e)

    def wait_for_thank_you_for_your_feedback_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[wait_for_thank_you_for_your_feedback_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("thank_you_for_your_feedback_title", timeout=timeout, raise_e=raise_e)

    def wait_for_to_better_support_you_dialog_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[wait_for_to_better_support_you_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("to_better_support_you_continue_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_feedback_title(self):
        '''
        This is a method to get the value of Give us your feedback screen title.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_title]-Get the value of Give us your feedback screen title...")

        return self.driver.get_value("feedback_title")

    def get_value_of_feedback_content_we_would_like_hear(self):
        '''
        This is a method to get the value of We would like to hear about ... content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_we_would_like_hear]-Get the value of We would like to hear about...")

        return self.driver.get_value("feedback_content_we_would_like_hear")

    def get_value_of_feedback_content_required(self):
        '''
        This is a method to get the value of Required content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_required]-Get the value of Required content...")

        return self.driver.get_value("feedback_content_required")

    def get_value_of_feedback_content_how_easy_was_to_use(self):
        '''
        This is a method to get the value of How easy was to use content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_how_easy_was_to_use]-Get the value of How easy was to use content...")

        return self.driver.get_value("feedback_content_how_easy_was_to_use")

    def get_value_of_feedback_content_how_likely_are_you(self):
        '''
        This is a method to get the value of How likely are you content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_how_likely_are_you]-Get the value of How likely are you content...")

        return self.driver.get_value("feedback_content_how_likely_are_you")

    def get_value_of_feedback_dropdown_very_easy(self):
        '''
        This is a method to get the value of Very Easy item on Give us your feedback screen after clicking drop down button.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_dropdown_very_easy]-Get the value of Very Easy item...")

        return self.driver.get_value("feedback_dropdown_very_easy")

    def get_value_of_feedback_dropdown_easy(self):
        '''
        This is a method to get the value of Easy item on Give us your feedback screen after clicking drop down button.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_dropdown_easy]-Get the value of Easy item...")

        return self.driver.get_value("feedback_dropdown_easy")

    def get_value_of_feedback_dropdown_average(self):
        '''
        This is a method to get the value of Average item on Give us your feedback screen after clicking drop down button.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_dropdown_average]-Get the value of Average item...")

        return self.driver.get_value("feedback_dropdown_average")

    def get_value_of_feedback_dropdown_difficult(self):
        '''
        This is a method to get the value of Difficult item on Give us your feedback screen after clicking drop down button.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_dropdown_difficult]-Get the value of Difficult item...")

        return self.driver.get_value("feedback_dropdown_difficult")

    def get_value_of_feedback_dropdown_very_difficult(self):
        '''
        This is a method to get the value of Very difficult item on Give us your feedback screen after clicking drop down button.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_dropdown_very_difficult]-Get the value of Very difficult item...")

        return self.driver.get_value("feedback_dropdown_very_difficult")

    def get_value_of_feedback_content_would_you_like_to_give(self):
        '''
        This is a method to get the value of Would you like to give content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_would_you_like_to_give]-Get the value of Would you like to give content...")

        return self.driver.get_value("feedback_content_would_you_like_to_give")

    def get_value_of_feedback_content_characters_remaining(self):
        '''
        This is a method to get the value of Characters Remaining content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_characters_remaining]-Get the value of Characters Remaining content...")

        return self.driver.get_value("feedback_content_characters_remaining")

    def get_value_of_feedback_content_your_comments_and_suggestions(self):
        '''
        This is a method to get the value of Your comments and suggestions... content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_your_comments_and_suggestions]-Get the value of Your comments and suggestions content...")

        return self.driver.get_value("feedback_content_your_comments_and_suggestions")

    def get_value_of_feedback_sendfeedback_btn(self):
        '''
        This is a method to get the value of Send Feedback button on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_sendfeedback_btn]-Get the value of Send Feedback button...")

        return self.driver.get_title("feedback_sendfeedback_btn")

    def get_value_of_feedback_content_do_you_need_help(self):
        '''
        This is a method to get the value of Do you need a help solving a problem content on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_feedback_content_do_you_need_help]-Get the value of Do you need a help solving a problem content...")

        return self.driver.get_value("feedback_content_do_you_need_help")

    def get_value_of_users_guide_and_faq_link(self):
        '''
        This is a method to get the value of Users Guide and FAQ link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_users_guide_and_faq_link]-Get the value of Users Guide and FAQ link...")

        return self.driver.get_title("users_guide_and_faq_link")

    def get_value_of_visit_our_hp_smart_support_forum_link(self):
        '''
        This is a method to get the value of Visit our HP Smart Support Forum link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_visit_our_hp_smart_support_forum_link]-Get the value of Visit our HP Smart Support Forum link...")

        return self.driver.get_title("visit_our_hp_smart_support_forum_link")

    def get_value_of_send_an_email_to_support_team_link(self):
        '''
        This is a method to get the value of Send an Email to Support Team link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_send_an_email_to_support_team_link]-Get the value of Send an Email to Support Team link...")

        return self.driver.get_title("send_an_email_to_support_team_link")

    def get_value_of_thank_you_for_your_feedback_title(self):
        '''
        This is a method to get the value of Thank you for your feedback screen title after clicking send feedback button on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_thank_you_for_your_feedback_title]-Get the value of Thank you for your feedback screen title...")

        return self.driver.get_value("thank_you_for_your_feedback_title")

    def get_value_of_thank_you_for_your_feedback_content(self):
        '''
        This is a method to get the value of Thank you for your feedback screen content after clicking send feedback button on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_thank_you_for_your_feedback_content]-Get the value of Thank you for your feedback screen content...")

        return self.driver.get_value("thank_you_for_your_feedback_content")

    def get_value_of_thank_you_for_your_feedback_done_btn(self):
        '''
        This is a method to get the value of Done button on Thank you for your feedback screen after clicking send feedback button on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_thank_you_for_your_feedback_done_btn]-Get the value of Done button on Thank you for your feedback screen...")

        return self.driver.get_title("thank_you_for_your_feedback_done_btn")

    def get_value_of_to_better_support_you_title(self):
        '''
        This is a method to get the value of To better support you dialog title after clicking Send an email to our support team link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_to_better_support_you_title]-Get the value of To better support you dialog title...")

        return self.driver.get_value("to_better_support_you_title")

    def get_value_of_to_better_support_you_content(self):
        '''
        This is a method to get the value of To better support you dialog content after clicking Send an email to our support team link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_to_better_support_you_content]-Get the value of To better support you dialog content...")

        return self.driver.get_value("to_better_support_you_content")

    def get_value_of_to_better_support_you_cancel_btn(self):
        '''
        This is a method to get the value of Cancel button on To better support you dialog after clicking Send an email to our support team link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_to_better_support_you_cancel_btn]-Get the value of Cancel button...")

        return self.driver.get_title("to_better_support_you_cancel_btn")

    def get_value_of_to_better_support_you_continue_btn(self):
        '''
        This is a method to get the value of Continue button on To better support you dialog after clicking Send an email to our support team link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[get_value_of_to_better_support_you_continue_btn]-Get the value of Continue button...")

        return self.driver.get_title("to_better_support_you_continue_btn")

    def click_dropdown_btn_1(self):
        '''
        This is a method to click drop down button on Give us feedback screen
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_dropdown_btn_1")
        
    def click_dropdown_btn_2(self):
        '''
        This is a method to click drop down button on Give us feedback screen
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_dropdown_btn_2")

    def click_feedback_gender_dropdown_btn(self):
        '''
        This is a method to click drop down button on Give us feedback screen
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_gender_dropdown_btn")

    def click_feedback_age_range_dropdown_btn(self):
        '''
        This is a method to click drop down button on Give us feedback screen
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_age_range_dropdown_btn")

    def click_selectoption_combobox(self):
        '''
        choose select option in combobox
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_select_option_combobox")

    def select_dropdown_listitem_very_easy(self):
        '''
        This is a method to select Very Easy option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_very_easy]-Select Very Easy option... ")

        self.driver.click("feedback_dropdown_very_easy", is_native_event=True)

    def click_feedback_dropdown_1_item(self):
        '''
        This is a method to select Easy option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_easy]-Select Easy option... ")

        self.driver.click("feedback_dropdown_1_item", is_native_event=True)

    def click_feedback_dropdown_2_item(self):
        '''
        This is a method to select Easy option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_easy]-Select Easy option... ")

        self.driver.click("feedback_dropdown_2_item", is_native_event=True)

    def click_feedback_gender_dropdown_btn_item(self):
        '''
        This is a method to select Easy option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_easy]-Select Easy option... ")

        self.driver.click("feedback_gender_dropdown_btn_item", is_native_event=True)

    def click_feedback_age_range_dropdown_btn_item(self):
        '''
        This is a method to select Easy option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_easy]-Select Easy option... ")

        self.driver.click("feedback_age_range_dropdown_btn_item", is_native_event=True)

    def select_dropdown_listitem_average(self):
        '''
        This is a method to select Average option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_average]-Select Average option... ")

        self.driver.click("feedback_dropdown_average", is_native_event=True)

    def select_dropdown_listitem_difficult(self):
        '''
        This is a method to select Difficult option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_difficult]-Select Difficult option... ")

        self.driver.click("feedback_dropdown_difficult", is_native_event=True)

    def select_dropdown_listitem_very_difficult(self):
        '''
        This is a method to select Very Difficult option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[select_dropdown_listitem_very_difficult]-Select Very Difficult option... ")

        self.driver.click("feedback_dropdown_very_difficult", is_native_event=True)

# Only can choose index 0, it should be a xpath issue for feedback_dropdown_listitems. Need to debug.
    def choose_dropdown_listitems(self, index):
        '''
        choose any option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_dropdown_listitem_1]click-feedback_dropdown_listitem_1button... ")

        self.driver.choose_combo_box_options("feedback_dropdown_btn", "feedback_dropdown_listitems", option_index=index)

    def input_textbox(self, contents):
        '''
        input text in textbox
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_textbox]input-feedback_textbox... ")

        self.driver.send_keys("feedback_textbox", contents, press_enter=True)

    def input_email(self, contents):
        '''
        input text in textbox
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[feedback_textbox]input-feedback_textbox... ")

        self.driver.send_keys("email_textbox", contents, press_enter=True)

    def click_star_item(self):
        '''
        click_feedback_sendfeedback_button
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[ffeedback_sendfeedback_btn]click-feedback_sendfeedback_btn... ")

        self.driver.click("star_item")

    def click_sendfeedback_btn(self):
        '''
        click_feedback_sendfeedback_button
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[ffeedback_sendfeedback_btn]click-feedback_sendfeedback_btn... ")
        self.driver.scroll_on_app()
        time.sleep(2)
        self.driver.click("feedback_sendfeedback_btn")

    def click_yes_item(self):
        '''
        click_yes_item
        :return:
        '''
        logging.debug("[FeedBack]:[ffeedback_sendfeedback_btn]click-yes_item... ")

        self.driver.click("yes_item")

    def click_how_likely_radio_item_0(self):
        '''
        This is a method to click to choose How Likely radio item 0
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_0]-click to choose How Likely radio item 0.. ")

        self.driver.click("feedback_likely_radio_item_0")

    def click_how_likely_radio_item_1(self):
        '''
        This is a method to click to choose How Likely radio item 1
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_1]-click to choose How Likely radio item 1.. ")

        self.driver.click("feedback_likely_radio_item_1")

    def click_how_likely_radio_item_2(self):
        '''
        This is a method to click to choose How Likely radio item 2
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_2]-click to choose How Likely radio item 2.. ")

        self.driver.click("feedback_likely_radio_item_2")

    def click_how_likely_radio_item_3(self):
        '''
        This is a method to click to choose How Likely radio item 3
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_3]-click to choose How Likely radio item 3.. ")

        self.driver.click("feedback_likely_radio_item_3")

    def click_how_likely_radio_item_4(self):
        '''
        This is a method to click to choose How Likely radio item 4
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_4]-click to choose How Likely radio item 4.. ")

        self.driver.click("feedback_likely_radio_item_4")

    def click_how_likely_radio_item_5(self):
        '''
        This is a method to click to choose How Likely radio item 5
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_5]-click to choose How Likely radio item 5.. ")

        self.driver.click("feedback_likely_radio_item_5")

    def click_how_likely_radio_item_6(self):
        '''
        This is a method to click to choose How Likely radio item 6
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_6]-click to choose How Likely radio item 6.. ")

        self.driver.click("feedback_likely_radio_item_6")

    def click_how_likely_radio_item_7(self):
        '''
        This is a method to click to choose How Likely radio item 7
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_7]-click to choose How Likely radio item 7.. ")

        self.driver.click("feedback_likely_radio_item_7")

    def click_how_likely_radio_item_8(self):
        '''
        This is a method to click to choose How Likely radio item 8
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_8]-click to choose How Likely radio item 8.. ")

        self.driver.click("feedback_likely_radio_item_8")

    def click_how_likely_radio_item_9(self):
        '''
        This is a method to click to choose How Likely radio item 9
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_9]-click to choose How Likely radio item 9.. ")

        self.driver.click("feedback_likely_radio_item_9")

    def click_how_likely_radio_item_10(self):
        '''
        This is a method to click to choose How Likely radio item 10
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_how_likely_radio_item_10]-click to choose How Likely radio item 10.. ")

        self.driver.click("feedback_likely_radio_item_10")

    def click_users_guide_and_faq_link(self):
        '''
        This is a method to click Users guide & FAQ link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_users_guide_and_faq_link]-Click Users guide & FAQ link.. ")

        self.driver.click("users_guide_and_faq_link", is_native_event=True)

    def click_visit_our_hp_smart_support_forum_link(self):
        '''
        This is a method to click Visit our HP Smart support forum link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_visit_our_hp_smart_support_forum_link]-Click Visit our HP Smart support forum link.. ")

        self.driver.click("visit_our_hp_smart_support_forum_link")

    def click_send_an_email_to_support_team_link(self):
        '''
        This is a method to click Send an email to support team link on Give us your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_send_an_email_to_support_team_link]-Click Send an email to support team link.. ")

        self.driver.click("send_an_email_to_support_team_link")

    def click_thank_you_for_your_feedback_done_btn(self):
        '''
        This is a method to click Done button on Thank you for your feedback screen.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_thank_you_for_your_feedback_done_btn]-Click Done button.. ")

        self.driver.click("thank_you_for_your_feedback_done_btn")

    def click_to_better_support_you_cancel_btn(self):
        '''
        This is a method to click Cancel button on To better support you dialog.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_to_better_support_you_cancel_btn]-Click Cancel button.. ")

        self.driver.click("to_better_support_you_cancel_btn")

    def click_to_better_support_you_continue_btn(self):
        '''
        This is a method to click Continue button on To better support you dialog.
        :parameter:
        :return:
        '''
        logging.debug("[FeedBack]:[click_to_better_support_you_continue_btn]-Click Continue button.. ")

        self.driver.click("to_better_support_you_continue_btn")

# -------------------------------Verification Methods--------------------------
    def verify_give_us_feedback_screen(self):
        '''
        This is a verification method to check UI strings of Give Us Feedback screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Give Us Feedback screen")
#         assert self.get_value_of_feedback_title() == u""
#         assert self.get_value_of_feedback_content_we_would_like_hear() == u""
#         assert self.get_value_of_feedback_content_required() == u""
#         assert self.get_value_of_feedback_content_how_easy_was_to_use() == u""
#         assert self.get_value_of_feedback_content_how_likely_are_you() == u""
#         assert self.get_value_of_feedback_content_would_you_like_to_give() == u""
#         assert self.get_value_of_feedback_content_characters_remaining() == u""
#         assert self.get_value_of_feedback_content_your_comments_and_suggestions() == u""
#         assert self.get_value_of_feedback_sendfeedback_btn() == u""
#         assert self.get_value_of_feedback_content_do_you_need_help() == u""
#         assert self.get_value_of_users_guide_and_faq_link() == u""
#         assert self.get_value_of_visit_our_hp_smart_support_forum_link() == u""
#         assert self.get_value_of_send_an_email_to_support_team_link() == u""

    def verify_drop_down_option_screen(self):
        '''
        This is a verification method to check UI strings of Drop down option on Give Us Feedback screen.
        :parameter:
        :return:
        '''
        self.wait_for_drop_down_option_screen_load()
        logging.debug("Start to check UI strings of Drop down option on Give Us Feedback screen")
#         assert self.get_value_of_feedback_dropdown_very_easy() == u""
#         assert self.get_value_of_feedback_dropdown_easy() == u""
#         assert self.get_value_of_feedback_dropdown_average() == u""
#         assert self.get_value_of_feedback_dropdown_difficult() == u""
#         assert self.get_value_of_feedback_dropdown_very_difficult() == u""

    def verify_send_feedback_btn_disable(self):
        '''
        This is a verification method to check Send Feedback button is disable
        :parameter:
        :return:
        '''
        logging.debug("verify Send Feedback button's behavior")
        if self.driver.is_enable("feedback_sendfeedback_btn"):
            raise UnexpectedItemPresentException("Send Feedback button is enabled")
        return True

    def verify_send_feedback_btn_enable(self):
        '''
        This is a verification method to check Send Feedback button is enable
        :parameter:
        :return:
        '''
        logging.debug("verify Send Feedback button's behavior")
        if not self.driver.is_enable("feedback_sendfeedback_btn"):
            raise UnexpectedItemPresentException("Send Feedback button is disabled")
        return True

    def verify_thank_you_for_your_feedback_screen(self):
        '''
        This is a verification method to check UI strings of Thank you for your feedback screen.
        :parameter:
        :return:
        '''
        self.wait_for_thank_you_for_your_feedback_screen_load()
        logging.debug("Start to check UI strings of Thank you for your feedback screen")
#         assert self.get_value_of_thank_you_for_your_feedback_title() == u""
#         assert self.get_value_of_thank_you_for_your_feedback_content() == u""
#         assert self.get_value_of_thank_you_for_your_feedback_done_btn() == u""

    def verify_to_better_support_you_dialog(self):
        '''
        This is a verification method to check UI strings of To better support you dialog after clicking Send an email to our support team link.
        :parameter:
        :return:
        '''
        self.wait_for_to_better_support_you_dialog_load()
        logging.debug("Start to check UI strings of To better support you dialog")
#         assert self.get_value_of_to_better_support_you_title() == u""
#         assert self.get_value_of_to_better_support_you_content() == u""
#         assert self.get_value_of_to_better_support_you_cancel_btn() == u""
#         assert self.get_value_of_to_better_support_you_continue_btn() == u""

    def verify_thankyou_title_enabled(self, timeout=30):
        '''
        verify thank you screen display
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[wait_for_screen_load]-Wait for screen loading successful... ")
        assert self.driver.wait_for_object("feedback_thankyou_title", timeout=timeout)
