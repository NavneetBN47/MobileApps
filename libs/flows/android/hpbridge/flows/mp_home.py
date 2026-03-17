# coding: utf-8
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from time import sleep
import logging


class MPHome(HPBridgeFlow):
    flow_name = "mp_home"

    def __init__(self, driver):
        super(MPHome, self).__init__(driver)
        self.context = "WEBVIEW_com.tencent.mm:appbrand0"
        self.page = "pages/index"

    def check_add_printer_filed_no_device(self):
        """
        if there is no printer was bound, the message should be displayed: "添加打印机，即可开始打印"
        :return:
        """

        self.driver.wait_for_object("add_printer", timeout=20)
        self.driver.find_object("add_printer_icon")

    def check_add_printer_filed_with_device(self):
        """
        if there is already printer bound, check the printer list field
        :return:
        """

        self.check_printer_list_filed_fold()
        self.driver.click("printer_component")
        self.check_printer_list_filed_unfold()


    def check_printer_list_filed_fold(self):
        """
        check the printer list field when the printer details filed is fold
        :return:
        """
        self.driver.wait_for_object("printer_component")
        # self.driver.wait_for_object("printer_status_icon_fold", )
        self.driver.find_object("printer_icon")
        self.driver.find_object("printer_name")
        self.driver.find_object("printer_refresh")
        self.driver.find_object("print_task_button")
        self.driver.find_object("add_another_printer")
        # self.driver.wait_for_object("printer_status_icon_unfold", invisible=True)
        self.driver.wait_for_object("printer_cartridge", invisible=True)
        self.driver.wait_for_object("printer_setting", invisible=True)
        self.driver.wait_for_object("printer_share", invisible=True)
        self.driver.wait_for_object("printer_status_description", invisible=True)

    def check_printer_list_filed_unfold(self):
        """
        check the printer list filed when the printer details filed is unfold
        :return:
        """
        self.driver.wait_for_object("printer_component")
        self.driver.find_object("printer_name")
        self.driver.find_object("printer_refresh")
        self.driver.find_object("print_task_button")
        self.driver.find_object("add_another_printer")
        self.driver.find_object("printer_img")
        self.driver.find_object("printer_status_icon_unfold")
        self.driver.find_object("printer_cartridge")
        self.driver.find_object("printer_setting")
        self.driver.find_object("printer_share")
        self.driver.find_object("printer_status_description")
        self.driver.wait_for_object("printer_status_icon_fold", invisible=True)


    def click_add_first_printer_btn(self):
        """
        There is no printer was bound, click "添加打印机" button to add the first printer
        :return:
        """
        self.driver.click("add_printer")

    def click_personal_center_icon(self):
        """
        There is a "me" icon on the upper left corner of applet home page,and it jumps to the "我的" page with message center.
        :return:
        """
        self.driver.click("person_icon")

    def check_new_message_received(self):
        """
        When received a new notification message, there will be a red hot dot nearby the person icon
        :return:
        """
        self.driver.find_object("person_icon")
        self.driver.find_object("personal_msg_new")

    def check_announcement(self):
        """
        check the announcement exist in the home page
        :return:
        """
        self.driver.wait_for_object("announcement")

    def check_home_page_without_printer(self):
        """
        Verify the home page displayed with basic print option/menu
        :return:
        """
        self.check_file_print_no_device()
        self.check_img_print_no_device()
        self.check_invoice_print_no_device()
        self.check_id_copy_no_device()
        self.check_netdisk_print_no_device()
        self.check_url_print_no_device()
        self.check_id_photo_no_device()
        self.check_scan_no_device()

    def get_current_printer_index(self):
        """
        get the printer index in the list for which is current display on home page
        :return:
        """
        return int(self.driver.get_attribute("printer_component", "data-current"))

    def check_current_printer(self):
        """
        check the current printer's information on home page
        :return:
        """
        self.driver.get_attribute("printer_component", "data-current")

    def verify_printer_exist(self, printer_name):
        """
        verify the printer is exist in the home page printer list, by using the printer name
        :param printer_name: the printer's name going to check
        :return:
        """
        self.driver.wait_for_object("printer_spec", format_specifier=[printer_name])

    def verify_printer_new_icon(self, printer_name, invisible=False):
        """
        verify the printer is exist in the home page printer list, by using the printer name, and verify
        the new icon exist for the printer
        :param printer_name: the printer's name going to check
        :param invisible: if True, verify the new icon not exist
        :return:
        """
        self.driver.wait_for_object("new_icon", format_specifier=[printer_name], invisible=invisible)

    def verify_group_name(self, printer_name, group_name):
        """
        Check the group name on mini program home page
        :return:
        """
        printer = self.driver.wait_for_object("printer_spec", format_specifier=[printer_name])
        assert self.driver.get_text("group_name", root_obj=printer) == group_name

    def verify_mini_program_home_page(self):
        """
        Verify if the current page is mini program home page or not
        :return:
        """
        self.driver.wait_for_object("hp_cloud_print")

    def check_no_device_warm_promopt(self):
        """
        If there is no printer was bound, the warm prompt will pop up once you click the function button on home page
        if you click the "确定" button on the prompt, the pop up will be disappear
        :return:
        """
        self.driver.wait_for_object("warm_prompt_title")
        self.driver.wait_for_object("warm_prompt_msg")
        self.driver.click("warm_prompt_confirm")
        self.driver.wait_for_object("warm_prompt_msg", invisible=True)

    def check_advertisement(self):
        """
        check the advertisement carousel exist or not
        :return:
        """
        self.driver.wait_for_object("advertisement_items")

    def check_help_support_no_device(self):
        """
        Click the "帮助和支持" button, and verify the FAQ page displayed
        if the mobile screen is small, the "帮助和支持" button maybe hide need to scroll the screen
        :return:
        """
        self.click_help_and_support()
        self.driver.wait_for_object("help_support_close")
        self.driver.wait_for_object("customer_service")
        self.driver.wait_for_object("faq")
        self.close_help_support()
        self.driver.wait_for_object("customer_service", invisible=True)

    def check_hp_shop(self):
        """
        Click the "购物车" button, and verify the "HP 微商城" warm prompt pops up
        :return:
        """
        self.click_shopping_cart()
        # self.switch_to_native_view()
        # self.driver.click("consumable_popup_cancel")
        self.driver.press_key_back()

    def click_help_and_support(self):
        """
        Click on help and support link on mini program home page
        """
        self.driver.click("help_support")

    def close_help_support(self):
        """
        click "X" to close help and support component
        :return:
        """
        self.driver.click("help_support_close")

    def click_shopping_cart(self):
        """
        Click shopping cart icon, goto "HP 微商城"
        :return:
        """
        self.driver.click("shopping_cart")

    def check_file_print_no_device(self):
        """
        Click the "文件打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("file_print")
        self.check_no_device_warm_promopt()

    def check_img_print_no_device(self):
        """
        Click the "文件打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("img_print")
        self.check_no_device_warm_promopt()

    def check_invoice_print_no_device(self):
        """
        Click the "发票打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("invoice_print")
        self.check_no_device_warm_promopt()

    def check_id_copy_no_device(self):
        """
        Click the "身份证复印" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("ID_copy_print")
        self.check_no_device_warm_promopt()

    def check_netdisk_print_no_device(self):
        """
        Click the "百度网盘打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("baidu_netdisk_print")
        self.check_no_device_warm_promopt()

    def check_spice_print_no_device(self):
        """
        Click the "趣味打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("spice_print")
        self.driver.click("spice_print")
        self.driver.wait_for_object("womoooo_plugin")
        self.driver.press_key_back()
        self.driver.wait_for_object("womoooo_plugin", invisible=True)

    def check_url_print_no_device(self):
        """
        Click the "网络文章打印" button， the warm prompt will pop up
        :return:
        """
        self.click_url_article_print_section()
        self.check_no_device_warm_promopt()

    def check_id_photo_no_device(self):
        """
        Click the "证件照打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("ID_photo_print")
        self.check_no_device_warm_promopt()

    def check_scan_no_device(self):
        """
        Click the "扫描" button， the warm prompt will pop up
        :return:
        """
        self.driver.click("scan")
        self.check_no_device_warm_promopt()

    def select_add_printer(self):
        """
        Click the "添加打印机" button to add a new printer
        :return:
        """
        if self.driver.wait_for_object("add_printer_btn"):
            self.driver.click("add_printer_btn")
        else:
            self.driver.wait_for_object("add_printer_plus_icon").click()

    def scan_qrcode_with_camera(self, qr_code_valid=True):
        """
        click "扫一扫" and launch camera to scan a qrcode, lead to printer binding page
        :param: If the qr code is an HP printer qr code, set to True, if the qr code is not a printer, set to False
        """
        self.driver.click("scan_button")
        if qr_code_valid:
            self.driver.wait_for_object("mp_loading_icon", timeout=15, raise_e=False)
            self.driver.wait_for_object("mp_loading_icon", invisible=True)

    def goto_print_info_page(self):
        """
        Click "添加打印机" and then click "没有打印机信息页？", goto "如何打印信息页" guide page
        :return:
        """
        self.select_add_printer()
        self.driver.click("no_printer_info")

    def click_message_center_bell_icon(self):
        """
        Click on the bell icon - message center on mini program home page
        :return:
        """
        self.driver.click("mc_bell_icon")

    def click_url_article_print_section(self):
        """
        Click on the URL article print section
        :return:
        """
        self.driver.wait_for_object("web_article_print")
        self.driver.click("web_article_print")

    def click_person_icon(self):
        """
        Click on the personal center icon on mini program home screen
        :return:
        """
        self.driver.click("person_icon")

    def click_mp_home_3dot_menu(self):
        """
        Click the 3 dots menu on top right of the mini program home page
        :return:
        """
        self.driver.click("more_option_3dot_menu")

    def click_hb_test_account(self):
        """
        Click on the ‘HB测试号’ on the pops up menu after clicked the 3 dots more option menu
        :return:
        """
        self.driver.click("hp_test_account")

    def click_hp_pa_msg(self):
        """
        Click on the public account message after clicked the public account info on more option menu
        :return:
        """
        self.driver.click("hp_pa_account_msg")

    def click_hp_bridge_pa_test_account(self):
        """
        Click on the hp bridge pa test account to go to pa home page
        :return:
        """
        self.driver.click("hp_test_pa_account")

    def verify_new_message_reminder(self, message_exist=True):
        """
        Verify the new message count on top of the person icon
        :param message_exist: If you expect there is notification message, set the message_exist to true. Otherwise, set
                to False
        """
        sleep(1)
        current = self.driver.wait_for_object("message_number", timeout=2, raise_e=False)
        assert current if message_exist else current == message_exist

    def verify_home_page_displayed(self):
        """
        Verify the home page displayed with basic print option/menu
        :return:
        """
        self.driver.wait_for_object("hp_cloud_print_title")
        self.driver.find_object("file_print", timeout=5)
        self.driver.find_object("img_print", timeout=5)
        self.driver.find_object("invoice_print", timeout=5)
        self.driver.find_object("ID_copy_print", timeout=5)
        self.driver.find_object("baidu_netdisk_print", timeout=5)
        self.driver.find_object("voice_print", timeout=5)
        self.driver.find_object("HP_consumable", timeout=5)
        self.driver.find_object("url_print", timeout=5)
        self.driver.find_object("ID_photo_print", timeout=5)

    def get_mc_notifications_num(self):
        """
        Get the notifications amount on mini program home page
        :return if there is a number then return the notification amount, otherwise return 0
        """
        sleep(1)
        if self.driver.wait_for_object("notification_messages", timeout=3, raise_e=False):
            return int(self.driver.get_text("notification_messages"))
        else:
            return 0
