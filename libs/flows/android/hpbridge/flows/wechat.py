from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow, Stacks, QRCode
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from time import sleep
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import QRCode
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
import base64
import logging


class WeChat(HPBridgeFlow):
    flow_name = "wechat"

    def goto_pa(self):
        """
        from WeChat home page, go to HP Bridge public account device list page
        :return:
        """
        stack = utlitiy_misc.load_stack_info()
        if stack["stack"] == Stacks.DEV:
            mp_locator = "dev_public_account"
        else:
            mp_locator = "stage_public_account"
        self.launch_wechat()
        self.driver.wait_for_object("address_book_button")
        self.driver.click("address_book_button")
        self.driver.click("public_account_button")
        self.driver.click(mp_locator)

    def save_qrcode_to_device(self, printer_id):

        """
        this is a special method that will call generate QR code API for the specified printer,
         send the qrcode to the test mobile phone, under the special path: /sdcard/Pictures/QRCode
        :return:
        """
        qrcode_info = APIUtility().get_dbt_by_qrcode(printer_id, is_return=False)

        save_to_phone_path = "/sdcard/" + QRCode.valid
        # rm the old qrcode
        try:
            self.driver.wdvr.execute_script("mobile:shell", {"command": "rm {}/*".format(save_to_phone_path)})
        except:
            logging.info("/sdcard/a_printer/*  path not exist")

        sleep(1)
        # push the new qrcode to the device
        self.driver.wdvr.push_file(save_to_phone_path + "/QRcode.png", qrcode_info["data"])
        sleep(1)

    def send_qrcode(self, qrcode=QRCode.valid):
        """
        Choose a expected qrcode, Send an qrcode to the chat history,
        :param qrcode: value should under QRCode class,
        """
        self.launch_wechat()
        self.driver.wait_for_object("address_book_button")
        self.driver.click("qrcode_owner")
        self.driver.click("more_func")
        self.driver.click("wechat_album")
        self.driver.click("all_folder")
        self.driver.click("qrcode_folder", format_specifier=[qrcode])
        self.driver.click("img_list", index=0)
        self.driver.click("send_btn")
        self.driver.wait_for_object("qrcode_list")


    def scan_qrcode_to_mp(self, public_account_qr_code=False):
        """
        Launch HP Bridge mini program by sacn the printer QR code
        :param:public_account_qr_code - Extend printer QR code(default) or Public QR code(set to True)
        """
        if not self.driver.find_object("qrcode_chat_page", raise_e=False):
            self.driver.press_key_home()
            self.launch_wechat()
            self.driver.wait_for_object("address_book_button")
            self.driver.click("qrcode_owner")
        self.driver.click("qrcode_list", index=-1)
        self.driver.long_press("full_screen")
        if not public_account_qr_code:
            self.driver.click("qrcode_recognize")
        else:
            self.driver.wait_for_object("public_account_qrcode_recognize").click()

    def back_from_qrcode(self):
        """
        Go back to Wechat home page from chat window with a QR code opened
        :return:
        """
        self.driver.click("full_screen")
        self.driver.press_key_back()

    def goto_mp(self):
        """
        According to the stack parameter, launch the corresponding HP Bridge mini program
        from WeChat "my mini programs list"
        :param stack: which program going to launch
        :return:
        """
        stack = utlitiy_misc.load_stack_info()
        if stack["stack"] == Stacks.DEV:
            mp_locator = "mp_icon_dev"
        else:
            mp_locator = "mp_icon_stage"
        self.launch_wechat()
        self.driver.wait_for_object("address_book_button")
        self.driver.swipe(direction="up", per_offset=0.7)
        self.driver.wait_for_object(mp_locator)
        self.driver.click(mp_locator)
        sleep(5)



