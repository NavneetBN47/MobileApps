# encoding: utf-8
'''
Description: alignment_pattern_choices_dialog screen

@author: ten
@create_date: Nov 1, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class Alignment_Pattern_Choices_Dialog(SmartScreens):

    folder_name = "printersettings"
    flow_name = "alignment_pattern_choices_dialog"

    def __init__(self, driver):
        super(Alignment_Pattern_Choices_Dialog, self).__init__(driver)

# ------------------------------Operate Elements----------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("alignment_pattern_choices_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_alignment_pattern_choices_title(self):
        '''
        get_value_of_alignment_pattern_choices_title
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_alignment_pattern_choices_title-Get the contents of alignment_pattern_choices_title ...  ")

        return self.driver.get_value("alignment_pattern_choices_title")

    def get_value_of_alignment_pattern_choices_contents(self):
        '''
        get_value_of_alignment_pattern_choices_contents
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_alignment_pattern_choices-Get the contents of alignment_pattern_choices...  ")

        return self.driver.get_value("alignment_pattern_choices_contents")

    def get_value_of_dialog_with_text_content_title(self):
        '''
        get_value_of_dialog_with_text_content_title
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_dialog_with_text_content_title_title-Get the contents of dialog_with_text_content_title ...  ")

        return self.driver.get_value("dialog_with_text_content_title")

    def get_value_of_a_text(self):
        '''
        get_value_of_a_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_a_text-Get the contents of a_text ...  ")

        return self.driver.get_value("a_text")

    def get_value_of_b_text(self):
        '''
        get_value_of_b_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_b_text-Get the contents of b_text ...  ")

        return self.driver.get_value("b_text")

    def get_value_of_c_text(self):
        '''
        get_value_of_c_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_c_text-Get the contents of c_text ...  ")

        return self.driver.get_value("c_text")

    def get_value_of_d_text(self):
        '''
        get_value_of_d_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_d_text-Get the contents of d_text ...  ")

        return self.driver.get_value("d_text")

    def get_value_of_e_text(self):
        '''
        get_value_of_e_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_e_text-Get the contents of e_text ...  ")

        return self.driver.get_value("e_text")

    def get_value_of_f_text(self):
        '''
        get_value_of_f_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_f_text-Get the contents of f_text ...  ")

        return self.driver.get_value("f_text")

    def get_value_of_g_text(self):
        '''
        get_value_of_g_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_g_text-Get the contents of g_text ...  ")

        return self.driver.get_value("g_text")

    def get_value_of_h_text(self):
        '''
        get_value_of_h_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_h_text-Get the contents of h_text ...  ")

        return self.driver.get_value("h_text")

    def get_value_of_i_text(self):
        '''
        get_value_of_i_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_i_text-Get the contents of i_text ...  ")

        return self.driver.get_value("i_text")

    def get_value_of_j_text(self):
        '''
        get_value_of_j_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_j_text-Get the contents of j_text ...  ")

        return self.driver.get_value("j_text")

    def get_value_of_k_text(self):
        '''
        get_value_of_k_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_k_text-Get the contents of k_text ...  ")

        return self.driver.get_value("k_text")

    def get_value_of_l_text(self):
        '''
        get_value_of_l_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_l_text-Get the contents of l_text ...  ")

        return self.driver.get_value("l_text")

    def get_value_of_m_text(self):
        '''
        get_value_of_m_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_m_text-Get the contents of m_text ...  ")

        return self.driver.get_value("m_text")

    def get_value_of_n_text(self):
        '''
        get_value_of_n_text
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_n_text-Get the contents of n_text ...  ")

        return self.driver.get_value("n_text")

    def get_value_of_a_value(self):
        '''
        get_value_of_a_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_a_value-Get the contents of a_value ...  ")

        return self.driver.get_value("a_value")

    def get_value_of_b_value(self):
        '''
        get_value_of_b_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_b_value-Get the contents of b_value ...  ")

        return self.driver.get_value("b_value")

    def get_value_of_c_value(self):
        '''
        get_value_of_c_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_c_value-Get the contents of c_value ...  ")

        return self.driver.get_value("c_value")

    def get_value_of_d_value(self):
        '''
        get_value_of_d_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_d_value-Get the contents of d_value ...  ")

        return self.driver.get_value("d_value")

    def get_value_of_e_value(self):
        '''
        get_value_of_e_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_e_value-Get the contents of e_value ...  ")

        return self.driver.get_value("e_value")

    def get_value_of_f_value(self):
        '''
        get_value_of_f_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_f_value-Get the contents of f_value ...  ")

        return self.driver.get_value("f_value")

    def get_value_of_g_value(self):
        '''
        get_value_of_g_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_g_value-Get the contents of g_value ...  ")

        return self.driver.get_value("g_value")

    def get_value_of_h_value(self):
        '''
        get_value_of_b_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_h_value-Get the contents of h_value ...  ")

        return self.driver.get_value("h_value")

    def get_value_of_i_value(self):
        '''
        get_value_of_i_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_i_value-Get the contents of i_value ...  ")

        return self.driver.get_value("i_value")

    def get_value_of_j_value(self):
        '''
        get_value_of_j_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_j_value-Get the contents of j_value ...  ")

        return self.driver.get_value("j_value")

    def get_value_of_k_value(self):
        '''
        get_value_of_k_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_k_value-Get the contents of k_value ...  ")

        return self.driver.get_value("k_value")

    def get_value_of_l_value(self):
        '''
        get_value_of_l_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_l_value-Get the contents of l_value ...  ")

        return self.driver.get_value("l_value")

    def get_value_of_m_value(self):
        '''
        get_value_of_m_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_m_value-Get the contents of m_value ...  ")

        return self.driver.get_value("m_value")

    def get_value_of_n_value(self):
        '''
        get_value_of_n_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_n_value-Get the contents of n_value ...  ")

        return self.driver.get_value("n_value")

    def get_value_of_contents_1(self):
        '''
        get_value_of_contents_1
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_contents_1-Get the contents of contents_1 ...  ")

        return self.driver.get_value("contents_1")

    def get_value_of_done_btn(self):
        '''
        get_value_of_done_btn
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_done_btn-Get the contents of done_btn ...  ")

        return self.driver.get_title("done_btn")

    def get_value_of_exit_btn(self):
        '''
        get_value_of_exit_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_exit_btn-Get the contents of exit_btn ...  ")

        return self.driver.get_title("exit_btn")

    def get_value_of_close_btn(self):
        '''
        get_value_of_close_btn
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_close_btn-Get the contents of close_btn ...  ")

        return self.driver.get_title("close_btn")

    def click_done_btn(self):
        '''
        click_done_btn
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_done_btn")

        return self.driver.click("done_btn")

    def click_exit_btn(self):
        '''
        click_exit_btn
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_exit_btn")

        return self.driver.click("exit_btn")

    def click_close_btn(self):
        '''
        click_close_btn
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_close_btn")

        return self.driver.click("close_btn")

    def choose_a1_item(self, index):
        '''
        click_a1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_a1_item")

        self.driver.choose_combo_box_options("a_dropdown_btn", "a_item", option_index=index)

    def choose_b1_item(self, index):
        '''
        click_b1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_b1_item")

        self.driver.choose_combo_box_options("b_dropdown_btn", "b_item", option_index=index)

    def choose_c1_item(self, index):
        '''
        click_c1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_c1_item")

        self.driver.choose_combo_box_options("c_dropdown_btn", "c_item", option_index=index)

    def choose_d1_item(self, index):
        '''
        click_d1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_d1_item")

        self.driver.choose_combo_box_options("d_dropdown_btn", "d_item", option_index=index)

    def choose_e1_item(self, index):
        '''
        click_e1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_e1_item")

        self.driver.choose_combo_box_options("e_dropdown_btn", "e_item", option_index=index)

    def choose_f1_item(self, index):
        '''
        click_f1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_f1_item")

        self.driver.choose_combo_box_options("f_dropdown_btn", "f_item", option_index=index)

    def choose_g1_item(self, index):
        '''
        click_g1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_g1_item")

        self.driver.choose_combo_box_options("g_dropdown_btn", "g_item", option_index=index)

    def choose_h1_item(self, index):
        '''
        click_h1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_h1_item")

        self.driver.choose_combo_box_options("h_dropdown_btn", "h_item", option_index=index)

    def choose_i1_item(self, index):
        '''
        click_i1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_i1_item")

        self.driver.choose_combo_box_options("i_dropdown_btn", "i_item", option_index=index)

    def choose_j1_item(self, index):
        '''
        click_j1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_j1_item")

        self.driver.choose_combo_box_options("j_dropdown_btn", "j_item", option_index=index)

    def choose_k1_item(self, index):
        '''
        click_d1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_k1_item")

        self.driver.choose_combo_box_options("k_dropdown_btn", "k_item", option_index=index)

    def choose_l1_item(self, index):
        '''
        click_l1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_l1_item")

        self.driver.choose_combo_box_options("l_dropdown_btn", "l_item", option_index=index)

    def choose_n1_item(self, index):
        '''
        click_n1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_n1_item")

        self.driver.choose_combo_box_options("n_dropdown_btn", "n_item", option_index=index)

    def choose_m1_item(self, index):
        '''
        click_m1_item
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[click_m1_item")

        self.driver.choose_combo_box_options("m_dropdown_btn", "m_item", option_index=index)


# ------------------------------Verification Methods---------------------------------
    def verify_ui_string(self):
        '''
        Verify alignment_pattern_choices_dialog screen
        :parameter:
        :return:
        '''
        logging.debug("Verify alignment_pattern_choices_dialog screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='alignment_pattern_choices_dialog')
        assert self.get_value_of_alignment_pattern_choices_title() == test_strings['alignment_pattern_choices_title']
        assert self.get_value_of_alignment_pattern_choices_contents() == test_strings['alignment_pattern_choices_contents']
        assert self.get_value_of_done_btn() == test_strings['done_btn']
        assert self.get_value_of_exit_btn() == test_strings['exit_btn']

    def verify_alignment_pattern_choices_dialog_with_text_content(self):
        '''
        verify_alignment_pattern_choices_dialog_with_text_content
        :parameter:
        :return:
        '''
        logging.debug("verify_alignment_pattern_choices_dialog_with_text_content")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='alignment_pattern_choices_dialog')
        assert self.get_value_of_dialog_with_text_content_title() == test_strings['alignment_pattern_choices_title']
        assert self.get_value_of_contents_1() == test_strings['contents_1']
        assert self.get_value_of_close_btn() == test_strings['close_btn']

    def verify_alignment_pattern_choices_disappear(self):
        '''
        verify_alignment_pattern_choices_disappear
        :parameter:
        :return:
        '''
        logging.debug("verify_alignment_complete_dialogue_disappear")
        # if self.driver.wait_for_object("alignment_pattern_choices_title", raise_e=False):
        #     raise UnexpectedItemPresentException("the screen still exists")
        # return True
        return self.driver.wait_for_object("alignment_pattern_choices_title", invisible=True, raise_e=False)
