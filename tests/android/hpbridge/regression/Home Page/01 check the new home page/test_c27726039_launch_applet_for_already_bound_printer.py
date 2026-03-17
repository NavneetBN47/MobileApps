import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterNameOption
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
pytest.app_info = "hpbridge"
HPBridgeFlow.set_pytest_data()


class TestNewHomePage(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.mp_faq = self.fc.flow["mp_faq"]
        self.binding = self.fc.flow["bind_printer"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_my_printer = self.fc.flow["pa_my_printer"]
        self.msg_center = self.fc.flow["mp_message_center"]

        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it.
            4. The test printer is not bound with the login Wechat account.
        """
        # define variables
        self.printer_name = PrinterNameOption.OFFICE.value
        api_uitility = APIUtility()
        api_uitility.unbind_all_printers()

    def test_01_new_home_page_fields(self):
        """
        Steps：
            1. Search out the WeChat Applet and then launch the Applet.
                Check the all stings and buttons on new home page.
            2. Click all buttons on this page.

        Expected:
            1. Verify the printer home page with no bound printer display correctly.
            2. Verify the "Me" icon displayed on the upper left corner of applet home page,and it jumps to the "我的" page with message center.
            3. Verify the announcement displayed correctly.
            4. Verify the "添加打印机" displayed correctly and it will jump to the "绑定打印机" page.
            5. Verify the"文档打印" "照片打印" "百度网盘打印""发票打印" "网络文章打印" "证件照打印" and "身份证复印"displayed well, red "新" displayed on the top right corner of "网络文章打印" and "证件照打印"(The "新" lab will never disappear) , and "您还未绑定设备，请先添加打印机" will pop up when click on it.
            6. Verify the advertisement carousel displayed correctly.
            7. Verify the "?" and "shop" icon displayed on the middle right of applet home page,and "售后服务""X"“帮助”should be displayed when click the "?" icon.
            8. Verify the content store displayed correctly.
        :return:
        """
        self.wechat.goto_mp()
        # 1. Verify the printer home page with no bound printer display correctly.
        self.mphome.check_add_printer_filed_no_device()
        # 2. Verify the "Me" icon displayed on the upper left corner of applet home page,and it jumps to the "我的" page with message center.
        self.mphome.click_personal_center_icon()
        self.msg_center.check_page_title()
        self.msg_center.back_to_home_page()
        # 3. Verify the announcement displayed correctly.
        self.mphome.check_announcement()
        self.mphome.click_add_first_printer_btn()
        self.binding.check_bind_printer_page()
        self.binding.back_to_home_page()
        # 5. Verify the"文档打印" "照片打印" "百度网盘打印""发票打印" "网络文章打印" "证件照打印" and "身份证复印"displayed well, red "新" displayed on the top right corner of "网络文章打印" and "证件照打印"(The "新" lab will never disappear) , and "您还未绑定设备，请先添加打印机" will pop up when click on it.

        self.mphome.check_home_page_without_printer()
        # 6. Verify the advertisement carousel displayed correctly.
        self.mphome.check_advertisement()

        # 7. Verify the "?" and "shop" icon displayed on the middle right of applet home page,and "售后服务""X"“帮助”should be displayed when click the "?" icon.
        self.mphome.check_hp_shop()
        self.mphome.check_help_support_no_device()


    def test_02_add_and_remove_printer(self):
        """
        Steps；
            1.Click the "添加打印机.." button to 添加打印机 page.
            2.Click the "扫一扫" button and "绑定打印机" button to bound the first printer for the new user.
            3.Enter the Wechat Official Account and then go to unbind the printer.
            4.Launch the Applet and go to the printer home page.
        Expected:
            Verify the printer home page with new bound printer display well.
            Verify there is a red "新" in the upper right corner of the printer icon.
            Verify the printer name display right of the printer icon.
            Verify the unbind the printer operation can be performed successfully.
            Verify there is no bound printer on home page.
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.change_printer_name(self.printer_name)
        self.binding.bind_printer(bound=False)
        self.mphome.verify_printer_exist(self.printer_name)
        self.mphome.verify_printer_new_icon(self.printer_name)
        self.driver.press_key_home()
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.verify_printer_under_account(self.printer_name)
        self.pa_my_printer.unbind_printer(self.printer_name)
        self.pa_home.goto_wechat_from_pa()
        self.wechat.goto_mp()
        self.mphome.check_add_printer_filed_no_device()

